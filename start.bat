@echo off
chcp 65001 >nul
title 游戏鉴赏博客 - 一键启动

echo ====================================
echo   游戏鉴赏博客系统 正在启动...
echo ====================================
echo.

:: 获取脚本所在目录
set "PROJECT_DIR=%~dp0"

:: ===== 自动创建数据库（如果不存在） =====
echo [0/4] 检查并创建数据库...
mysql -u root -p2992402041 -e "CREATE DATABASE IF NOT EXISTS game_blog DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;" 2>nul
if %errorlevel% neq 0 (
    echo    ! 数据库连接失败，请确保 MySQL 服务已启动且密码正确
    echo    ! 当前使用的密码: 2992402041（可在 application.yml 中修改）
    echo.
    pause
    exit /b 1
)
echo    数据库 game_blog 已就绪

:: 启动后端（新窗口，端口 8080）
echo [1/4] 启动后端服务...
start "game-blog-server" cmd /c "cd /d "%PROJECT_DIR%game-blog-server" && mvn spring-boot:run"

:: 等待后端初始化
echo    等待后端启动（约15秒）...
timeout /t 15 /nobreak >nul

:: 启动前端（新窗口，端口 3000）
echo [2/4] 启动前端服务...
start "game-blog-web" cmd /c "cd /d "%PROJECT_DIR%game-blog-web" && npm run dev"

:: 等待前端启动
timeout /t 4 /nobreak >nul

:: 打开浏览器
echo [3/4] 打开浏览器...
start http://localhost:3000

echo.
echo ====================================
echo   启动完成！
echo   后端地址: http://localhost:8080
echo   前端地址: http://localhost:3000
echo.
echo   测试账号:
echo     管理员: admin / admin123
echo     普通用户: gamer / gamer123
echo.
echo   关闭本窗口不会影响服务运行。
echo   如需停止服务，请运行 stop.bat
echo ====================================
echo.
pause