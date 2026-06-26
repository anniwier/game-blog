<template>
  <div class="ranking-page">
    <h2>游戏排行榜</h2>
    <p class="subtitle">按热度排行，发现最受欢迎的游戏</p>
    <div v-if="games.length === 0" style="text-align:center;padding:60px 0;color:var(--text-muted)">加载中...</div>
          <div v-for="(g, i) in games" :key="g.id" class="rank-item" @click="$router.push('/games/' + g.id)">
      <div class="rank-num">{{ i + 1 }}</div>
      <div class="rank-info">
        <div class="rank-title">{{ g.title }}</div>
        <div class="rank-meta">
          <span>评分: {{ g.rating }}</span><span>{{ g.platform }}</span><span>{{ g.viewCount }} 次浏览</span>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { ref, onMounted } from "vue"; import { useRouter } from "vue-router"; import { gameApi } from "@/api"; import type { GameItem } from "@/types"
const router = useRouter(); const games = ref<GameItem[]>([])
onMounted(async () => { try { const r = await gameApi.getTopGames(); games.value = r.data } catch {} })
</script>
<style scoped>
.ranking-page { max-width:800px; margin:0 auto; padding:20px; }
.ranking-page h2 { margin:0; font-size:24px; }
.subtitle { margin:4px 0 24px; font-size:14px; color:var(--text-muted); }
.rank-item { display:flex; align-items:center; gap:16px; padding:16px; border-radius:12px; cursor:pointer; transition:all 0.25s; margin-bottom:8px; background:var(--glass-bg); border:1px solid var(--glass-border); }
.rank-item:hover { transform:translateX(6px); box-shadow:var(--glass-shadow); }
.rank-num { width:40px; height:40px; display:flex; align-items:center; justify-content:center; border-radius:50%; font-size:18px; font-weight:700; background:linear-gradient(135deg,var(--el-menu-active),#764ba2); color:#fff; flex-shrink:0; }
.rank-info { flex:1; min-width:0; }
.rank-title { font-size:16px; font-weight:600; margin-bottom:4px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
.rank-meta { display:flex; gap:16px; font-size:13px; color:var(--text-muted); }
</style>
