@echo off 

set data="{\"dates\":[\"%1\"],\"facilityId\":\"6448d14dbf530c0226ea4d6a\",\"positionId\":\"6448d14dbf530c0226ea4d78\",\"x\":1262,\"y\":1577,\"code\":\"030\",\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"%1\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}"

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
