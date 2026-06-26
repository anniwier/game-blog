<template>
  <div class="game-detail">
    <el-card v-if="game" class="detail-card">
      <div class="detail-header">
        <img :src="game.coverImage" :alt="game.title" class="detail-cover" />
        <div class="detail-info">
          <h1>{{ game.title }}</h1>
          <div class="detail-meta">
            <span><el-icon><User /></el-icon> {{ game.authorName }}</span>
            <span><el-icon><Clock /></el-icon> {{ game.publishedAt }}</span>
            <span><el-icon><StarFilled /></el-icon> {{ game.rating }}</span>
            <span><el-icon><View /></el-icon> {{ game.viewCount }}</span>
            <span><el-icon @click="toggleFavorite" :style="{ color: isFavorited ? '#e74c3c' : '#999', cursor: 'pointer' }"><Star /></el-icon> {{ game.favoriteCount }}</span>
          </div>
          <div class="detail-tags" v-if="game.tags && game.tags.length > 0">
            <el-tag
              v-for="tag in game.tags"
              :key="tag.id"
              :color="tag.color || '#409eff'"
              style="color: #fff; margin-right: 8px;"
            >
              {{ tag.tagName }}
            </el-tag>
          </div>
          <div class="detail-info-grid">
            <div><strong>平台：</strong>{{ game.platform }}</div>
            <div><strong>开发商：</strong>{{ game.developer }}</div>
            <div><strong>发行商：</strong>{{ game.publisher }}</div>
            <div><strong>发行日期：</strong>{{ game.releaseDate }}</div>
            <div><strong>分类：</strong>{{ game.categoryName }}</div>
          </div>
        </div>
      </div>

      <el-divider />

      <div class="detail-content">
        <h2>游戏介绍</h2>
        <div class="markdown-body" v-html="renderedContent"></div>
      </div>

      <el-divider />

      <!-- Related Games -->
      <div class="related-games" v-if="relatedGames.length > 0">
        <h2>相关游戏推荐</h2>
        <el-row :gutter="16">
          <el-col :xs="24" :sm="12" :md="6" v-for="rg in relatedGames" :key="rg.id">
            <el-card class="related-card" :body-style="{ padding: '0px' }" @click="goToGame(rg.id)">
              <img :src="rg.coverImage" class="related-cover" :alt="rg.title" />
              <div class="related-info">
                <h4>{{ rg.title }}</h4>
                <span class="related-rating"><el-icon><StarFilled /></el-icon> {{ rg.rating }}</span>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </div>

      <div class="detail-comments">
        <h2>评论 ({{ comments.length }})</h2>
        <div class="comment-form" v-if="userStore.isLoggedIn()">
          <el-input
            v-model="newComment"
            type="textarea"
            :rows="3"
            placeholder="写下你的评论..."
          />
          <el-button type="primary" @click="submitComment" style="margin-top: 10px;">
            发表评论
          </el-button>
        </div>
        <div v-else class="login-tip">
          <router-link to="/login">登录</router-link>后即可发表评论
        </div>

        <div class="comment-list" v-if="comments.length > 0">
          <div class="comment-item" v-for="comment in comments" :key="comment.id">
            <el-avatar :src="comment.avatar" :size="40" />
            <div class="comment-body">
              <div class="comment-header">
                <span class="comment-username">{{ comment.username }}</span>
                <span class="comment-time">{{ comment.createdAt }}</span>
              </div>
              <p class="comment-content">{{ comment.content }}</p>
              <el-button
                v-if="userStore.userInfo?.id === comment.userId"
                type="danger"
                size="small"
                link
                @click="deleteComment(comment.id)"
              >
                删除
              </el-button>
            </div>
          </div>
        </div>
        <el-empty v-else description="暂无评论" />
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { marked } from 'marked'
import { User, Clock, StarFilled, View } from '@element-plus/icons-vue'
import { gameApi, commentApi, favoriteApi } from '@/api'
import { useUserStore } from '@/stores/user'
import { ElMessage } from 'element-plus'
import type { GameItem, CommentInfo } from '@/types'

const route = useRoute()
const router = useRouter()
const userStore = useUserStore()
const game = ref<GameItem | null>(null)
const comments = ref<CommentInfo[]>([])
const newComment = ref('')
const isFavorited = ref(false)
const favoriteLoading = ref(false)
const relatedGames = ref<GameItem[]>([])
const renderedContent = computed(() => {
  if (!game.value?.content) return ''
  return marked.parse(game.value.content)
})

onMounted(async () => {
  const id = Number(route.params.id)
  try {
    const res = await gameApi.getGameDetail(id)
    game.value = res.data
    await loadComments()
    if (userStore.isLoggedIn()) {
      const favRes = await favoriteApi.checkFavorite(id)
      isFavorited.value = favRes.data
    }
    // Fetch related games
    const relRes = await gameApi.getGameList({ categoryId: game.value.categoryId })
    relatedGames.value = relRes.data.filter((g) => g.id !== id).slice(0, 4)
  } catch (error) {
    console.error('获取游戏详情失败:', error)
  }
})

function goToGame(id) {
  router.push("/games/" + id)
}

async function toggleFavorite() {
  if (!userStore.isLoggedIn()) {
    ElMessage.warning('请先登录')
    return
  }
  favoriteLoading.value = true
  try {
    const id = Number(route.params.id)
    if (isFavorited.value) {
      await favoriteApi.removeFavorite(id)
      isFavorited.value = false
      if (game.value) game.value.favoriteCount--
      ElMessage.success('已取消收藏')
    } else {
      await favoriteApi.addFavorite(id)
      isFavorited.value = true
      if (game.value) game.value.favoriteCount++
      ElMessage.success('已收藏')
    }
  } catch (error) {
    ElMessage.error('操作失败')
  } finally {
    favoriteLoading.value = false
  }
}

async function loadComments() {
  const id = Number(route.params.id)
  try {
    const res = await commentApi.getGameComments(id)
    comments.value = res.data
  } catch (error) {
    console.error('获取评论失败:', error)
  }
}

async function submitComment() {
  if (!newComment.value.trim()) {
    ElMessage.warning('请输入评论内容')
    return
  }
  try {
    await commentApi.addComment({
      gameId: Number(route.params.id),
      content: newComment.value
    })
    ElMessage.success('评论成功')
    newComment.value = ''
    await loadComments()
  } catch (error) {
    ElMessage.error('评论失败')
  }
}

async function deleteComment(commentId: number) {
  try {
    await commentApi.deleteComment(commentId)
    ElMessage.success('删除成功')
    await loadComments()
  } catch (error) {
    ElMessage.error('删除失败')
  }
}
</script>

<style scoped>
.markdown-body {
  line-height: 1.9;
  font-size: 16px;
  color: var(--text-primary);
}
.markdown-body h1,
.markdown-body h2,
.markdown-body h3 {
  margin: 1.2em 0 0.6em;
  color: var(--text-primary);
  font-weight: 700;
  line-height: 1.3;
}
.markdown-body h1 { font-size: 26px; padding-bottom: 8px; border-bottom: 2px solid var(--border-color); }
.markdown-body h2 { font-size: 22px; padding-bottom: 6px; border-bottom: 1px solid var(--border-color); }
.markdown-body h3 { font-size: 18px; }
.markdown-body p { margin: 0.6em 0; }
.markdown-body ul, .markdown-body ol { padding-left: 24px; }
.markdown-body li { margin: 0.4em 0; }
.markdown-body strong { font-weight: 700; color: var(--text-primary); }
.markdown-body code {
  background: var(--glass-bg);
  padding: 3px 8px;
  border-radius: 6px;
  font-size: 14px;
  border: 1px solid var(--glass-border);
}
.markdown-body table {
  width: 100%;
  border-collapse: collapse;
  margin: 1em 0;
}
.markdown-body th, .markdown-body td {
  padding: 10px 14px;
  border: 1px solid var(--border-color);
  text-align: left;
}
.markdown-body th {
  background: var(--glass-bg);
  font-weight: 600;
}

@keyframes favPop { 0% { transform: scale(1); } 50% { transform: scale(1.35); } 100% { transform: scale(1); } }

.game-detail {
  max-width: 900px;
  margin: 0 auto;
  padding: 20px;
}

.detail-header {
  display: flex;
  gap: 30px;
}

.detail-cover {
  width: 300px;
  height: 400px;
  object-fit: cover;
  border-radius: 8px;
}

.detail-info {
  flex: 1;
}

.detail-info h1 {
  margin: 0 0 16px;
  font-size: 28px;
}

.detail-meta {
  display: flex;
  gap: 20px;
  margin-bottom: 16px;
  color: #666;
  font-size: 14px;
}

.detail-meta span {
  display: flex;
  align-items: center;
  gap: 4px;
}

.detail-tags {
  margin-bottom: 16px;
}

.detail-info-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  font-size: 14px;
  color: #333;
}

.detail-content {
  line-height: 1.8;
  font-size: 15px;
}

.comment-form {
  margin-bottom: 20px;
}

.login-tip {
  text-align: center;
  color: #999;
  padding: 20px;
}

.comment-list {
  margin-top: 20px;
}

.comment-item {
  display: flex;
  gap: 12px;
  padding: 12px 0;
  border-bottom: 1px solid #eee;
}

.comment-body {
  flex: 1;
}

.comment-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 6px;
}

.comment-username {
  font-weight: 600;
  font-size: 14px;
}

.comment-time {
  font-size: 12px;
  color: #999;
}

.comment-content {
  margin: 0;
  font-size: 14px;
  line-height: 1.6;
}
</style>
