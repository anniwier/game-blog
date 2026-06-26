import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/user'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'
import GameDetailView from '@/views/GameDetailView.vue'
import UserProfileView from '@/views/UserProfileView.vue'
import AdminArticlesView from '@/views/admin/AdminArticlesView.vue'
import RankingView from '@/views/RankingView.vue'
import CategoriesView from '@/views/CategoriesView.vue'
import TagGamesView from '@/views/TagGamesView.vue'
import ArticleEditorView from '@/views/admin/ArticleEditorView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: { title: '游戏博客' }
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      meta: { title: '登录' }
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView,
      meta: { title: '注册' }
    },
    {
      path: '/games/:id',
      name: 'gameDetail',
      component: GameDetailView,
      meta: { title: '游戏详情' }
    },
    {
      path: '/profile',
      name: 'profile',
      component: UserProfileView,
      meta: { title: '个人中心', requiresAuth: true }
    },
    {
      path: '/admin/articles',
      name: 'adminArticles',
      component: AdminArticlesView,
      meta: { title: '文章管理', requiresAuth: true }
    },
    {
      path: '/admin/articles/new',
      name: 'newArticle',
      component: ArticleEditorView,
      meta: { title: '新建文章', requiresAuth: true }
    },
    {
      path: '/admin/articles/edit/:id',
      name: 'editArticle',
      component: ArticleEditorView,
      meta: { title: '编辑文章', requiresAuth: true }
    },
    {
      path: '/tags/:tagId',
      name: 'tagGames',
      component: TagGamesView,
      meta: { title: '标签筛选' }
    },
    {
      path: '/ranking',
      name: 'ranking',
      component: RankingView,
      meta: { title: '排行榜' }
    },
    {
      path: '/categories',
      name: 'categories',
      component: CategoriesView,
      meta: { title: '分类浏览' }
    }
  ]
})

router.beforeEach((to, _from, next) => {
  document.title = to.meta.title as string || '游戏博客'
  if (to.meta.requiresAuth) {
    const userStore = useUserStore()
    if (!userStore.isLoggedIn()) {
      next({ name: 'login', query: { redirect: to.fullPath } })
      return
    }
  }
  next()
})

export default router
