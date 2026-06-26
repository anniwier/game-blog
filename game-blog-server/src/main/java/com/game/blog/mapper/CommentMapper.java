package com.game.blog.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.game.blog.domain.entity.Comment;
import com.game.blog.domain.vo.CommentVO;

import java.util.List;

public interface CommentMapper extends BaseMapper<Comment> {

    List<CommentVO> selectGameComments(Long gameId);
}
