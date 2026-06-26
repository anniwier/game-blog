package com.game.blog.domain.vo;

import lombok.Data;

@Data
public class LoginVO {

    private String token;
    private Long userId;
    private String nickname;
    private String avatar;
}
