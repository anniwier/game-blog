package com.game.blog.controller;

import cn.dev33.satoken.stp.StpUtil;
import com.game.blog.common.response.Result;
import com.game.blog.domain.dto.GameCreateRequest;
import com.game.blog.domain.entity.GameCategory;
import com.game.blog.domain.entity.Tag;
import com.game.blog.domain.vo.GameItemVO;
import com.game.blog.service.IGameCategoryService;
import com.game.blog.service.IGameService;
import com.game.blog.mapper.TagMapper;
import org.springframework.web.bind.annotation.*;

import jakarta.annotation.Resource;
import java.util.List;

@RestController
@RequestMapping("/api/games")
public class GameController {

    @Resource
    private IGameService gameService;

    @Resource
    private TagMapper tagMapper;

    @Resource
    private IGameCategoryService gameCategoryService;

    @GetMapping("/list")
    public Result<List<GameItemVO>> getGameList(
            @RequestParam(required = false) Long categoryId,
            @RequestParam(required = false) String keyword) {
        if (categoryId != null) {
            List<GameItemVO> gameList = gameService.getGameListByCategory(categoryId);
            return Result.success(gameList);
        }
        if (keyword != null && !keyword.trim().isEmpty()) {
            List<GameItemVO> gameList = gameService.searchGames(keyword.trim());
            return Result.success(gameList);
        }
        List<GameItemVO> gameList = gameService.getGameList();
        return Result.success(gameList);
    }

    @GetMapping("/top")
    public Result<List<GameItemVO>> getTopGames() {
        List<GameItemVO> gameList = gameService.getTopGames();
        return Result.success(gameList);
    }

    @GetMapping("/tag/{tagId}")
    public Result<List<GameItemVO>> getGameListByTag(@PathVariable Long tagId) {
        List<GameItemVO> gameList = gameService.getGameListByTag(tagId);
        return Result.success(gameList);
    }

    @GetMapping("/tags")
    public Result<List<Tag>> getAllTags() {
        List<Tag> tags = tagMapper.selectList(null);
        return Result.success(tags);
    }

    @GetMapping("/categories")
    public Result<List<GameCategory>> getCategories() {
        List<GameCategory> categories = gameCategoryService.list();
        return Result.success(categories);
    }

    @GetMapping("/{id}")
    public Result<GameItemVO> getGameDetail(@PathVariable Long id) {
        GameItemVO gameDetail = gameService.getGameDetail(id);
        return Result.success(gameDetail);
    }

    @PostMapping
    public Result<GameItemVO> createGame(@RequestBody GameCreateRequest request) {
        StpUtil.checkLogin();
        long userId = StpUtil.getLoginIdAsLong();
        GameItemVO game = gameService.createGame(request, userId);
        return Result.success(game);
    }

    @PutMapping("/{id}")
    public Result<GameItemVO> updateGame(@PathVariable Long id, @RequestBody GameCreateRequest request) {
        StpUtil.checkLogin();
        GameItemVO game = gameService.updateGame(id, request);
        return Result.success(game);
    }

    @DeleteMapping("/{id}")
    public Result<Void> deleteGame(@PathVariable Long id) {
        StpUtil.checkLogin();
        gameService.deleteGame(id);
        return Result.success();
    }
}