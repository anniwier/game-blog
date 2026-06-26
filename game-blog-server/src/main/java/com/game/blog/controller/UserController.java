package com.game.blog.controller;

import cn.dev33.satoken.stp.StpUtil;
import com.game.blog.common.response.Result;
import com.game.blog.domain.vo.UserVO;
import com.game.blog.service.IUserService;
import org.springframework.web.bind.annotation.*;

import jakarta.annotation.Resource;

@RestController
@RequestMapping("/api/user")
public class UserController {

    @Resource
    private IUserService userService;

    @GetMapping("/info")
    public Result<UserVO> getUserInfo() {
        long userId = StpUtil.getLoginIdAsLong();
        UserVO userVO = userService.getUserInfo(userId);
        return Result.success(userVO);
    }

    @GetMapping("/info/{userId}")
    public Result<UserVO> getUserInfoById(@PathVariable Long userId) {
        UserVO userVO = userService.getUserInfo(userId);
        return Result.success(userVO);
    }
}