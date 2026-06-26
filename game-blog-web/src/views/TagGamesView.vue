<template>
  <div class="tag-page">
    <div class="tag-header"><h2>{{ tagName || '标签筛选' }}</h2><span>共 {{ games.length }} 款游戏</span></div>
    <el-row :gutter="20">
      <el-col :xs="24" :sm="12" :md="8" :lg="6" v-for="g in games" :key="g.id">
        <el-card class="game-card" :body-style="{ padding: '0px' }" @click="$router.push('/games/' + g.id)">
          <img :src="g.coverImage" class="game-cover" :alt="g.title" />
          <div class="game-info">
            <h3>{{ g.title }}</h3><p>{{ g.summary }}</p>
            <div class="game-meta"><span><el-icon><StarFilled /></el-icon> {{ g.rating }}</span><span>{{ g.platform }}</span></div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>
<script setup lang="ts">
import { ref, onMounted } from "vue"; import { useRoute, useRouter } from "vue-router"; import { StarFilled } from "@element-plus/icons-vue"; import { gameApi } from "@/api"; import type { GameItem } from "@/types"
const route = useRoute(); const router = useRouter(); const games = ref<GameItem[]>([]); const tagName = ref("")
onMounted(async () => {
  const id = Number(route.params.tagId)
  const [gr, tr] = await Promise.all([gameApi.getGameListByTag(id), gameApi.getTags()])
  games.value = gr.data; const found = tr.data.find((t:any) => t.id === id); if (found) tagName.value = found.tagName
})
</script>
<style scoped>
.tag-page { max-width:1200px; margin:0 auto; padding:20px; }
.tag-header { display:flex; align-items:baseline; gap:12px; margin-bottom:24px; }
.tag-header h2 { font-size:24px; margin:0; }
.tag-header span { font-size:13px; color:var(--text-muted); }
.game-card { cursor:pointer; margin-bottom:20px; transition:transform 0.3s; }
.game-card:hover { transform:translateY(-5px); }
.game-cover { width:100%; height:200px; object-fit:cover; }
.game-info { padding:14px; }
.game-info h3 { margin:0 0 8px; font-size:18px; font-weight:600; }
.game-info p { margin:0 0 12px; font-size:14px; color:var(--text-secondary); display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; }
.game-meta { display:flex; justify-content:space-between; font-size:13px; color:var(--text-muted); }
</style>