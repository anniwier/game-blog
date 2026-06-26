<template>
  <div class="admin-page">
    <div class="admin-header">
      <h2>文章管理</h2>
      <el-button type="primary" @click="$router.push('/admin/articles/new')">新建文章</el-button>
    </div>
    <el-table :data="articles" stripe style="width: 100%">
      <el-table-column prop="id" label="ID" width="60" />
      <el-table-column prop="title" label="标题" min-width="200" />
      <el-table-column prop="categoryName" label="分类" width="100" />
      <el-table-column prop="platform" label="平台" width="120" />
      <el-table-column prop="rating" label="评分" width="80" />
      <el-table-column prop="viewCount" label="浏览" width="80" />
      <el-table-column label="操作" width="160" fixed="right">
        <template #default="{ row }">
          <el-button size="small" @click="edit(row.id)">编辑</el-button>
          <el-button size="small" type="danger" @click="remove(row.id)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue"
import { useRouter } from "vue-router"
import { gameApi } from "@/api"
import { ElMessage, ElMessageBox } from "element-plus"
import type { GameItem } from "@/types"

const router = useRouter()
const articles = ref<GameItem[]>([])

onMounted(async () => {
  try {
    const res = await gameApi.getGameList()
    articles.value = res.data
  } catch (e: any) {
    ElMessage.error("获取文章列表失败")
  }
})

function edit(id: number) {
  router.push("/admin/articles/edit/" + id)
}

async function remove(id: number) {
  try {
    await ElMessageBox.confirm("确定要删除这篇文章吗？", "提示", { type: "warning" })
    await gameApi.deleteGame(id)
    ElMessage.success("已删除")
    articles.value = articles.value.filter((a: any) => a.id !== id)
  } catch {
    // cancelled
  }
}
</script>

<style scoped>
.admin-page { max-width: 1200px; margin: 0 auto; padding: 24px; }
.admin-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
.admin-header h2 { margin: 0; font-size: 24px; }
</style>
