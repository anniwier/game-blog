package com.game.blog.common.request;

import lombok.Data;

@Data
public class PageQuery {

    private int page = 1;

    private int size = 10;

    public int getOffset() {
        return (page - 1) * size;
    }
}