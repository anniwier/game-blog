package com.game.blog.service;

import com.baomidou.mybatisplus.extension.service.IService;
import com.game.blog.domain.dto.LoginDTO;
import com.game.blog.domain.dto.RegisterDTO;
import com.game.blog.domain.entity.User;
import com.game.blog.domain.vo.LoginVO;
import com.game.blog.domain.vo.UserVO;

public interface IUserService extends IService<User> {

    LoginVO login(LoginDTO loginDTO);

    void register(RegisterDTO registerDTO);

    UserVO getUserInfo(Long userId);
}