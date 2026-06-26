<template>
  <div class="categories-page">
    <h2>分类浏览</h2>
    <p class="subtitle">按游戏分类查看攻略</p>
    <div v-if="loading && cats.length === 0" style="text-align:center;padding:60px 0;color:var(--text-muted)">加载中...</div>
    <div v-for="cat in cats" :key="cat.id" class="cat-section">
      <div class="cat-header" @click="toggleCat(cat.id)">
        <h3>{{ cat.categoryName }}</h3>
        <span class="cat-count">{{ (catGames[cat.id] || []).length }} 款</span>
      </div>
      <div v-show="openCats.includes(cat.id)" class="cat-games">
          <div v-for="g in (catGames[cat.id] || [])" :key="g.id" class="cat-game" @click="$router.push('/games/' + g.id)">
          <div class="cat-game-title">{{ g.title }}</div>
          <div class="cat-game-meta">{{ g.rating }} 分 / {{ g.platform }}</div>
        </div>
        <div v-if="!(catGames[cat.id] || []).length" class="empty">暂无游戏</div>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { ref, onMounted } from "vue"; import { useRouter } from "vue-router"; import { gameApi } from "@/api"; import type { GameCategory, GameItem } from "@/types"
const router = useRouter(); const cats = ref<GameCategory[]>([]); const catGames = ref<Record<number,GameItem[]>>({}); const openCats = ref<number[]>([]); const loading = ref(true)
function toggleCat(id: number) { const i = openCats.value.indexOf(id); if(i>=0) openCats.value.splice(i,1); else openCats.value.push(id) }
onMounted(async () => {
  try { const r = await gameApi.getCategories(); cats.value = r.data || []
    for (const c of cats.value) { try { const gr = await gameApi.getGameList({ categoryId: c.id }); catGames.value[c.id] = gr.data } catch {} }
  } catch {} finally { loading.value = false }
})
</script>
<style scoped>
.categories-page { max-width:900px; margin:0 auto; padding:20px; }
.categories-page h2 { margin:0; font-size:24px; }
.subtitle { margin:4px 0 24px; font-size:14px; color:var(--text-muted); }
.cat-section { margin-bottom:12px; border-radius:12px; overflow:hidden; background:var(--glass-bg); border:1px solid var(--glass-border); }
.cat-header { display:flex; justify-content:space-between; align-items:center; padding:14px 18px; cursor:pointer; transition:all 0.2s; user-select:none; }
.cat-header:hover { background:rgba(0,0,0,0.03); }
.cat-header h3 { margin:0; font-size:16px; font-weight:600; }
.cat-count { font-size:13px; color:var(--text-muted); }
.cat-games { padding:0 18px 12px; }
.cat-game { display:flex; justify-content:space-between; align-items:center; padding:10px 14px; border-radius:8px; cursor:pointer; transition:all 0.2s; margin-top:4px; }
.cat-game:hover { background:rgba(0,0,0,0.04); }
.cat-game-title { font-size:14px; font-weight:500; }
.cat-game-meta { font-size:12px; color:var(--text-muted); }
.empty { text-align:center; padding:16px; color:var(--text-muted); font-size:13px; }
</style>
