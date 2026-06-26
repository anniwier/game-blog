package com.game.blog.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.game.blog.domain.entity.GameCategory;
import com.game.blog.mapper.GameCategoryMapper;
import com.game.blog.service.IGameCategoryService;
import org.springframework.stereotype.Service;

@Service
public class GameCategoryServiceImpl extends ServiceImpl<GameCategoryMapper, GameCategory> implements IGameCategoryService {
}
