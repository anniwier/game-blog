<template>
  <div class="app-layout">
    <el-menu
      :default-active="route.path"
      mode="horizontal"
      class="nav-menu"
      router
    >
      <el-menu-item index="/">
        <el-icon><HomeFilled /></el-icon>
        <span>首页</span>
      </el-menu-item>
      <el-menu-item index="/ranking">
        <el-icon><TrendCharts /></el-icon>
        <span>排行榜</span>
      </el-menu-item>
      <el-menu-item index="/categories">
        <el-icon><Collection /></el-icon>
        <span>分类</span>
      </el-menu-item>

      <div class="nav-spacer"></div>

      <template v-if="userStore.isLoggedIn()">
        <el-menu-item index="/admin/articles">
          <el-icon><Edit /></el-icon>
          <span>文章管理</span>
        </el-menu-item>
      </template>

      <template v-if="userStore.isLoggedIn()">
        <el-menu-item index="/profile">
          <el-icon><UserFilled /></el-icon>
          <span>{{ userStore.userInfo?.nickname || '个人中心' }}</span>
        </el-menu-item>
        <el-menu-item index="logout" @click="handleLogout">
          <el-icon><SwitchButton /></el-icon>
          <span>退出登录</span>
        </el-menu-item>
      </template>
      <template v-else>
        <el-menu-item index="/login">
          <el-icon><UserFilled /></el-icon>
          <span>登录</span>
        </el-menu-item>
        <el-menu-item index="/register">
          <el-icon><UserFilled /></el-icon>
          <span>注册</span>
        </el-menu-item>
      </template>
    </el-menu>

    <div class="main-content">
      <router-view v-slot="{ Component }">
        <transition name="page-fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { HomeFilled, UserFilled, SwitchButton, Edit, TrendCharts, Collection } from '@element-plus/icons-vue'

const route = useRoute()
const userStore = useUserStore()

function handleLogout() {
  userStore.logout()
  window.location.href = '/'
}
</script>

<style scoped>
.app-layout {
  min-height: 100vh;
  background: transparent;
}

.nav-menu {
  display: flex;
  align-items: center;
  padding: 0 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.nav-spacer {
  margin-left: auto;
}

.main-content {
  min-height: calc(100vh - 60px);
}
</style>
