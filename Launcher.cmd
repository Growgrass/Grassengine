@echo off
title ---Launcher---

REM  --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )
:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
    "%temp%\getadmin.vbs"
    exit /B
:gotAdmin
    if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )
    pushd "%CD%"
    CD /D "%~dp0"
REM Done!

:main
cls
echo.
echo.
echo -------------------------------------------------------------------------------------------------------------------------------
echo.
echo  Grassengine Launcher
echo.
echo  v1.0.0
echo.
echo -------------------------------------------------------------------------------------------------------------------------------
echo.
echo.
echo  [1] Start
echo.
echo  [2] Stop
echo.
echo  [3] Setup
echo.
echo  [4] help
echo.
echo  [5] exit
echo.
echo.
echo -------------------------------------------------------------------------------------------------------------------------------
echo.
set menu=
set /p menu= [ 원하시는 작업 번호를 입력 후 엔터(Enter)키를 눌러주세요 ] : 
if "%menu%" == "1" goto !start
if "%menu%" == "2" goto !stop
if "%menu%" == "3" goto !setup
if "%menu%" == "4" goto !help
if "%menu%" == "5" exit
goto main

:!start
cls
python main.py start

:!stop
python main.py stop

:!setup
cls
echo.
echo.
echo -------------------------------------------------------------------------------------------------------------------------------
echo.
echo  Grassengine Launcher
echo.
echo -------------------------------------------------------------------------------------------------------------------------------
echo.
echo.
echo  [1] Grasscutter
echo.
echo  [2] Resources
echo.
echo  [3] Proxy
echo.
echo.
echo -------------------------------------------------------------------------------------------------------------------------------
echo.
set menu=
set /p menu= [ 원하시는 작업 번호를 입력 후 엔터(Enter)키를 눌러주세요 ] : 
if "%menu%" == "1" python main.py setup Grasscutter
if "%menu%" == "2" python main.py setup Resources
if "%menu%" == "3" python main.py setup Proxy
