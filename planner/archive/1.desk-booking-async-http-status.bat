@echo off
setlocal enabledelayedexpansion

set url_test=https://httpbin.org/post
set url=https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/deskbooking
set header="Content-Type: application/json"
set cookie="Cookie: Path=/; Path=/; Path=/; _ga=GA1.1.2086248922.1725605193; _ga_PV0JVKBGJ5=GS1.1.1728549146.3.1.1728549241.0.0.0; TS00000000076=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4109d0002c414daca58a0b699f46146bcbde638c98ad92ed06571e023144e38b763b9466c6b7bf992381b930f3125a803c7b3e4e3bda2704b04d7c23c1bf8fbb57c98046742f4ddb9b2e79b8514879e75568ac15d179109caeaebf3e0a82af0718e8372c5870af9f96c815662ae274527f65aa5e977b4fd7820b34da5938db370b9138f90138be50d7c51564be260b2d32c0e4ddf82d17a7bef6a7fd0ca61788d469ad71428bf9c346073af2a64d77d44810d7005e3f11a26b0480f6b76c05f82fc5a4bfb36cb5f3ee07a899697550a1a8ae6d59; TSPD_101_DID=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4106380090e31c1c8fd8def8622a1c50a3e582f0eafd739bc15ef7424e7b0df059e5eb21ab4ad20ffe6c716dfc942ac32212737c2234ecd3605f0866; JSESSIONID=2672A16945EAB180F73884357FA2BB9E; TS010ee64b=01eb1053a051b782b53aab456b14e5e86126fddcd77c435749fc42cf8090c3e6430df214e178006e99da16b3ba63dd35389cd570bcc898c325693bb5c6bf2fa10da745e418bc4c4fd29ed0fa8ab2f28ba226a23088; TSf455e12a027=0804a8c53bab20001f043bdeecfedbb603e10cf9f0351c6a3b57e209cc9547ea6d9466fd5ab5a619084bbdc02411300098367f9c2355d52e82091ca0091adaea6f902512689f9eafc18809d98465bf32c3982dd073689f977d410507e484dc82"


set data1="{\"dates\":[\"2024-11-11\"],\"facilityId\":\"6448cee7bf530c0226ea4d4d\",\"positionId\":\"6448cee7bf530c0226ea4d55\",\"x\":1225,\"y\":1504,\"code\":\"008\",\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"2024-11-11\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}"

set data2="{\"dates\":[\"2024-11-12\"],\"facilityId\":\"6448cee7bf530c0226ea4d4d\",\"positionId\":\"6448cee7bf530c0226ea4d5c\",\"x\":1404,\"y\":881,\"code\":\"015\",\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"2024-11-12\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}"

set data3="{\"dates\":[\"2024-11-13\"],\"facilityId\":\"6448d14dbf530c0226ea4d6a\",\"positionId\":\"6448d14dbf530c0226ea4d72\",\"x\":759.0,\"y\":1768.0,\"code\":\"023\",\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"2024-11-13\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}"

set data4="{\"dates\":[\"2024-11-14\"],\"facilityId\":\"6448cee7bf530c0226ea4d4d\",\"positionId\":\"6448cee7bf530c0226ea4d57\",\"x\":1349,\"y\":1238,\"code\":\"010\",\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"2024-11-14\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}"

set data5="{\"dates\":[\"2024-11-15\"],\"facilityId\":\"6448d14dbf530c0226ea4d6a\",\"positionId\":\"6448d14dbf530c0226ea4d88\",\"x\":1247,\"y\":921,\"code\":\"046\",\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"2024-11-15\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}"



:: Define log file path
set "logfile=logfile.txt"

:: Array of request data
set "requests[0]=%data1%"
set "requests[1]=%data2%"
set "requests[2]=%data3%"
set "requests[3]=%data4%"
set "requests[4]=%data5%"

:: Infinite loop
:loop
	echo %date% %time% - Starting new round of requests

    :: Send requests in parallel
    set "success=0"
	  REM for /L %%i in (0, 1, 1) do ( - 2 days
    for /L %%i in (0, 1, 4) do (
        start /b "" cmd /c (			
            for /f "tokens=*" %%a in ('curl -o NUL -s -w "%%{http_code}" -X POST %url% -H %header% -H %cookie% -d "!requests[%%i]!"') do set "status=%%a"
			REM call :calculate_duration !startTime! !endTime! duration			
            if "!status!"=="200" (
				echo %date% %time% - Request %%i succeeded, status 200
                REM echo %date% %time% - Request %%i succeeded, status 200, duration: !duration! ms >> "%logfile%"
            ) else (
				echo %date% %time% - Request %%i failed - status: !status!, retrying... 
                REM echo %date% %time% - Request %%i failed - status: !status!, retrying... , duration: !duration! ms>> "%logfile%"
                set "success=1"
            )
            REM del response_status_%%i.txt
        )
    )

    :: If any request failed, loop again
    if !success! neq 0 (
		echo Resend ...
        goto loop
    )
	
	pause

endlocal
exit /b

:calculate_duration
    setlocal
    set "start=%~1"
    set "end=%~2"

    :: Parse start time into hours, minutes, seconds, and milliseconds
    for /f "tokens=1-4 delims=:.," %%a in ("%start%") do (
        set /a "start_ms=%%a*3600000 + %%b*60000 + %%c*1000 + %%d"
    )

    :: Parse end time into hours, minutes, seconds, and milliseconds
    for /f "tokens=1-4 delims=:.," %%a in ("%end%") do (
        set /a "end_ms=%%a*3600000 + %%b*60000 + %%c*1000 + %%d"
    )

    :: Calculate the duration in milliseconds
    set /a duration=end_ms - start_ms
    if %duration% lss 0 set /a duration+=86400000  :: Account for midnight rollover

    endlocal & set "%~3=%duration%"
    exit /b

