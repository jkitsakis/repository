@echo off

SET DEMO_NAME=MyPlanner App
SET APP_HOME=%cd%
SET PYTHON_ENV=%APP_HOME%\.venv
SET PYTHON_SCRIPTS_PATH=%PYTHON_ENV%\Scripts
SET PATH=%PYTHON_SCRIPTS_PATH%;%PATH%

:start
cls
title %DEMO_NAME% CONSOLE
echo
echo        ---------------------------
echo              Main Menu
echo        ---------------------------
echo   1. Run %DEMO_NAME%
echo   2. Export requirements.txt %DEMO_NAME%
echo   3. Upgrade packages %DEMO_NAME%

call %PYTHON_ENV%\Scripts\activate

set /p opt=Type option:
if "%opt%"=="0" goto exit
if "%opt%"=="1" goto run
if "%opt%"=="2" goto req
if "%opt%"=="3" goto update-packages
if "%opt%"=="cmd" goto cmd
goto start


:cmd
cd %PYTHON_SCRIPTS_PATH%
start cmd /k "%PYTHON_ENV%\Scripts\activate && echo Command prompt started with the environment" & cd /d %PYTHON_SCRIPTS_PATH%"
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


:run
cls
cd %APP_HOME%
python main.py
echo Planner script finished.
pause
goto start


:exit
cd %PYTHON_SCRIPTS_PATH%
cls
exit

pause
