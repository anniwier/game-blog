package com.game.blog.service;

import com.baomidou.mybatisplus.extension.service.IService;
import com.game.blog.domain.entity.Favorite;

import java.util.List;

public interface IFavoriteService extends IService<Favorite> {

    void addFavorite(Long userId, Long gameId);

    void removeFavorite(Long userId, Long gameId);

    boolean isFavorited(Long userId, Long gameId);

    List<Favorite> getUserFavorites(Long userId);
}