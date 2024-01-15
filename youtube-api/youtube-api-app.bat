@echo off
SET APP_HOME=D:\Projects\MY_SPACE\repository\youtube-api
SET TOOLS_HOME=D:\Projects\Trader-Partner-Adapter
SET JAVA_HOME=%ProgramFiles%\Java\jdk1.8.0_181
SET MAVEN_HOME=%TOOLS_HOME%\Tools\apache-maven-3.6.0
SET DEVELOPMENT_HOME=%APP_HOME%\youtube-api-app
SET GIT_HOME=%ProgramFiles%\Git
SET MAVEN_OPTS=-Xmx1024m  -Dfile.encoding=UTF8
SET DOMAIN_HOME=C:\ICISNET\Oracle\Middleware\user_projects\domains\base_domain\bin
SET PATH=%JAVA_HOME%\bin;%GIT_HOME%\bin;C:\windows\system32;%MAVEN_HOME%\bin;



:start
cls   
title youtube-api MENU
echo        
echo        ---------------------------
echo              Main Menu       
echo        ---------------------------
echo   0. Exit  
echo   -
echo   1. Build 
echo   -

  
set /p opt=Type option: 

if "%opt%"=="1" goto build
if "%opt%"=="0" goto exit
goto start

:exit
cls
exit


:build
cd %DEVELOPMENT_HOME%
call mvn clean install -U -X
pause
goto eof



:eof
goto start