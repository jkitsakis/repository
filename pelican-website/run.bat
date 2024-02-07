@echo off

SET PORT=2020
SET DEMO_NAME=SandyCV
SET APP_HOME=C:\Workspace\My-Applications\GitHub\repository\pelican-website
SET PYTHON_ENV=C:\Workspace\My-Applications\PythonEnvironments
SET PYTHON_SCRIPTS_PATH=%PYTHON_ENV%\pelicanenv\Scripts


:start
cls   
title %DEMO_NAME% CONSOLE
echo    
echo        ---------------------------      
echo              Main Menu 
echo        ---------------------------   
echo   1. Build %DEMO_NAME%
echo   2. Run %DEMO_NAME%
echo   3. Debug %DEMO_NAME%
echo   4. Deactivate Env %DEMO_NAME%
echo   5. Activate Env %DEMO_NAME%

set /p opt=Type option:
if "%opt%"=="0" goto cmd
if "%opt%"=="1" goto build
if "%opt%"=="2" goto run
if "%opt%"=="3" goto debug
if "%opt%"=="4" goto venv-deactivate
if "%opt%"=="5" goto venv-activate
goto start


:venv-activate
cd %PYTHON_SCRIPTS_PATH%
call activate 
pause
goto start 

:venv-deactivate
cd %PYTHON_SCRIPTS_PATH%
call deactivate 
pause
goto start 

:build
cd %PYTHON_SCRIPTS_PATH%
call activate 
cd %APP_HOME%
call pelican content -D
REM PORT=''\"%PORT%\"''
pause
goto start 

:run
cd %APP_HOME%
start cmd /k call pelican -lr -p %PORT%
pause
call "C:\Users\ikitsakis\AppData\Local\Programs\Opera\opera.exe"  --ran-launcher --remote http://localhost:%PORT%
pause
goto start 

:debug
cd %APP_HOME%
call pelican content --debug 
REM > Debug.txt 2>&1
pause
goto start 

:cmd
cd %PYTHON_SCRIPTS_PATH%
call activate 
cd %APP_HOME%
start cmd /k 
pause
goto start 

:exit
cd %PYTHON_SCRIPTS_PATH%
call deactivate 
cls
exit




pause