@echo off

SET ECLIPSE_HOME=D:\Kitsakis\Projects\MY_SPACE\eclipse
SET JAVA_HOME=C:\Program Files\Java\jdk1.8.0_45
SET M2_HOME=D:\kitsakis\Projects\ACTS\maven-3.3.9
SET MAVEN_OPTS=-Xmx1024m  -Dfile.encoding=UTF8
SET DEVELOPMENT_HOME=%cd%\youtube-api-app
SET PATH=C:\Program Files\Git\bin;C:\windows\system32;%M2_HOME%\bin;C:\Program Files (x86)\Notepad++;%PATH%;
SET JAVA_OPTS=%JAVA_OPTS% -Xms512M -Xmx4096M


:start
cls   
title YT MENU 
echo    
echo        ---------------------------      
echo              Main Menu       
echo        ---------------------------
echo   0. Exit 
echo   -
echo   1. Eclipse  
echo   -
echo   2. Build  
  
set /p opt=Type option: 

if "%opt%"=="1" goto eclipse_ide
if "%opt%"=="2" goto trs_build
if "%opt%"=="0" goto exit
goto start

:exit
cls
exit


:eclipse_ide
cd %Eclipse_HOME%
call eclipse.exe
pause
goto start 

:trs_build
cd %DEVELOPMENT_HOME%
call mvn clean install -U
pause
goto start 

pause