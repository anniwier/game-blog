import { defineStore } from 'pinia'
import { ref } from 'vue'
import { authApi, userApi } from '@/api'
import type { LoginVO, UserInfo } from '@/types'

export const useUserStore = defineStore('user', () => {
  const token = ref(localStorage.getItem('token') || '')
  const userInfo = ref<UserInfo | null>(null)

  async function login(username: string, password: string) {
    const res = await authApi.login({ username, password })
    const data = res.data as LoginVO
    token.value = data.token
    localStorage.setItem('token', data.token)
    userInfo.value = {
      id: data.userId,
      username: '',
      nickname: data.nickname,
      avatar: data.avatar,
      email: '',
      status: 1,
      createdAt: '',
      updatedAt: ''
    }
    return data
  }

  async function register(username: string, password: string) {
    await authApi.register({ username, password })
  }

  async function getUserInfo() {
    const res = await userApi.getUserInfo()
    userInfo.value = res.data as UserInfo
    return res.data
  }

  function logout() {
    token.value = ''
    userInfo.value = null
    localStorage.removeItem('token')
    authApi.logout()
  }

  function isLoggedIn() {
    return !!token.value
  }

  return {
    token,
    userInfo,
    login,
    register,
    getUserInfo,
    logout,
    isLoggedIn
  }
})