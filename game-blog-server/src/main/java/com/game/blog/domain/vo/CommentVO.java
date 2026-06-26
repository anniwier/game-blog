package com.game.blog.domain.vo;

import lombok.Data;
import java.time.LocalDateTime;

@Data
public class CommentVO {

    private Long id;
    private Long gameId;
    private Long userId;
    private String username;
    private String avatar;
    private String content;
    private LocalDateTime createdAt;
}
