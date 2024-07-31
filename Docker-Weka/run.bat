@echo off
SETLOCAL

REM Allow connections from Docker container
echo Allowing connections from Docker container...
xhost +

REM Set DISPLAY environment variable
SET DISPLAY=%HOSTNAME%.local:0

REM Build and run Docker Compose
echo Building and running Docker Compose...
docker-compose up --build

REM Disable connections from Docker container
echo Disabling connections from Docker container...
xhost -

ENDLOCAL
