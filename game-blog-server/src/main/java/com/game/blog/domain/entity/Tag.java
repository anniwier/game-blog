package com.game.blog.domain.entity;

import com.baomidou.mybatisplus.annotation.*;
import lombok.Data;

import java.time.LocalDateTime;

@Data
@TableName("tags")
public class Tag {

    @TableId(type = IdType.AUTO)
    private Long id;

    private String tagName;

    private String tagCode;

    private String color;

    @TableField(fill = FieldFill.INSERT)
    private LocalDateTime createdAt;
}