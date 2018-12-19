@echo off
SET TRADER_ADAPTER_HOME=D:\Projects\Trader-Partner-Adapter
SET WORKSPACE=%TRADER_ADAPTER_HOME%\workspace
SET JAVA_HOME=%ProgramFiles%\Java\jdk1.8.0_181
SET GIT_HOME=%ProgramFiles%\Git
SET SVN_HOME=%ProgramFiles%\TortoiseSVN\bin
SET PATH=%JAVA_HOME%\bin;%GIT_HOME%\bin;%SVN_HOME%\bin;
SET SVN_USER=s.mpousgos
SET SVN_PASS=arch101
rem Currently Using TortoiseSVN. Use this to Authenticate to SVN Repo
rem SET SVN_REPO=http://%SVN_USER%:%SVN_PASS%@thira.internal.intracom-it.com/svn/icisnet/sources/trader-partner-adapter
SET SVN_REPO=http://thira.internal.intracom-it.com/svn/icisnet/sources/trader-partner-adapter
SET GIT_REPO_NAME=tpa
SET SVN_BRANCH=tags/2.0.0



:start
cls   
title SVN To Git Migration
echo        
echo        ---------------------------
echo              Main Menu       
echo        ---------------------------
echo   0. Exit  
echo   -
echo   1. svn-migration-scripts help 
echo   -
echo   2. svn-migration-scripts verify
echo   -
echo   3. Authors
echo   -
echo   4. Clone (Standard SVN layouts)
echo   4-1. Clone Branch %SVN_BRANCH%
echo   -
echo   5. Clean the new Git repository
echo   5-1. Clean Branch %SVN_BRANCH%

  
set /p opt=Type option: 
if "%opt%"=="5-1" goto clean-branch
if "%opt%"=="5" goto clean
if "%opt%"=="4-1" goto clone-branch
if "%opt%"=="4" goto clone
if "%opt%"=="3" goto authors
if "%opt%"=="2" goto verify
if "%opt%"=="1" goto help
if "%opt%"=="0" goto exit
goto start

:exit
cls
exit

:help
java -jar %TRADER_ADAPTER_HOME%\svn-migration-scripts.jar authors --help authors
pause
goto eof

:verify
java -jar %TRADER_ADAPTER_HOME%\svn-migration-scripts.jar verify
pause
goto eof

:authors
java -jar %TRADER_ADAPTER_HOME%\svn-migration-scripts.jar authors %SVN_REPO% %SVN_USER% %SVN_PASS% > authors.txt
pause
goto eof

:clone
cd %WORKSPACE%
call "%GIT_HOME%\bin\bash.exe" --login -i -c "git svn clone --stdlayout --prefix=origin/ --no-minimize-url  %SVN_REPO% %GIT_REPO_NAME%"
pause
goto eof

:clone-branch
cd %WORKSPACE%
call "%GIT_HOME%\bin\bash.exe" --login -i -c "git svn clone --prefix=origin/ --no-minimize-url  %SVN_REPO%/%SVN_BRANCH% %GIT_REPO_NAME%-%SVN_BRANCH%"
pause
goto eof

:clean
cd %WORKSPACE%\%GIT_REPO_NAME%
java -Dfile.encoding=utf-8 -jar %TRADER_ADAPTER_HOME%\svn-migration-scripts.jar clean-git --force
pause
goto eof

:clean-branch
cd %WORKSPACE%\%GIT_REPO_NAME%-%SVN_BRANCH%
java -Dfile.encoding=utf-8 -jar %TRADER_ADAPTER_HOME%\svn-migration-scripts.jar clean-git --force
pause
goto eof

:eof
goto start