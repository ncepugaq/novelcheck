@echo off
title NovelCheck
echo Starting NovelCheck, please wait...
echo.

python main.py 2>&1

set EXITCODE=%errorlevel%
if %EXITCODE% equ 9009 (
    echo.
    echo   ERROR: Python is not installed or not in PATH.
    echo   Please run setup.bat first.
    echo.
) else if %EXITCODE% neq 0 (
    echo.
    echo   Program exited with code %EXITCODE%.
    echo   Check the error messages above.
    echo.
)

echo.
pause
