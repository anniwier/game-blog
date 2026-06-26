package com.game.blog.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.game.blog.domain.entity.Game;
import com.game.blog.domain.vo.GameItemVO;

import org.apache.ibatis.annotations.Param;

import java.util.List;

public interface GameMapper extends BaseMapper<Game> {

    List<GameItemVO> selectGameItemList();

    List<GameItemVO> selectTopGameItemList();

    List<GameItemVO> selectGameItemListByTag(@Param("tagId") Long tagId);

    GameItemVO selectGameItemById(Long id);

    List<GameItemVO> selectGameItemListByCategory(@Param("categoryId") Long categoryId);

    List<GameItemVO> searchGameItemList(@Param("keyword") String keyword);
}