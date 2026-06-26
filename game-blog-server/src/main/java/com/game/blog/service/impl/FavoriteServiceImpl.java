package com.game.blog.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.game.blog.domain.entity.Favorite;
import com.game.blog.mapper.FavoriteMapper;
import com.game.blog.service.IFavoriteService;
import org.springframework.stereotype.Service;

import jakarta.annotation.Resource;
import java.time.LocalDateTime;
import java.util.List;

@Service
public class FavoriteServiceImpl extends ServiceImpl<FavoriteMapper, Favorite> implements IFavoriteService {

    @Resource
    private FavoriteMapper favoriteMapper;

    @Override
    public void addFavorite(Long userId, Long gameId) {
        Favorite favorite = new Favorite();
        favorite.setUserId(userId);
        favorite.setGameId(gameId);
        favorite.setCreatedAt(LocalDateTime.now());
        this.save(favorite);
    }

    @Override
    public void removeFavorite(Long userId, Long gameId) {
        LambdaQueryWrapper<Favorite> wrapper = new LambdaQueryWrapper<>();
        wrapper.eq(Favorite::getUserId, userId);
        wrapper.eq(Favorite::getGameId, gameId);
        this.remove(wrapper);
    }

    @Override
    public boolean isFavorited(Long userId, Long gameId) {
        return favoriteMapper.countUserFavorite(userId, gameId) > 0;
    }

    @Override
    public List<Favorite> getUserFavorites(Long userId) {
        return favoriteMapper.selectUserFavorites(userId);
    }
}