-- ============================================
-- 游戏攻略博客系统 - 数据库建表脚本
-- ============================================

-- 用户表
CREATE TABLE `users` (
    `id`              BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY COMMENT '主键ID',
    `username`        VARCHAR(64)  NOT NULL COMMENT '登录用户名',
    `password_hash`   VARCHAR(128) NOT NULL COMMENT '密码密文',
    `nickname`        VARCHAR(64)  DEFAULT NULL COMMENT '昵称',
    `avatar`          VARCHAR(512) DEFAULT NULL COMMENT '头像URL',
    `email`           VARCHAR(128) DEFAULT NULL COMMENT '邮箱',
    `phone`           VARCHAR(32)  DEFAULT NULL COMMENT '手机号',
    `status`          TINYINT      NOT NULL DEFAULT 1 COMMENT '状态: 0-禁用 1-启用',
    `is_deleted`      TINYINT      NOT NULL DEFAULT 0 COMMENT '逻辑删除: 0-未删除 1-已删除',
    `created_at`      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `updated_at`      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    UNIQUE KEY `uk_username` (`username`),
    UNIQUE KEY `uk_email`    (`email`),
    KEY              `idx_phone`          (`phone`),
    KEY              `idx_status`         (`status`),
    KEY              `idx_is_deleted`     (`is_deleted`),
    KEY              `idx_deleted_status` (`is_deleted`, `status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户表';

-- 角色表
CREATE TABLE `roles` (
    `id`          BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY COMMENT '主键ID',
    `role_code`   VARCHAR(64)   NOT NULL COMMENT '角色编码',
    `role_name`   VARCHAR(128)  NOT NULL COMMENT '角色名称',
    `description` VARCHAR(256)  DEFAULT NULL COMMENT '角色描述',
    `status`      TINYINT       NOT NULL DEFAULT 1 COMMENT '状态: 0-禁用 1-启用',
    `created_at`  DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `updated_at`  DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    UNIQUE KEY `uk_role_code` (`role_code`),
    KEY          `idx_status`  (`status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='角色表';

-- 用户角色关联表
CREATE TABLE `user_roles` (
    `id`         BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY COMMENT '主键ID',
    `user_id`    BIGINT UNSIGNED NOT NULL COMMENT '用户ID',
    `role_id`    BIGINT UNSIGNED NOT NULL COMMENT '角色ID',
    `created_at` DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    UNIQUE KEY `uk_user_role` (`user_id`, `role_id`),
    KEY          `idx_role_id` (`role_id`),
    CONSTRAINT `fk_user_roles_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_user_roles_role_id` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户角色关联表';

-- 初始化角色数据
INSERT INTO `roles` (`role_code`, `role_name`, `description`, `status`)
VALUES ('USER', '普通用户', '默认普通用户角色', 1),
       ('ADMIN', '管理员', '系统管理员角色', 1);

-- ============================================
-- 游戏分类表
-- ============================================
CREATE TABLE `game_categories` (
    `id`            BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY COMMENT '主键ID',
    `category_name` VARCHAR(128)  NOT NULL COMMENT '分类名称',
    `category_code` VARCHAR(128)  NOT NULL COMMENT '分类编码/URL别名',
    `parent_id`     BIGINT UNSIGNED DEFAULT NULL COMMENT '父分类ID，NULL为顶级分类',
    `description`   VARCHAR(256)  DEFAULT NULL COMMENT '分类描述',
    `icon`          VARCHAR(512)  DEFAULT NULL COMMENT '分类图标',
    `sort_order`    INT           NOT NULL DEFAULT 0 COMMENT '排序权重',
    `status`        TINYINT       NOT NULL DEFAULT 1 COMMENT '状态: 0-禁用 1-启用',
    `created_at`    DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `updated_at`    DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    UNIQUE KEY `uk_category_code` (`category_code`),
    KEY          `idx_parent_id`  (`parent_id`),
    KEY          `idx_status`     (`status`),
    CONSTRAINT `fk_category_parent_id` FOREIGN KEY (`parent_id`) REFERENCES `game_categories` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='游戏分类表';

-- ============================================
-- 游戏标签表
-- ============================================
CREATE TABLE `tags` (
    `id`         BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY COMMENT '主键ID',
    `tag_name`   VARCHAR(64)  NOT NULL COMMENT '标签名称',
    `tag_code`   VARCHAR(64)  NOT NULL COMMENT '标签编码',
    `color`      VARCHAR(32)  DEFAULT NULL COMMENT '标签颜色',
    `created_at` DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    UNIQUE KEY `uk_tag_code` (`tag_code`),
    UNIQUE KEY `uk_tag_name` (`tag_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='游戏标签表';

-- ============================================
-- 游戏表
-- ============================================
CREATE TABLE `games` (
    `id`            BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY COMMENT '主键ID',
    `title`         VARCHAR(256)    NOT NULL COMMENT '游戏名称',
    `slug`          VARCHAR(256)    NOT NULL COMMENT 'URL别名',
    `summary`       VARCHAR(512)    DEFAULT NULL COMMENT '简介摘要',
    `content`       LONGTEXT        NOT NULL COMMENT '攻略内容',
    `cover_image`   VARCHAR(512)    DEFAULT NULL COMMENT '封面图URL',
    `category_id`   BIGINT UNSIGNED NOT NULL COMMENT '分类ID',
    `author_id`     BIGINT UNSIGNED NOT NULL COMMENT '作者ID',
    `platform`      VARCHAR(128)    DEFAULT NULL COMMENT '平台: PC/PS5/Xbox/Switch/Mobile',
    `rating`        DECIMAL(3,1)    DEFAULT NULL COMMENT '评分 0-10',
    `developer`     VARCHAR(256)    DEFAULT NULL COMMENT '开发商',
    `publisher`     VARCHAR(256)    DEFAULT NULL COMMENT '发行商',
    `release_date`  DATE            DEFAULT NULL COMMENT '发售日期',
    `view_count`    BIGINT UNSIGNED NOT NULL DEFAULT 0 COMMENT '浏览次数',
    `like_count`    BIGINT UNSIGNED NOT NULL DEFAULT 0 COMMENT '点赞数',
    `favorite_count` BIGINT UNSIGNED NOT NULL DEFAULT 0 COMMENT '收藏数',
    `status`        TINYINT         NOT NULL DEFAULT 0 COMMENT '状态: 0-草稿 1-已发布 2-归档',
    `is_deleted`    TINYINT         NOT NULL DEFAULT 0 COMMENT '逻辑删除: 0-未删除 1-已删除',
    `published_at`  DATETIME        DEFAULT NULL COMMENT '发布时间',
    `created_at`    DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `updated_at`    DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    UNIQUE KEY `uk_slug`            (`slug`),
    KEY             `idx_category_id`  (`category_id`),
    KEY             `idx_author_id`    (`author_id`),
    KEY             `idx_status`       (`status`),
    KEY             `idx_is_deleted`   (`is_deleted`),
    KEY             `idx_deleted_status` (`is_deleted`, `status`),
    KEY             `idx_published_at` (`published_at`),
    KEY             `idx_view_count`   (`view_count`),
    KEY             `idx_rating`       (`rating`),
    CONSTRAINT `fk_games_category_id` FOREIGN KEY (`category_id`) REFERENCES `game_categories` (`id`) ON DELETE RESTRICT,
    CONSTRAINT `fk_games_author_id`   FOREIGN KEY (`author_id`)   REFERENCES `users` (`id`) ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='游戏攻略表';

-- ============================================
-- 游戏-标签关联表
-- ============================================
CREATE TABLE `game_tags` (
    `id`         BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY COMMENT '主键ID',
    `game_id`    BIGINT UNSIGNED NOT NULL COMMENT '游戏ID',
    `tag_id`     BIGINT UNSIGNED NOT NULL COMMENT '标签ID',
    `created_at` DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    UNIQUE KEY `uk_game_tag` (`game_id`, `tag_id`),
    KEY          `idx_tag_id` (`tag_id`),
    CONSTRAINT `fk_game_tags_game_id` FOREIGN KEY (`game_id`) REFERENCES `games` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_game_tags_tag_id`  FOREIGN KEY (`tag_id`)  REFERENCES `tags` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='游戏标签关联表';

-- ============================================
-- 评论表
-- ============================================
CREATE TABLE `comments` (
    `id`         BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY COMMENT '主键ID',
    `game_id`    BIGINT UNSIGNED NOT NULL COMMENT '游戏ID',
    `user_id`    BIGINT UNSIGNED NOT NULL COMMENT '评论用户ID',
    `parent_id`  BIGINT UNSIGNED DEFAULT NULL COMMENT '父评论ID，NULL为顶级评论',
    `content`    TEXT            NOT NULL COMMENT '评论内容',
    `status`     TINYINT         NOT NULL DEFAULT 1 COMMENT '状态: 0-隐藏 1-显示',
    `created_at` DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `updated_at` DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    KEY          `idx_game_id`  (`game_id`),
    KEY          `idx_user_id`  (`user_id`),
    KEY          `idx_parent_id` (`parent_id`),
    CONSTRAINT `fk_comments_game_id` FOREIGN KEY (`game_id`) REFERENCES `games` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_comments_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_comments_parent_id` FOREIGN KEY (`parent_id`) REFERENCES `comments` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='评论表';

-- ============================================
-- 收藏表
-- ============================================
CREATE TABLE `favorites` (
    `id`         BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY COMMENT '主键ID',
    `user_id`    BIGINT UNSIGNED NOT NULL COMMENT '用户ID',
    `game_id`    BIGINT UNSIGNED NOT NULL COMMENT '游戏ID',
    `created_at` DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    UNIQUE KEY `uk_user_game` (`user_id`, `game_id`),
    KEY          `idx_game_id` (`game_id`),
    CONSTRAINT `fk_favorites_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_favorites_game_id` FOREIGN KEY (`game_id`) REFERENCES `games` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='收藏表';

-- ============================================
-- 初始化数据
-- ============================================

-- 测试用户（密码需要替换为BCrypt加密后的值）
INSERT INTO `users` (`id`, `username`, `password_hash`, `nickname`, `avatar`, `email`, `phone`, `status`, `is_deleted`)
VALUES (1, 'admin', '$2a$10$N.zmdr9k7uOCQb376NoUnuTJ8iAt6Z5EHsM8lE9lBOsl7iAt6Z5EH', '游戏管理员', NULL, 'admin@gameblog.com', '13800138000', 1, 0),
       (2, 'gamer', '$2a$10$N.zmdr9k7uOCQb376NoUnuTJ8iAt6Z5EHsM8lE9lBOsl7iAt6Z5EH', '资深玩家', NULL, 'gamer@gameblog.com', NULL, 1, 0);

-- 游戏分类数据
INSERT INTO `game_categories` (`id`, `category_name`, `category_code`, `parent_id`, `description`, `icon`, `sort_order`, `status`)
VALUES (1, '角色扮演', 'rpg',       NULL, '角色扮演游戏（RPG）', '🎮', 1, 1),
       (2, '动作冒险', 'action-adventure', NULL, '动作冒险游戏', '⚔️', 2, 1),
       (3, '射击游戏', 'fps',      NULL, '第一/三人称射击游戏', '🔫', 3, 1),
       (4, '策略游戏', 'strategy', NULL, '策略、模拟经营游戏', '🧠', 4, 1),
       (5, '体育竞速', 'sports',   NULL, '体育、竞速类游戏', '🏎️', 5, 1),
       (6, '开放世界', 'open-world', 1, '开放世界RPG', '🌍', 1, 1),
       (7, '日式RPG', 'jrpg',     1, '日式角色扮演游戏', '🗾', 2, 1);

-- 游戏标签数据
INSERT INTO `tags` (`id`, `tag_name`, `tag_code`, `color`)
VALUES (1, '开放世界', 'open-world', '#e74c3c'),
       (2, '多人联机', 'multiplayer', '#3498db'),
       (3, '单人剧情', 'single-player', '#2ecc71'),
       (4, '高难度', 'hardcore', '#9b59b6'),
       (5, '休闲', 'casual', '#f39c12'),
       (6, '独立游戏', 'indie', '#1abc9c'),
       (7, '3A大作', 'aaa', '#e67e22');

-- 游戏攻略测试数据
INSERT INTO `games` (`id`, `title`, `slug`, `summary`, `content`, `cover_image`, `category_id`, `author_id`, `platform`, `rating`, `developer`, `publisher`, `release_date`, `view_count`, `like_count`, `favorite_count`, `status`, `is_deleted`, `published_at`)
VALUES (1, '艾尔登法环 全成就攻略', 'elden-ring-guide',
        '交界地全BOSS位置、全收集品地图、全结局触发条件详解',
        '# 艾尔登法环 全成就攻略\n\n## 开局推荐\n选择武士或观星者开局...',
        'https://example.com/images/elden-ring.jpg', 6, 1, 'PC/PS5/Xbox', 9.5, 'FromSoftware', 'Bandai Namco', '2022-02-25', 12500, 342, 128, 1, 0, NOW()),
       (2, '塞尔达传说：王国之泪 新手入门', 'totk-beginner-guide',
        '初始空岛全解谜、左纳乌装置合成指南、隐藏宝箱位置',
        '# 塞尔达传说：王国之泪 新手入门\n\n## 初始空岛\n从初始空岛开始，建议先完成所有神庙解谜...',
        'https://example.com/images/totk.jpg', 6, 2, 'Switch', 10.0, 'Nintendo', 'Nintendo', '2023-05-12', 9800, 256, 89, 1, 0, NOW()),
       (3, '只狼 通关技巧与BOSS打法', 'sekiro-boss-guide',
        '全BOSS无伤打法、忍义手获取顺序、全结局流程',
        '# 只狼 通关技巧\n\n## 基础战斗系统\n弹反是核心机制，需要熟练掌握...',
        'https://example.com/images/sekiro.jpg', 2, 1, 'PC/PS5/Xbox', 9.0, 'FromSoftware', 'Activision', '2019-03-22', 7600, 189, 67, 1, 0, NOW()),
       (4, '原神 角色培养优先级指南', 'genshin-impact-guide',
        '各版本T0角色推荐、圣遗物搭配、武器选择全解析',
        '# 原神 角色培养指南\n\n## T0级别角色\n当前版本推荐培养...',
        'https://example.com/images/genshin.jpg', 1, 2, 'PC/Mobile/PS5', 8.5, 'miHoYo', 'miHoYo', '2020-09-28', 15000, 423, 201, 1, 0, NOW());

-- 关联游戏与标签
INSERT INTO `game_tags` (`game_id`, `tag_id`) VALUES
(1, 1), (1, 3), (1, 4), (1, 7),
(2, 1), (2, 3), (2, 5),
(3, 3), (3, 4), (3, 7),
(4, 1), (4, 2), (4, 5);

-- 测试评论数据
INSERT INTO `comments` (`id`, `game_id`, `user_id`, `parent_id`, `content`, `status`, `created_at`)
VALUES (1, 1, 2, NULL, '非常好的攻略，帮助我拿到了白金奖杯！', 1, NOW()),
       (2, 1, 1, 1, '谢谢支持，有问题可以随时问我', 1, NOW()),
       (3, 2, 1, NULL, '王泪确实好玩，建议先去地底探索', 1, NOW());

-- 测试收藏数据
INSERT INTO `favorites` (`user_id`, `game_id`) VALUES (1, 2), (1, 3), (2, 1), (2, 4);