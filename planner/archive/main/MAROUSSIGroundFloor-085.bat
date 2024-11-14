@echo off 

set data="{\"dates\":[\"%1\"],\"facilityId\":\"64a41c5241d4b80382ab638b\",\"positionId\":\"64a41cb441d4b80382ab63b9\",\"x\":401.2236926360724,\"y\":1784.000738098167,\"code\":\"085\",\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"%1\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}"

:start
title %1
for /f "tokens=*" %%i in ('curl -o NUL -s -w "%%{http_code}" -X POST %url% -H %header% -H %cookie% -d %data%') do set HTTP_STATUS=%%i

if %HTTP_STATUS% == 200 (
	echo OK ... 
    pause
) else (
	echo %HTTP_STATUS%	
    goto start
)
