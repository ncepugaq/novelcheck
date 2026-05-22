@echo off
title NovelCheck - Environment Setup

echo ============================================================
echo   NovelCheck - Environment Setup
echo ============================================================
echo.

echo [1/3] Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo   ERROR: Python not found!
    echo.
    echo   Please install Python 3.10+ first:
    echo   Download: https://www.python.org/downloads/
    echo   IMPORTANT: Check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)
python --version 2>&1
echo   OK

echo.
echo [2/3] Upgrading pip (using Tsinghua mirror)...
python -m pip install --upgrade pip -q -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn

echo.
echo [3/3] Installing dependencies...
echo   Using Tsinghua mirror...
echo.

python -m pip install -r requirements.txt ^
    -i https://pypi.tuna.tsinghua.edu.cn/simple ^
    --trusted-host pypi.tuna.tsinghua.edu.cn ^
    --retries 5 ^
    --timeout 30

if errorlevel 1 (
    echo.
    echo   Tsinghua mirror failed, trying Aliyun mirror...
    echo.
    python -m pip install -r requirements.txt ^
        -i https://mirrors.aliyun.com/pypi/simple ^
        --trusted-host mirrors.aliyun.com ^
        --retries 5 ^
        --timeout 30

    if errorlevel 1 (
        echo.
        echo ============================================================
        echo   Installation FAILED!
        echo.
        echo   Possible causes:
        echo   1. Network issue - try again or use VPN
        echo   2. Try manual install in cmd:
        echo      pip install -r requirements.txt
        echo ============================================================
    ) else (
        goto success
    )
) else (
    goto success
)
goto end

:success
echo.
echo ============================================================
echo   Installation SUCCESS!
echo   Now run: run.bat
echo   Or:     python main.py
echo ============================================================

:end
echo.
pause
