-- ============================================
-- 游戏攻略博客系统 - 自动建表
-- ============================================

-- 用户表
CREATE TABLE IF NOT EXISTS `users` (
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
CREATE TABLE IF NOT EXISTS `roles` (
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
CREATE TABLE IF NOT EXISTS `user_roles` (
    `id`         BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY COMMENT '主键ID',
    `user_id`    BIGINT UNSIGNED NOT NULL COMMENT '用户ID',
    `role_id`    BIGINT UNSIGNED NOT NULL COMMENT '角色ID',
    `created_at` DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    UNIQUE KEY `uk_user_role` (`user_id`, `role_id`),
    KEY          `idx_role_id` (`role_id`),
    CONSTRAINT `fk_user_roles_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_user_roles_role_id` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户角色关联表';

-- 游戏分类表
CREATE TABLE IF NOT EXISTS `game_categories` (
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

-- 游戏标签表
CREATE TABLE IF NOT EXISTS `tags` (
    `id`         BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY COMMENT '主键ID',
    `tag_name`   VARCHAR(64)  NOT NULL COMMENT '标签名称',
    `tag_code`   VARCHAR(64)  NOT NULL COMMENT '标签编码',
    `color`      VARCHAR(32)  DEFAULT NULL COMMENT '标签颜色',
    `created_at` DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    UNIQUE KEY `uk_tag_code` (`tag_code`),
    UNIQUE KEY `uk_tag_name` (`tag_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='游戏标签表';

-- 游戏表
CREATE TABLE IF NOT EXISTS `games` (
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

-- 游戏-标签关联表
CREATE TABLE IF NOT EXISTS `game_tags` (
    `id`         BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY COMMENT '主键ID',
    `game_id`    BIGINT UNSIGNED NOT NULL COMMENT '游戏ID',
    `tag_id`     BIGINT UNSIGNED NOT NULL COMMENT '标签ID',
    `created_at` DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    UNIQUE KEY `uk_game_tag` (`game_id`, `tag_id`),
    KEY          `idx_tag_id` (`tag_id`),
    CONSTRAINT `fk_game_tags_game_id` FOREIGN KEY (`game_id`) REFERENCES `games` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_game_tags_tag_id`  FOREIGN KEY (`tag_id`)  REFERENCES `tags` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='游戏标签关联表';

-- 评论表
CREATE TABLE IF NOT EXISTS `comments` (
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

-- 收藏表
CREATE TABLE IF NOT EXISTS `favorites` (
    `id`         BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY COMMENT '主键ID',
    `user_id`    BIGINT UNSIGNED NOT NULL COMMENT '用户ID',
    `game_id`    BIGINT UNSIGNED NOT NULL COMMENT '游戏ID',
    `created_at` DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    UNIQUE KEY `uk_user_game` (`user_id`, `game_id`),
    KEY          `idx_game_id` (`game_id`),
    CONSTRAINT `fk_favorites_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_favorites_game_id` FOREIGN KEY (`game_id`) REFERENCES `games` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='收藏表';