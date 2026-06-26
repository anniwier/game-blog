export interface UserInfo {
  id: number
  username: string
  nickname: string
  avatar: string
  email: string
  status: number
  createdAt: string
  updatedAt: string
}

export interface LoginVO {
  userId: number
  nickname: string
  avatar: string
  token: string
}

export interface GameItem {
  id: number
  title: string
  slug: string
  summary: string
  coverImage: string
  content?: string
  categoryId: number
  categoryName: string
  authorId: number
  authorName: string
  platform: string
  rating: number
  developer: string
  publisher: string
  releaseDate: string
  viewCount: number
  likeCount: number
  favoriteCount: number
  publishedAt: string
  createdAt: string
  tags: TagInfo[]
}

export interface TagInfo {
  id: number
  tagName: string
  tagCode: string
  color: string
}

export interface CommentInfo {
  id: number
  gameId: number
  userId: number
  username: string
  avatar: string
  content: string
  createdAt: string
}

export interface GameCategory {
  id: number
  categoryName: string
  categoryCode: string
  description: string
  sortOrder: number
}

export interface Favorite {
  id: number
  userId: number
  gameId: number
  createdAt: string
}

export interface ApiResult<T = any> {
  code: number
  message: string
  data: T
}