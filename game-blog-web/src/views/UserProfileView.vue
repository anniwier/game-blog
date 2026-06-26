<template>
  <div class="profile">
    <el-card class="profile-card">
      <h2>个人中心</h2>
      <div class="profile-info" v-if="userStore.userInfo">
        <el-avatar :src="userStore.userInfo.avatar" :size="80" />
        <div class="profile-details">
          <p><strong>昵称：</strong>{{ userStore.userInfo.nickname }}</p>
          <p><strong>用户名：</strong>{{ userStore.userInfo.username }}</p>
          <p><strong>邮箱：</strong>{{ userStore.userInfo.email || '未设置' }}</p>
          <p><strong>注册时间：</strong>{{ userStore.userInfo.createdAt }}</p>
        </div>
      </div>
    </el-card>

    <el-card class="favorites-card" v-if="userStore.isLoggedIn()">
      <h2>我的收藏 ({{ favoriteGames.length }})</h2>
      <el-empty v-if="favoriteGames.length === 0" description="还没有收藏任何游戏" />
      <el-row :gutter="20" v-else>
        <el-col :xs="24" :sm="12" :md="8" v-for="game in favoriteGames" :key="game.id">
          <el-card class="fav-card" :body-style="{ padding: '0px' }" @click="goToGame(game.id)">
            <img :src="game.coverImage" class="fav-cover" :alt="game.title" />
            <div class="fav-info">
              <h3 class="fav-title">{{ game.title }}</h3>
              <div class="fav-meta">
                <span class="fav-rating"><el-icon><StarFilled /></el-icon> {{ game.rating }}</span>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { StarFilled } from '@element-plus/icons-vue'
import { useUserStore } from '@/stores/user'
import { favoriteApi, gameApi } from '@/api'
import type { GameItem } from '@/types'

const router = useRouter()
const userStore = useUserStore()
const favoriteGames = ref<GameItem[]>([])

onMounted(async () => {
  if (userStore.isLoggedIn() && !userStore.userInfo) {
    await userStore.getUserInfo()
  }
  if (userStore.isLoggedIn()) {
    await loadFavorites()
  }
})

async function loadFavorites() {
  try {
    const res = await favoriteApi.getUserFavorites()
    const ids = res.data.map((f: any) => f.gameId)
    const games = []
    for (const id of ids) {
      const gameRes = await gameApi.getGameDetail(id)
      games.push(gameRes.data)
    }
    favoriteGames.value = games
  } catch (error) {
    console.error('获取收藏列表失败:', error)
  }
}

function goToGame(id: number) {
  router.push('/games/' + id)
}
</script>

<style scoped>
.profile {
  max-width: 900px;
  margin: 0 auto;
  padding: 20px;
}
.profile-card {
  margin-bottom: 20px;
}
.profile-card h2 {
  margin-bottom: 20px;
}
.profile-info {
  display: flex;
  gap: 30px;
  align-items: flex-start;
}
.profile-details {
  flex: 1;
}
.profile-details p {
  margin: 8px 0;
  font-size: 15px;
}
.favorites-card h2 {
  margin-bottom: 16px;
}
.fav-card {
  cursor: pointer;
  transition: transform 0.3s;
  margin-bottom: 16px;
}
.fav-card:hover {
  transform: translateY(-4px);
}
.fav-cover {
  width: 100%;
  height: 160px;
  object-fit: cover;
}
.fav-info {
  padding: 10px;
}
.fav-title {
  margin: 0 0 6px;
  font-size: 15px;
  font-weight: 600;
}
.fav-meta {
  font-size: 13px;
  color: #888;
}
.fav-rating {
  display: flex;
  align-items: center;
  gap: 3px;
  color: #f59e0b;
}
</style>
