@echo off
SET DOCKER_HOST=http://192.168.235.130
SET JAVA_HOME=C:\Program Files\Java\jdk1.8.0_45
SET M2_HOME=C:\kitsakis\Projects\ACTS\maven-3.3.9
SET MAVEN_OPTS=-Xmx1024m  -Dfile.encoding=UTF8
SET DEVELOPMENT_HOME=C:\kitsakis\Projects\my_work\my_workspace\maven-docker
SET PATH=%PATH%;C:\Program Files\Git\bin;C:\windows\system32;%M2_HOME%\bin;C:\Program Files (x86)\Notepad++;
SET JAVA_OPTS=%JAVA_OPTS% -Xms512M -Xmx4096M

:start
cls   
title Maven Docker MENU 
echo    
echo        ---------------------------      
echo              Main Menu       
echo        ---------------------------
echo   VM :%DOCKER_HOST%
echo   Ubuntu VM : ubuntu / admin
echo        ---------------------------
echo   0. Exit 
echo   -
echo   1. Transit-Build  
echo   -
echo   2. Transit-Build No tests
echo   -
echo   - 
echo   -----------------------------------------
echo   ---- Utilities ----
echo   -----------------------------------------
echo   gitbash. Git Bash






  
set /p opt=Type option: 

if "%opt%"=="gitbash" goto gitbash
if "%opt%"=="artifactory" goto trs_deploy_artifactory
if "%opt%"=="version" goto version
if "%opt%"=="giteye" goto giteye
if "%opt%"=="checkversions" goto checkdependencies
if "%opt%"=="updatedep" goto updatedependency

if "%opt%"=="2" goto build_no_tests
if "%opt%"=="1" goto build
if "%opt%"=="0" goto exit
goto start

:exit
cls
exit


:gitbash  
cd %DEVELOPMENT_HOME%\maven-docker
start C:\Windows\SysWOW64\cmd.exe /c "C:\Program Files\Git\git-bash.exe" 
pause
goto start



:build
cd %DEVELOPMENT_HOME%\maven-docker
call mvn clean install -U
pause
goto start 


:build_no_tests
cd %DEVELOPMENT_HOME%\maven-docker
call mvn clean install -U -DskipTests
pause
goto start


pause