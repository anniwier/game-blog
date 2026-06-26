package com.game.blog.service;

import com.baomidou.mybatisplus.extension.service.IService;
import com.game.blog.domain.dto.GameCreateRequest;
import com.game.blog.domain.entity.Game;
import com.game.blog.domain.vo.GameItemVO;

import java.util.List;

public interface IGameService extends IService<Game> {

    List<GameItemVO> getGameList();

    List<GameItemVO> getTopGames();

    List<GameItemVO> getGameListByTag(Long tagId);

    GameItemVO getGameDetail(Long id);

    List<GameItemVO> getGameListByCategory(Long categoryId);

    List<GameItemVO> searchGames(String keyword);

    GameItemVO createGame(GameCreateRequest request, Long authorId);

    GameItemVO updateGame(Long id, GameCreateRequest request);

    void deleteGame(Long id);
}