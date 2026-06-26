package com.game.blog.domain.dto;

import lombok.Data;
import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.List;

@Data
public class GameCreateRequest {
    private String title;
    private String summary;
    private String content;
    private String coverImage;
    private Long categoryId;
    private String platform;
    private BigDecimal rating;
    private String developer;
    private String publisher;
    private LocalDate releaseDate;
    private List<Long> tagIds;
}
