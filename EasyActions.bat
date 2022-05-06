@echo off
title EasyActions [By ShadowOcto]
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
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

:select
cls
echo What action would you like to perform?
echo [1] Restart Explorer (TASKBAR, etc.)
echo [2] Check Internet Status
echo [3] Optimise Ram
echo.
set /p ac="Action: "

if %ac%==1 (
goto restart
)
if %ac%==2 (
goto internet
)
if %ac%==3 (
goto ram
)
if %ac%=="" (
goto select
)
if %ac%==" " (
goto select
)

cls
color 0c
echo Action not found!
pause>nul
color 0f
goto select

:restart
cls
TASKKILL /f /im explorer.exe
explorer
goto select

:internet
cls
:check
ping -n 1 1.1.1.1 | find "TTL"
if not errorlevel 1 set error=Internet is online!&&color 0a
if errorlevel 1 set error=Oh no, Internet is offline...&& color 0c
cls
echo %error%
timeout /t 1 >nul
goto check

:ram
cd .\Addons
cls
echo Optimising Ram...
EmptyStandbyList.exe workingsets
EmptyStandbyList.exe modifiedpagelist
EmptyStandbyList.exe priority0standbylist
EmptyStandbyList.exe standbylist
goto select