<template>
  <div class="editor-page">
    <h2>{{ isEdit ? "编辑文章" : "新建文章" }}</h2>
    <el-form :model="form" label-width="100px" class="editor-form">
      <el-form-item label="标题" required>
        <el-input v-model="form.title" placeholder="请输入文章标题" />
      </el-form-item>
      <el-form-item label="摘要">
        <el-input v-model="form.summary" type="textarea" :rows="2" placeholder="简要描述" />
      </el-form-item>
      <el-form-item label="封面图">
        <el-input v-model="form.coverImage" placeholder="图片URL" />
        <img v-if="form.coverImage" :src="form.coverImage" class="cover-preview" />
      </el-form-item>
      <el-form-item label="攻略内容" required>
        <el-input v-model="form.content" type="textarea" :rows="15" placeholder="支持 Markdown 格式" />
      </el-form-item>
      <el-row :gutter="16">
        <el-col :span="8">
          <el-form-item label="分类">
            <el-select v-model="form.categoryId" placeholder="选择分类" clearable style="width:100%">
              <el-option v-for="c in categories" :key="c.id" :label="c.categoryName" :value="c.id" />
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :span="8">
          <el-form-item label="平台">
            <el-input v-model="form.platform" placeholder="PC/PS5/Xbox" />
          </el-form-item>
        </el-col>
        <el-col :span="8">
          <el-form-item label="评分">
            <el-input-number v-model="form.rating" :min="0" :max="10" :step="0.1" style="width:100%" />
          </el-form-item>
        </el-col>
      </el-row>
      <el-row :gutter="16">
        <el-col :span="12">
          <el-form-item label="开发商">
            <el-input v-model="form.developer" />
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="发行商">
            <el-input v-model="form.publisher" />
          </el-form-item>
        </el-col>
      </el-row>
      <el-form-item label="标签">
        <el-checkbox-group v-model="form.tagIds">
          <el-checkbox v-for="t in tags" :key="t.id" :label="t.id" :value="t.id">{{ t.tagName }}</el-checkbox>
        </el-checkbox-group>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="save" :loading="saving">保存</el-button>
        <el-button @click="$router.back()">取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted, computed } from "vue"
import { useRoute, useRouter } from "vue-router"
import { gameApi } from "@/api"
import { ElMessage } from "element-plus"
import type { GameCategory, TagInfo } from "@/types"

const route = useRoute()
const router = useRouter()
const isEdit = computed(() => !!route.params.id)
const saving = ref(false)
const categories = ref<GameCategory[]>([])
const tags = ref<TagInfo[]>([])

const form = reactive({
  title: "", summary: "", content: "", coverImage: "",
  categoryId: null as number | null,
  platform: "", developer: "", publisher: "",
  rating: 5, tagIds: [] as number[],
})

onMounted(async () => {
  try {
    const [catRes, tagRes] = await Promise.all([
      gameApi.getCategories(),
      gameApi.getTags(),
    ])
    categories.value = catRes.data || []
    tags.value = tagRes.data || []
  } catch {}
  if (route.params.id) {
    try {
      const res = await gameApi.getGameDetail(Number(route.params.id))
      const g = res.data
      Object.assign(form, {
        title: g.title, summary: g.summary, content: g.content, coverImage: g.coverImage,
        categoryId: g.categoryId, platform: g.platform, developer: g.developer,
        publisher: g.publisher, rating: g.rating, tagIds: (g.tags || []).map((t: any) => t.id),
      })
    } catch { ElMessage.error("加载文章失败") }
  }
})

async function save() {
  if (!form.title.trim()) { ElMessage.warning("请输入标题"); return }
  saving.value = true
  try {
    if (isEdit.value) {
      await gameApi.updateGame(Number(route.params.id), { ...form })
      ElMessage.success("已更新")
    } else {
      await gameApi.createGame({ ...form })
      ElMessage.success("已创建")
    }
    router.push("/admin/articles")
  } catch (e: any) {
    ElMessage.error(e.message || "保存失败")
  } finally { saving.value = false }
}
</script>

<style scoped>
.editor-page { max-width: 900px; margin: 0 auto; padding: 24px; }
.editor-page h2 { margin-bottom: 24px; }
.editor-form { max-width: 100%; }
.cover-preview { display: block; max-width: 200px; margin-top: 8px; border-radius: 8px; }
</style>