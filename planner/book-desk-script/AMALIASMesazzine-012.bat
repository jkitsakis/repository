@echo off 

set data="{\"dates\":[\"%1\"],\"facilityId\":\"6448cee7bf530c0226ea4d4d\",\"positionId\":\"6448cee7bf530c0226ea4d59\",\"x\":1382,\"y\":1171,\"code\":\"012\",\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"%1\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}"

:start
title %1
for /f "tokens=*" %%i in ('curl -o NUL -s -w "%%{http_code}" -X POST %url% -H %header% -H %header-agent% -H %cookie% -d %data%') do set HTTP_STATUS=%%i

if %HTTP_STATUS% == 200 (
	echo OK ... 
    pause
) else (
	echo %HTTP_STATUS%	
    goto start
)
