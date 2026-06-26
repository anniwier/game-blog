import axios from 'axios'
import type { ApiResult, LoginVO, GameItem, CommentInfo } from '@/types'

const request = axios.create({
  baseURL: '/api',
  timeout: 10000
})

request.interceptors.request.use(config => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.token = token
  }
  return config
})

request.interceptors.response.use(
  response => {
    const res = response.data as ApiResult
    if (res.code !== 200) {
      // Token invalid -> redirect to login
      if (res.message && res.message.includes('token')) {
        localStorage.removeItem('token')
        window.location.href = '/login'
        return Promise.reject(new Error('登录已过期，请重新登录'))
      }
      return Promise.reject(new Error(res.message || '请求失败'))
    }
    return response.data
  },
  error => {
    return Promise.reject(error)
  }
)

export const authApi = {
  login(data: { username: string; password: string }) {
    return request.post<any, ApiResult<LoginVO>>('/auth/login', data)
  },
  register(data: { username: string; password: string }) {
    return request.post<any, ApiResult>('/auth/register', data)
  },
  logout() {
    return request.post<any, ApiResult>('/auth/logout')
  }
}

export const userApi = {
  getUserInfo() {
    return request.get<any, ApiResult>('/user/info')
  }
}

export const gameApi = {
  getGameListByTag(tagId: number) {
    return request.get<any, ApiResult<GameItem[]>>(`/games/tag/${tagId}`)
  },
  getTopGames() {
    return request.get<any, ApiResult<GameItem[]>>('/games/top')
  },
  createGame(data: any) {
    return request.post<any, ApiResult<GameItem>>('/games', data)
  },
  updateGame(id: number, data: any) {
    return request.put<any, ApiResult<GameItem>>(`/games/${id}`, data)
  },
  deleteGame(id: number) {
    return request.delete<any, ApiResult>(`/games/${id}`)
  },
  getTags() {
    return request.get<any, ApiResult<TagInfo[]>>('/games/tags')
  },
  getGameList(params?: { categoryId?: number; keyword?: string }) {
    return request.get<any, ApiResult<GameItem[]>>('/games/list', { params })
  },
  getGameDetail(id: number) {
    return request.get<any, ApiResult<GameItem>>(`/games/${id}`)
  },
  getCategories() {
    return request.get<any, ApiResult<GameCategory[]>>('/games/categories')
  }
}

export const commentApi = {
  getGameComments(gameId: number) {
    return request.get<any, ApiResult<CommentInfo[]>>(`/comments/game/${gameId}`)
  },
  addComment(data: { gameId: number; content: string }) {
    return request.post<any, ApiResult>('/comments', data)
  },
  deleteComment(commentId: number) {
    return request.delete<any, ApiResult>(`/comments/${commentId}`)
  }
}

export const favoriteApi = {
  getUserFavorites() {
    return request.get<any, ApiResult<Favorite[]>>('/favorites')
  },
  addFavorite(gameId: number) {
    return request.post<any, ApiResult>('/favorites', { gameId })
  },
  removeFavorite(gameId: number) {
    return request.delete<any, ApiResult>(`/favorites/${gameId}`)
  },
  checkFavorite(gameId: number) {
    return request.get<any, ApiResult<boolean>>(`/favorites/check/${gameId}`)
  }
}

export default request