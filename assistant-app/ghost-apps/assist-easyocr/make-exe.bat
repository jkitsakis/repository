@echo off
cd /d "%~dp0"

call %cd%\.venv\Scripts\activate.bat

python.exe -m pip install --upgrade pip

pip install pyinstaller

pyinstaller --onefile --noconsole --icon=windowprogram.ico --hidden-import=plyer.platforms.win.notification --hidden-import=plyer.platforms.win.toast assist.py
REM pyinstaller --onefile --hidden-import=plyer.platforms.linux.notify test.py


echo.
echo Build complete. Executable is in the dist\ folder.
pause
