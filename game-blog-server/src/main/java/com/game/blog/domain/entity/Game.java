package com.game.blog.domain.entity;

import com.baomidou.mybatisplus.annotation.*;
import lombok.Data;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;

@Data
@TableName("games")
public class Game {

    @TableId(type = IdType.AUTO)
    private Long id;

    private String title;

    private String slug;

    private String summary;

    private String content;

    private String coverImage;

    private Long categoryId;

    private Long authorId;

    private String platform;

    private BigDecimal rating;

    private String developer;

    private String publisher;

    private LocalDate releaseDate;

    private Long viewCount;

    private Long likeCount;

    private Long favoriteCount;

    private Integer status;

    @TableLogic
    private Integer isDeleted;

    private LocalDateTime publishedAt;

    @TableField(fill = FieldFill.INSERT)
    private LocalDateTime createdAt;

    @TableField(fill = FieldFill.INSERT_UPDATE)
    private LocalDateTime updatedAt;
}