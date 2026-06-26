package com.game.blog.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.game.blog.domain.dto.GameCreateRequest;
import com.game.blog.domain.entity.Game;
import com.game.blog.domain.entity.GameTag;
import com.game.blog.domain.vo.GameItemVO;
import com.game.blog.mapper.GameMapper;
import com.game.blog.mapper.GameTagMapper;
import com.game.blog.service.IGameService;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import jakarta.annotation.Resource;
import java.time.LocalDateTime;
import java.util.List;

@Service
public class GameServiceImpl extends ServiceImpl<GameMapper, Game> implements IGameService {

    @Resource
    private GameMapper gameMapper;

    @Resource
    private GameTagMapper gameTagMapper;

    @Override
    public List<GameItemVO> getGameList() {
        return gameMapper.selectGameItemList();
    }

    @Override
    public List<GameItemVO> getTopGames() {
        return gameMapper.selectTopGameItemList();
    }

    @Override
    public List<GameItemVO> getGameListByTag(Long tagId) {
        return gameMapper.selectGameItemListByTag(tagId);
    }

    @Override
    public GameItemVO getGameDetail(Long id) {
        return gameMapper.selectGameItemById(id);
    }

    @Override
    public List<GameItemVO> getGameListByCategory(Long categoryId) {
        return gameMapper.selectGameItemListByCategory(categoryId);
    }

    @Override
    public List<GameItemVO> searchGames(String keyword) {
        return gameMapper.searchGameItemList(keyword);
    }

    @Override
    @Transactional
    public GameItemVO createGame(GameCreateRequest request, Long authorId) {
        Game game = new Game();
        game.setTitle(request.getTitle());
        game.setSlug(request.getTitle().toLowerCase().replaceAll("[^a-z0-9]+", "-").replaceAll("^-|-$", ""));
        game.setSummary(request.getSummary());
        game.setContent(request.getContent());
        game.setCoverImage(request.getCoverImage());
        game.setCategoryId(request.getCategoryId());
        game.setAuthorId(authorId);
        game.setPlatform(request.getPlatform());
        game.setRating(request.getRating());
        game.setDeveloper(request.getDeveloper());
        game.setPublisher(request.getPublisher());
        game.setReleaseDate(request.getReleaseDate());
        game.setStatus(1);
        game.setPublishedAt(LocalDateTime.now());
        save(game);

        Long gameId = game.getId();
        if (request.getTagIds() != null) {
            for (Long tagId : request.getTagIds()) {
                GameTag gt = new GameTag();
                gt.setGameId(gameId);
                gt.setTagId(tagId);
                gameTagMapper.insert(gt);
            }
        }

        return gameMapper.selectGameItemById(gameId);
    }

    @Override
    @Transactional
    public GameItemVO updateGame(Long id, GameCreateRequest request) {
        Game game = getById(id);
        if (game == null) throw new RuntimeException("游戏不存在");

        game.setTitle(request.getTitle());
        game.setSummary(request.getSummary());
        game.setContent(request.getContent());
        game.setCoverImage(request.getCoverImage());
        game.setCategoryId(request.getCategoryId());
        game.setPlatform(request.getPlatform());
        game.setRating(request.getRating());
        game.setDeveloper(request.getDeveloper());
        game.setPublisher(request.getPublisher());
        game.setReleaseDate(request.getReleaseDate());
        updateById(game);

        gameTagMapper.delete(new LambdaQueryWrapper<GameTag>()
            .eq(GameTag::getGameId, id));
        if (request.getTagIds() != null) {
            for (Long tagId : request.getTagIds()) {
                GameTag gt = new GameTag();
                gt.setGameId(id);
                gt.setTagId(tagId);
                gameTagMapper.insert(gt);
            }
        }

        return gameMapper.selectGameItemById(id);
    }

    @Override
    @Transactional
    public void deleteGame(Long id) {
        gameTagMapper.delete(new LambdaQueryWrapper<GameTag>()
            .eq(GameTag::getGameId, id));
        gameMapper.deleteById(id);
    }
}