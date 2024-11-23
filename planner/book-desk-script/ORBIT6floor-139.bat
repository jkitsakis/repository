@echo off 

set data="{\"dates\":[\"%1\"],\"facilityId\":\"63f73fbd79d8d3143f3ae2ba\",\"positionId\":\"672b3e9e18b7a57f32db5659\",\"x\":1038.662240478052,\"y\":169.33334350585938,\"code\":\"139\",\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"%1\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}"

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
