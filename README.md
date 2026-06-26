# GameBlog - 游戏攻略博客系统

一个基于 Spring Boot + Vue 3 的全栈游戏攻略分享平台，支持游戏浏览、攻略查看、评论互动、收藏管理等功能。

## 技术栈

### 后端
- **Java 17** + **Spring Boot 3.2.1**
- **MyBatis-Plus** — ORM 框架
- **MySQL 8.0** — 数据库
- **Sa-Token** — 登录认证
- **Druid** — 数据库连接池
- **Maven** — 构建工具

### 前端
- **Vue 3** + **TypeScript**
- **Vite** — 构建工具
- **Pinia** — 状态管理
- **Vue Router** — 路由
- **Element Plus** — UI 组件库
- **Axios** — HTTP 请求
- **Marked** — Markdown 渲染

## 项目结构

```
game-blog-server/          # 后端项目
├── src/main/java/com/game/blog/
│   ├── common/            # 通用工具类
│   │   ├── exception/     # 全局异常处理
│   │   ├── request/       # 分页查询
│   │   └── response/      # 统一响应格式
│   ├── config/            # 配置类 (MyBatis, Sa-Token, Security)
│   ├── controller/        # 控制器层
│   ├── domain/
│   │   ├── dto/           # 数据传输对象
│   │   ├── entity/        # 实体类
│   │   └── vo/            # 视图对象
│   ├── mapper/            # 数据访问层
│   └── service/           # 业务逻辑层
├── src/main/resources/
│   ├── mapper/            # MyBatis XML 映射
│   ├── static/covers/     # 游戏封面图
│   ├── schema.sql         # 数据库建表脚本
│   └── data.sql           # 初始化数据
└── pom.xml

game-blog-web/             # 前端项目
├── src/
│   ├── api/               # API 请求封装
│   ├── assets/            # 静态资源
│   ├── components/        # 公共组件
│   ├── router/            # 路由配置
│   ├── stores/            # Pinia 状态管理
│   ├── types/             # TypeScript 类型定义
│   └── views/             # 页面组件
│       └── admin/         # 后台管理页面
├── index.html
├── vite.config.ts
└── package.json
```

## 功能特性

### 首页
- 轮播图展示热门游戏
- 游戏列表 + 分页
- 分类筛选
- 关键词搜索

### 游戏详情
- 游戏信息展示（评分/平台/开发商等）
- 攻略内容（支持 Markdown 渲染）
- 评论系统（发表/删除）
- 收藏功能
- 相关游戏推荐

### 用户系统
- 注册 / 登录
- 个人中心
- 收藏列表

### 排行榜
- 按热度排行（浏览量）

### 分类浏览
- 按分类查看游戏

### 后台管理
- 文章管理（新建/编辑/删除）
- 标签关联

## 快速启动

### 前置要求
- **JDK 17+**
- **Maven 3.6+**
- **MySQL 8.0+**
- **Node.js 18+**

### 1. 配置数据库

修改 `game-blog-server/src/main/resources/application.yml` 中的数据库连接信息：

```yaml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/game_blog
    username: root
    password: your_password
```

### 2. 启动后端

```bash
cd game-blog-server
mvn spring-boot:run
```

后端将在 `http://localhost:8080` 启动，自动创建数据库表并导入初始数据。

### 3. 启动前端

```bash
cd game-blog-web
npm install
npm run dev
```

前端将在 `http://localhost:3001` 启动。

### 4. 访问

打开浏览器访问 `http://localhost:3001`

### 一键启动

项目根目录提供了 `start.bat` 脚本，可一键启动前后端：

```bash
start.bat
```

## 测试账号

| 角色 | 用户名 | 密码 |
|------|--------|------|
| 管理员 | admin | admin123 |
| 普通用户 | gamer | gamer123 |

## 预置数据

系统初始化时自动导入：
- **14 款游戏** — 涵盖各类热门游戏攻略
- **7 个分类** — 角色扮演、动作冒险、射击、策略等
- **13 个标签** — 开放世界、单人剧情、高难度等
- **42 条评论** — 每款游戏 3 条趣味评论
- **7 个标签分类**
- **2 个测试账号**

## API 接口

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/games/list | 游戏列表（支持分类/搜索） |
| GET | /api/games/top | 热门游戏排行 |
| GET | /api/games/{id} | 游戏详情 |
| GET | /api/games/tags | 标签列表 |
| GET | /api/games/tag/{tagId} | 按标签筛选游戏 |
| GET | /api/games/categories | 分类列表 |
| POST | /api/games | 新建游戏（需登录） |
| PUT | /api/games/{id} | 编辑游戏（需登录） |
| DELETE | /api/games/{id} | 删除游戏（需登录） |
| POST | /api/auth/login | 登录 |
| POST | /api/auth/register | 注册 |
| POST | /api/auth/logout | 退出 |
| GET | /api/user/info | 用户信息 |
| GET | /api/comments/game/{gameId} | 获取评论 |
| POST | /api/comments | 发表评论（需登录） |
| DELETE | /api/comments/{id} | 删除评论（需登录） |
| GET | /api/favorites | 收藏列表（需登录） |
| POST | /api/favorites | 添加收藏（需登录） |
| DELETE | /api/favorites/{gameId} | 取消收藏（需登录） |
| GET | /api/favorites/check/{gameId} | 检查是否已收藏 |

## License

MIT
