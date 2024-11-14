@echo off 

set url_test="https://httpbin.org/post"
set url="https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/deskbooking"
set header="Content-Type: application/json"
set cookie="Cookie: Path=/; Path=/; Path=/; _ga=GA1.1.2086248922.1725605193; _ga_PV0JVKBGJ5=GS1.1.1728549146.3.1.1728549241.0.0.0; TS00000000076=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4109d0002c414daca58a0b699f46146bcbde638c98ad92ed06571e023144e38b763b9466c6b7bf992381b930f3125a803c7b3e4e3bda2704b04d7c23c1bf8fbb57c98046742f4ddb9b2e79b8514879e75568ac15d179109caeaebf3e0a82af0718e8372c5870af9f96c815662ae274527f65aa5e977b4fd7820b34da5938db370b9138f90138be50d7c51564be260b2d32c0e4ddf82d17a7bef6a7fd0ca61788d469ad71428bf9c346073af2a64d77d44810d7005e3f11a26b0480f6b76c05f82fc5a4bfb36cb5f3ee07a899697550a1a8ae6d59; TSPD_101_DID=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4106380090e31c1c8fd8def8622a1c50a3e582f0eafd739bc15ef7424e7b0df059e5eb21ab4ad20ffe6c716dfc942ac32212737c2234ecd3605f0866; JSESSIONID=2672A16945EAB180F73884357FA2BB9E; TS010ee64b=01eb1053a051b782b53aab456b14e5e86126fddcd77c435749fc42cf8090c3e6430df214e178006e99da16b3ba63dd35389cd570bcc898c325693bb5c6bf2fa10da745e418bc4c4fd29ed0fa8ab2f28ba226a23088; TSf455e12a027=0804a8c53bab20001f043bdeecfedbb603e10cf9f0351c6a3b57e209cc9547ea6d9466fd5ab5a619084bbdc02411300098367f9c2355d52e82091ca0091adaea6f902512689f9eafc18809d98465bf32c3982dd073689f977d410507e484dc82"

set data1="{\"dates\":[\"2024-11-11\"],\"facilityId\":\"6448cee7bf530c0226ea4d4d\",\"positionId\":\"6448cee7bf530c0226ea4d55\",\"x\":1225,\"y\":1504,\"code\":\"008\",\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"2024-11-11\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}"

set data2="{\"dates\":[\"2024-11-12\"],\"facilityId\":\"6448cee7bf530c0226ea4d4d\",\"positionId\":\"6448cee7bf530c0226ea4d5c\",\"x\":1404,\"y\":881,\"code\":\"015\",\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"2024-11-12\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}"

set data3="{\"dates\":[\"2024-11-13\"],\"facilityId\":\"6448d14dbf530c0226ea4d6a\",\"positionId\":\"6448d14dbf530c0226ea4d72\",\"x\":759.0,\"y\":1768.0,\"code\":\"023\",\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"2024-11-13\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}"

set data4="{\"dates\":[\"2024-11-14\"],\"facilityId\":\"6448cee7bf530c0226ea4d4d\",\"positionId\":\"6448cee7bf530c0226ea4d57\",\"x\":1349,\"y\":1238,\"code\":\"010\",\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"2024-11-14\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}"

set data5="{\"dates\":[\"2024-11-15\"],\"facilityId\":\"6448d14dbf530c0226ea4d6a\",\"positionId\":\"6448d14dbf530c0226ea4d88\",\"x\":1247,\"y\":921,\"code\":\"046\",\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"2024-11-15\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}"

set data01="{\"dates\":[\"2024-11-08\"],\"facilityId\":\"63f73fbd79d8d3143f3ae2ba\",\"positionId\":\"63f73fbd79d8d3143f3ae300\",\"x\":985.6339604548871,\"y\":222.33334350585938,\"code\":\"146\",\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"2024-11-08\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}"

set data02="{\"dates\":[\"2024-11-11\"],\"facilityId\":\"64a41c5241d4b80382ab638b\",\"positionId\":\"64a41cb441d4b80382ab63b9\",\"x\":401.2236926360724,\"y\":1784.000738098167,\"code\":\"085\",\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"2024-11-11\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"]}"


:start
REM set time_start= %time% 

REM Running curl commands in parallel
start /b curl  -X POST %url%  -H %header% -H %cookie% -d %data2% >> logfile1.txt
start /b curl  -X POST %url%  -H %header% -H %cookie% -d %data1% >> logfile2.txt
start /b curl  -X POST %url%  -H %header% -H %cookie% -d %data3%   
start /b curl  -X POST %url%  -H %header% -H %cookie% -d %data4%   
start /b curl  -X POST %url%  -H %header% -H %cookie% -d %data5%  

REM echo %time%-%time_start%
REM pause
REM timeout /t 1 /nobreak > nul
goto start 
