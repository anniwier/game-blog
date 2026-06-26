@echo off
chcp 65001 >nul
title 停止游戏鉴赏博客服务

echo ====================================
echo   正在停止所有服务...
echo ====================================
echo.

:: 终止后端 Java 进程
echo [1/2] 停止后端服务...
wmic process where "commandline like '%%spring-boot%%' or name like '%%java%%' and commandline like '%%game-blog%%'" delete >nul 2>&1
taskkill /f /fi "WINDOWTITLE eq 后端服务 - game-blog" >nul 2>&1

:: 终止前端 Node 进程
echo [2/2] 停止前端服务...
taskkill /f /fi "WINDOWTITLE eq 前端服务 - game-blog" >nul 2>&1
taskkill /f /im node.exe >nul 2>&1

echo.
echo ====================================
echo   所有服务已停止！
echo ====================================
echo.
pause