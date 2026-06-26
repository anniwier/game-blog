package com.game.blog.service;

import com.baomidou.mybatisplus.extension.service.IService;
import com.game.blog.domain.entity.Comment;
import com.game.blog.domain.vo.CommentVO;

import java.util.List;

public interface ICommentService extends IService<Comment> {

    List<CommentVO> getGameComments(Long gameId);

    void addComment(Comment comment);

    void deleteComment(Long commentId, Long userId);
}
