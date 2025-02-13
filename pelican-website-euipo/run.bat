@echo off

SET PORT=1010
SET DEMO_NAME=EUIPO - Pelican
SET APP_HOME=%cd%
SET PYTHON_ENV=%APP_HOME%\.venv
SET PYTHON_SCRIPTS_PATH=%PYTHON_ENV%\Scripts
SET PATH=%PYTHON_SCRIPTS_PATH%

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

call %PYTHON_SCRIPTS_PATH%\activate

set /p opt=Type option:
if "%opt%"=="0" goto exit
if "%opt%"=="1" goto build
if "%opt%"=="2" goto run
if "%opt%"=="3" goto req
if "%opt%"=="4" goto update-packages
if "%opt%"=="cmd" goto cmd
goto start


:cmd
start cmd /k "echo Command prompt started with the environment & cd /d %PYTHON_SCRIPTS_PATH%"
pause
goto start

:req
cd %PYTHON_SCRIPTS_PATH%
call pip freeze > requirements.txt
move requirements.txt %APP_HOME%
pause
goto start

:update-packages
cd %APP_HOME%
call pip install --upgrade --no-cache-dir -r requirements.txt
pause
goto start


:build
cd %APP_HOME%
rmdir /s /q output
call pelican content --delete-output
call pelican content -D
pause
goto start 

:run
cd %APP_HOME%
start cmd /k call pelican -lr -p %PORT%
pause
REM call "C:\Users\ikitsakis\AppData\Local\Programs\Opera\opera.exe"  --ran-launcher --remote http://localhost:%PORT%
start chrome --new-window http://localhost:%PORT%
pause
goto start 

:debug
cd %APP_HOME%
call pelican content --debug 
REM > Debug.txt 2>&1
pause
goto start 


:exit
cd %PYTHON_SCRIPTS_PATH%
cls
exit

pause