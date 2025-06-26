@echo off
setlocal enabledelayedexpansion

:MENU
cls
echo 1. Choose Python version and create .venv
echo 2. Export requirements.txt
echo 3. Install from requirements.txt
echo 4. Exit
set /p choice="Enter your choice: "

if "%choice%"=="1" goto CHOOSE_PYTHON
if "%choice%"=="2" goto EXPORT_REQUIREMENTS
if "%choice%"=="3" goto INSTALL_REQUIREMENTS
if "%choice%"=="4" exit
goto MENU

:CHOOSE_PYTHON
echo Searching for installed Python versions...
for /f "delims=" %%i in ('where /R "%ProgramFiles%" python.exe 2^>nul') do (
    echo %%i
    set /a count+=1
    set "py!count!=%%i"
)

if "!count!"=="0" (
    echo No Python installations found.
    pause
    goto MENU
)

echo.
echo Select a Python version:
for /L %%i in (1,1,!count!) do (
    echo %%i. !py%%i!
)
set /p pychoice="Enter the number of the Python version to use: "
set "PYTHON_EXE=!py%pychoice%!"

if not exist "%PYTHON_EXE%" (
    echo Invalid selection.
    pause
    goto MENU
)

echo Creating virtual environment with %PYTHON_EXE%...
"%PYTHON_EXE%" -m venv .venv

echo Virtual environment created.
pause
goto MENU

:EXPORT_REQUIREMENTS
echo Exporting requirements.txt...
if not exist .venv\Scripts\activate (
    echo No virtual environment found. Please run option 1 first.
    pause
    goto MENU
)

call .venv\Scripts\activate.bat

pip show pipreqs >nul 2>&1
if errorlevel 1 (
    echo Installing pipreqs...
    pip install pipreqs
)

pipreqs . --force --savepath=requirements.txt --use-local --no-pin

echo requirements.txt exported (no version numbers).
pause
goto MENU

:INSTALL_REQUIREMENTS
if not exist requirements.txt (
    echo requirements.txt not found.
    pause
    goto MENU
)

if not exist .venv\Scripts\activate (
    echo No virtual environment found. Please run option 1 first.
    pause
    goto MENU
)

call .venv\Scripts\activate.bat
echo Installing from requirements.txt...
pip install -r requirements.txt

echo Installation complete.
pause
goto MENU
