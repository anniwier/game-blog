<template>
  <div class="home">
    <!-- Custom Carousel -->
    <div class="custom-carousel">
      <div class="carousel-slide" v-for="(game, idx) in featuredGames" :key="game.id" v-show="currentSlide === idx">
        <div class="carousel-bg" :style="{ background: 'url(' + game.coverImage + ') center/cover no-repeat, ' + gradients[idx % gradients.length] }">
          <div class="carousel-overlay">
            <h2 class="carousel-title">{{ game.title }}</h2>
            <p class="carousel-summary">{{ game.summary }}</p>
            <div class="carousel-meta">
              <el-tag v-for="tag in game.tags" :key="tag.id" :color="tag.color || '#409eff'" size="small" style="color:#fff;margin-right:6px;">{{ tag.tagName }}</el-tag>
              <span class="carousel-rating"><el-icon><StarFilled /></el-icon> {{ game.rating }}</span>
            </div>
            <el-button type="primary" size="large" round @click="goToGame(game.id)">查看详情</el-button>
          </div>
        </div>
      </div>
      <div class="carousel-dots">
        <span v-for="(g, i) in featuredGames" :key="g.id" :class="{ active: currentSlide === i }" @click="currentSlide = i"></span>
      </div>
    </div>

    <div class="search-bar">
      <el-input v-model="keyword" placeholder="搜索游戏..." clearable class="search-input" @keyup.enter="handleSearch">
        <template #append>
          <el-button @click="handleSearch" :icon="Search" />
        </template>
      </el-input>
    </div>

    <div class="category-filter" v-if="categories.length > 0">
      <el-tag :type="selectedCategory === null ? 'primary' : 'info'" class="category-tag" @click="filterByCategory(null)">全部</el-tag>
      <el-tag v-for="cat in categories" :key="cat.id" :type="selectedCategory === cat.id ? 'primary' : 'info'" class="category-tag" @click="filterByCategory(cat.id)">{{ cat.categoryName }}</el-tag>
    </div>

    <div class="section-header">
      <h1>GameBlog</h1>
      <p>发现精彩的游戏世界</p>
      <span class="game-count">共 {{ games.length }} 款游戏</span>
    </div>

    <div class="game-list">
      <el-row :gutter="20">
        <el-col :xs="24" :sm="12" :md="8" :lg="6" v-for="(game, index) in games" :key="game.id">
          <el-card class="game-card" :style="{ '--delay': index * 0.08 + 's' }" :body-style="{ padding: '0px' }" @click="goToGame(game.id)">
            <div class="game-cover-wrap">
              <img :src="game.coverImage" class="game-cover" :alt="game.title" @error="handleCardImgError" />
            </div>
            <div class="game-info">
              <h3 class="game-title">{{ game.title }}</h3>
              <p class="game-summary">{{ game.summary }}</p>
              <div class="game-meta">
                <span class="game-rating"><el-icon><StarFilled /></el-icon> {{ game.rating }}</span>
                <span class="game-platform">{{ game.platform }}</span>
              </div>
              <div class="game-tags" v-if="game.tags && game.tags.length > 0">
                <el-tag v-for="tag in game.tags" :key="tag.id" :color="tag.color || '#409eff'" size="small" style="color:#fff; margin-right:4px;cursor:pointer;" @click.stop="goToTag(tag.id)">{{ tag.tagName }}</el-tag>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { StarFilled, Search } from '@element-plus/icons-vue'
import { gameApi } from '@/api'
import type { GameItem, GameCategory } from '@/types'

const router = useRouter()
const games = ref<GameItem[]>([])
const categories = ref<GameCategory[]>([])
const keyword = ref('')
const selectedCategory = ref<number | null>(null)
const featuredGames = ref<GameItem[]>([])
const currentSlide = ref(0)
let slideTimer = 0
const gradients = computed(() => [
  'linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%)',
  'linear-gradient(135deg, #0f3443 0%, #0d7377 50%, #34e89e 100%)',
  'linear-gradient(135deg, #2d1b69 0%, #6c3483 50%, #bb8fce 100%)',
  'linear-gradient(135deg, #7b241c 0%, #c0392b 50%, #f1948a 100%)',
])

function handleCardImgError(e: Event) {
  const img = e.target as HTMLImageElement
  img.style.display = 'none'
}

onMounted(async () => {
  try {
    const res = await gameApi.getGameList()
    games.value = res.data
    // Pick 4 random games for the carousel
    const shuffled = [...res.data].sort(() => Math.random() - 0.5)
    featuredGames.value = shuffled.slice(0, 4)
    const catRes = await gameApi.getCategories()
    categories.value = catRes.data || []
    startSlideTimer()
  } catch (error) {
    console.error('获取游戏列表失败:', error)
  }
})

function startSlideTimer() {
  if (slideTimer) clearInterval(slideTimer)
  slideTimer = window.setInterval(() => {
    if (featuredGames.value.length > 0) {
      currentSlide.value = (currentSlide.value + 1) % featuredGames.value.length
    }
  }, 5000)
}

onUnmounted(() => { if (slideTimer) clearInterval(slideTimer) })

async function handleSearch() {
  try {
    const params: any = {}
    if (keyword.value.trim()) params.keyword = keyword.value.trim()
    if (selectedCategory.value !== null) params.categoryId = selectedCategory.value
    const res = await gameApi.getGameList(params)
    games.value = res.data
  } catch (error) {
    console.error('搜索失败:', error)
  }
}

async function filterByCategory(categoryId: number | null) {
  selectedCategory.value = categoryId
  try {
    const params: any = {}
    if (categoryId !== null) params.categoryId = categoryId
    if (keyword.value.trim()) params.keyword = keyword.value.trim()
    const res = await gameApi.getGameList(params)
    games.value = res.data
  } catch (error) {
    console.error('筛选失败:', error)
  }
}

function goToTag(tagId: number) { router.push("/tags/" + tagId) }

function goToGame(id: number) {
  router.push('/games/' + id)
}
</script>

<style scoped>
.home {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

/* Custom Carousel Styles - matching template classes */
.custom-carousel {
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  margin-bottom: 24px;
  height: 360px;
}
.carousel-slide {
  position: absolute;
  inset: 0;
}
.carousel-bg {
  width: 100%;
  height: 100%;
  position: relative;
}
.carousel-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 40px;
  background: linear-gradient(transparent, rgba(0,0,0,0.8));
  color: #fff;
}
.carousel-title {
  font-size: 28px;
  margin-bottom: 8px;
  font-weight: 700;
  text-shadow: 0 2px 8px rgba(0,0,0,0.6);
}
.carousel-summary {
  font-size: 14px;
  opacity: 0.9;
  margin-bottom: 12px;
  max-width: 500px;
  text-shadow: 0 1px 4px rgba(0,0,0,0.5);
}
.carousel-meta {
  display: flex;
  align-items: center;
  margin-bottom: 16px;
}
.carousel-rating {
  display: flex;
  align-items: center;
  gap: 4px;
  color: #fbbf24;
  font-size: 14px;
  margin-left: 8px;
}
.carousel-dots {
  position: absolute;
  bottom: 16px;
  right: 24px;
  display: flex;
  gap: 8px;
  z-index: 10;
}
.carousel-dots span {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: rgba(255,255,255,0.4);
  cursor: pointer;
  transition: all 0.3s;
}
.carousel-dots span.active {
  background: #fff;
  transform: scale(1.3);
}

.search-bar { margin-bottom: 16px; }
.search-input { max-width: 480px; }
.category-filter { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 20px; }
.category-tag { cursor: pointer; transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1); padding: 4px 0 !important; }
.category-tag:hover { transform: translateY(-2px); filter: brightness(1.1); }

.section-header {
  display: flex;
  align-items: baseline;
  gap: 12px;
  margin-bottom: 24px;
  padding: 0 4px;
}
.section-header h1 {
  font-size: 28px;
  color: var(--text-primary);
  font-weight: 800;
  background: linear-gradient(135deg, var(--text-primary), var(--el-menu-active));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.section-header p { font-size: 15px; color: var(--text-secondary); }
.game-count { margin-left: auto; font-size: 13px; color: var(--text-muted); }

.game-list { padding: 0; }
.game-card {
  cursor: pointer;
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  margin-bottom: 24px;
  animation: cardFadeIn 0.5s ease both;
  animation-delay: var(--delay, 0s);
  overflow: hidden;
}
.game-card:hover { transform: translateY(-8px); box-shadow: 0 16px 48px rgba(0,0,0,0.15); }

@keyframes cardFadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.game-cover-wrap {
  width: 100%;
  height: 200px;
  overflow: hidden;
  background: var(--bg-secondary);
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}
.game-cover {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.game-info { padding: 14px; }
.game-info .game-title {
  margin: 0 0 8px;
  font-size: 18px;
  font-weight: 600;
}
.game-summary {
  margin: 0 0 12px;
  font-size: 14px;
  color: var(--text-secondary);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.game-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
  font-size: 13px;
  color: var(--text-muted);
}
.game-rating {
  display: flex;
  align-items: center;
  gap: 4px;
  color: var(--rating-color);
}
.game-tags { display: flex; flex-wrap: wrap; gap: 4px; }
</style>