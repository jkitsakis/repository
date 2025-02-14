@echo off

SET PORT=2020
SET DEMO_NAME=SandyCV
SET APP_HOME=%cd%
SET PYTHON_ENV=%APP_HOME%\.venv
SET PYTHON_SCRIPTS_PATH=%PYTHON_ENV%\Scripts
SET PATH=%PYTHON_SCRIPTS_PATH%;%PATH%
SET OIKOGENEIAKOS_IATROS_DOMAIN=C:\Workspace\My-Applications\GitHub\oikogeneiakos-iatros-alimos.github.io

:start
cls   
title %DEMO_NAME% CONSOLE
echo    
echo        ---------------------------      
echo              Main Menu 
echo        ---------------------------   
echo   1. Build %DEMO_NAME%
echo   2. Run %DEMO_NAME%
echo   3. Export requirements.txt %DEMO_NAME%
echo   4. Upgrade packages %DEMO_NAME%
echo   5. Deploy %DEMO_NAME%

set /p opt=Type option:

if "%opt%"=="0" goto exit
if "%opt%"=="1" goto build
if "%opt%"=="2" goto run
if "%opt%"=="3" goto req
if "%opt%"=="4" goto update-packages
if "%opt%"=="5" goto deploy
if "%opt%"=="cmd" goto cmd
goto start


:cmd
call %PYTHON_SCRIPTS_PATH%\activate
start cmd /k "echo Command prompt started with the environment & cd /d %PYTHON_SCRIPTS_PATH%"
pause
goto start

:req
call %PYTHON_SCRIPTS_PATH%\activate
cd %APP_HOME%
call pip freeze > requirements.txt
move requirements.txt %APP_HOME%  2>nul
pause
goto start

:update-packages
call %PYTHON_SCRIPTS_PATH%\activate
cd %APP_HOME%
call python -m pip install --upgrade pip  || echo ❌ Failed to upgrade pip!
call pip install --upgrade --no-cache-dir -r requirements.txt
pause
goto start

:build
call %PYTHON_SCRIPTS_PATH%\activate
cd %APP_HOME%
rmdir /s /q output
call pelican content --delete-output
call pelican content -D
pause
goto start

:run
call %PYTHON_SCRIPTS_PATH%\activate
cd %APP_HOME%
start cmd /k call pelican -lr -p %PORT%
pause
start chrome --new-window http://localhost:%PORT%
pause
goto start

:debug
call %PYTHON_SCRIPTS_PATH%\activate
cd %APP_HOME%
call pelican content --debug
pause
goto start

:exit
call %PYTHON_SCRIPTS_PATH%\activate
call deactivate
cls
exit
pause