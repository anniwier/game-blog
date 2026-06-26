package com.game.blog.controller;

import cn.dev33.satoken.stp.StpUtil;
import com.game.blog.common.response.Result;
import com.game.blog.domain.entity.Comment;
import com.game.blog.domain.vo.CommentVO;
import com.game.blog.service.ICommentService;
import org.springframework.web.bind.annotation.*;

import jakarta.annotation.Resource;
import java.util.List;

@RestController
@RequestMapping("/api/comments")
public class CommentController {

    @Resource
    private ICommentService commentService;

    @GetMapping("/game/{gameId}")
    public Result<List<CommentVO>> getGameComments(@PathVariable Long gameId) {
        List<CommentVO> comments = commentService.getGameComments(gameId);
        return Result.success(comments);
    }

    @PostMapping
    public Result<Void> addComment(@RequestBody Comment comment) {
        long userId = StpUtil.getLoginIdAsLong();
        comment.setUserId(userId);
        commentService.addComment(comment);
        return Result.success();
    }

    @DeleteMapping("/{commentId}")
    public Result<Void> deleteComment(@PathVariable Long commentId) {
        long userId = StpUtil.getLoginIdAsLong();
        commentService.deleteComment(commentId, userId);
        return Result.success();
    }
}
