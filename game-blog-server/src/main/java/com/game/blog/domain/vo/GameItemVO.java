package com.game.blog.domain.vo;

import lombok.Data;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;

@Data
public class GameItemVO {

    private Long id;

    private String title;

    private String slug;

    private String summary;

    private String coverImage;

    private String content;

    private Long categoryId;

    private String categoryName;

    private Long authorId;

    private String authorName;

    private String platform;

    private BigDecimal rating;

    private String developer;

    private String publisher;

    private LocalDate releaseDate;

    private Long viewCount;

    private Long likeCount;

    private Long favoriteCount;

    private List<TagVO> tags;

    private LocalDateTime publishedAt;

    private LocalDateTime createdAt;
}
