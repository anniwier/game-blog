package com.game.blog.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.game.blog.domain.entity.Favorite;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface FavoriteMapper extends BaseMapper<Favorite> {

    List<Favorite> selectUserFavorites(@Param("userId") Long userId);

    int countUserFavorite(@Param("userId") Long userId, @Param("gameId") Long gameId);
}