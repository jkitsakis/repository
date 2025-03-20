@echo off
SET DEMO_NAME=DXDTridion publications
SET DEMO_VERSION=0.0.1-SNAPSHOT
SET DEVELOPMENT_HOME=C:\Workspace
SET JAVA_HOME=%ProgramFiles%\Java\jdk-17
SET GIT_HOME=%ProgramFiles%\Git
SET M2_HOME=%DEVELOPMENT_HOME%\Tools\apache-maven-3.8.6
SET WORKSPACE=%DEVELOPMENT_HOME%\eFiling-eForm\Examples-Tutorials\springboot-publications\publications
SET MAVEN_OPTS=-Xmx1024m -Dfile.encoding=UTF8
SET DriverData=C:\Windows\System32\Drivers\DriverData
SET PATH=%JAVA_HOME%\bin;%M2_HOME%\bin;%PATH%;
SET JAVA_OPTS=-Xms1024M -Xmx2048M -XX:PermSize=1024M -XX:MaxPermSize=1024M 

:start
cls   
title %DEMO_NAME% %DEMO_VERSION%- j11 CONSOLE
echo    
echo        ---------------------------      
echo              Main Menu 
echo        ---------------------------
echo   1. Build %DEMO_NAME%
echo   2. Run %DEMO_NAME%
echo   3. Run JAR %DEMO_NAME%

set /p opt=Type option:
if "%opt%"=="git" goto gitbash
if "%opt%"=="p" goto package
if "%opt%"=="3" goto run-validator-jar
if "%opt%"=="2" goto build-no-tests
if "%opt%"=="1" goto build
if "%opt%"=="0" goto exit
goto start

:exit
cls
exit

:gitbash  
cd %WORKSPACE%
start %LOCALAPPDATA%\Programs\Git\git-bash.exe
pause
goto start 

:package
cd %WORKSPACE%
call mvn package -Peuipo
pause
goto start 


:build
cd %WORKSPACE%
call mvn clean install -U -Peuipo
REM -DskipTests
REM --log-file=C:\Workspace\eFiling-eForm\output.txt
pause
goto start

:build-no-tests
cd %WORKSPACE%
call mvn clean install -U -Peuipo -DskipTests
pause
goto start

:run-validator-jar
java -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=8008 -jar %WORKSPACE%\target\demo-%DEMO_VERSION%.jar --spring.config.location=classpath:/application.yml
pause
goto start


pause