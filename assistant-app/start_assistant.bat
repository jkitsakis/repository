
@echo off

SET DEMO_NAME=Assistant
SET APP_HOME=%cd%\app
SET PYTHON_ENV=%cd%\.venv
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

set /p opt=Type option:
if "%opt%"=="0" goto exit
if "%opt%"=="1" goto run
if "%opt%"=="2" goto requirments
if "%opt%"=="3" goto update-packages
if "%opt%"=="4" goto uninstall-all
if "%opt%"=="cmd" goto cmd
goto start

:uninstall-all
call %PYTHON_SCRIPTS_PATH%\activate
cd %APP_HOME%
for /F "delims=" %%i in ('pip freeze') do pip uninstall -y %%i
pause
goto start

:cmd
call %PYTHON_SCRIPTS_PATH%\activate
start cmd /k "echo Command prompt started with the environment & cd /d %PYTHON_SCRIPTS_PATH%"
pause
goto start

:requirments
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


:run
cls
cd %APP_HOME%
python %APP_HOME%\start_assistant.py --apikey="your-openai-key-here" --defaultlang="Greek" --modelfolder="%APP_HOME%\model" --soundsfolder="%APP_HOME%\sounds"
echo %DEMO_NAME% script finished.
pause
goto start


:exit
call %PYTHON_SCRIPTS_PATH%\activate
call deactivate
cls
exit
pause
