@echo off

:start
cls   
title YouTube Download
echo        
echo        ---------------------------
echo              Main Menu       
echo        ---------------------------
echo   0. Exit  
echo   -
echo   1. Update app  
echo   -
echo   2. Download mp3
echo   -


set /p opt=Type option:
if "%opt%"=="2" goto downloadmp3
if "%opt%"=="1" goto update
if "%opt%"=="0" goto exit
goto start


:exit
cls
exit


:update
youtube-dl -U
goto exit

:downloadmp3
set /p url=YouTube URL:
youtube-dl --ignore-errors -f "bestaudio" --extract-audio --audio-format "mp3" --add-metadata  --output "./downloads/%%(title)s.%%(ext)s"  "%url%"
goto exit
