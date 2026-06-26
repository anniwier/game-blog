package com.game.blog.controller;

import com.game.blog.common.response.Result;
import com.game.blog.domain.entity.Favorite;
import com.game.blog.service.IFavoriteService;
import org.springframework.web.bind.annotation.*;

import jakarta.annotation.Resource;
import cn.dev33.satoken.stp.StpUtil;
import java.util.List;

@RestController
@RequestMapping("/api/favorites")
public class FavoriteController {

    @Resource
    private IFavoriteService favoriteService;

    @GetMapping
    public Result<List<Favorite>> getUserFavorites() {
        long userId = StpUtil.getLoginIdAsLong();
        List<Favorite> favorites = favoriteService.getUserFavorites(userId);
        return Result.success(favorites);
    }

    @PostMapping
    public Result<Void> addFavorite(@RequestBody AddFavoriteRequest request) {
        long userId = StpUtil.getLoginIdAsLong();
        favoriteService.addFavorite(userId, request.getGameId());
        return Result.success();
    }

    @DeleteMapping("/{gameId}")
    public Result<Void> removeFavorite(@PathVariable Long gameId) {
        long userId = StpUtil.getLoginIdAsLong();
        favoriteService.removeFavorite(userId, gameId);
        return Result.success();
    }

    @GetMapping("/check/{gameId}")
    public Result<Boolean> checkFavorite(@PathVariable Long gameId) {
        Object loginId = StpUtil.getLoginIdDefaultNull();
        if (loginId == null) return Result.success(false);
        long userId = Long.parseLong(loginId.toString());
        boolean favorited = favoriteService.isFavorited(userId, gameId);
        return Result.success(favorited);
    }

    public static class AddFavoriteRequest {
        private Long gameId;

        public Long getGameId() { return gameId; }
        public void setGameId(Long gameId) { this.gameId = gameId; }
    }
}
