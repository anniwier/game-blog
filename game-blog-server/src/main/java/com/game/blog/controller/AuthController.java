package com.game.blog.controller;

import cn.dev33.satoken.stp.StpUtil;
import com.game.blog.common.response.Result;
import com.game.blog.domain.dto.LoginDTO;
import com.game.blog.domain.dto.RegisterDTO;
import com.game.blog.domain.vo.LoginVO;
import com.game.blog.service.IUserService;
import org.springframework.web.bind.annotation.*;

import jakarta.annotation.Resource;
import jakarta.validation.Valid;

@RestController
@RequestMapping("/api/auth")
public class AuthController {

    @Resource
    private IUserService userService;

    @PostMapping("/login")
    public Result<LoginVO> login(@Valid @RequestBody LoginDTO loginDTO) {
        LoginVO loginVO = userService.login(loginDTO);
        return Result.success(loginVO);
    }

    @PostMapping("/register")
    public Result<Void> register(@Valid @RequestBody RegisterDTO registerDTO) {
        userService.register(registerDTO);
        return Result.success();
    }

    @PostMapping("/logout")
    public Result<Void> logout() {
        StpUtil.logout();
        return Result.success();
    }
}