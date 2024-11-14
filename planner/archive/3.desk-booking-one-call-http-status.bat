@echo off 

set url_test="https://httpbin.org/post"
set url="https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/deskbooking"
set header="Content-Type: application/json"
set cookie="Cookie: Path=/; Path=/; Path=/; _ga=GA1.1.2086248922.1725605193; _ga_PV0JVKBGJ5=GS1.1.1728549146.3.1.1728549241.0.0.0; TS00000000076=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4109d0002c414daca58a0b699f46146bcbde638c98ad92ed06571e023144e38b763b9466c6b7bf992381b930f3125a803c7b3e4e3bda2704b04d7c23c1bf8fbb57c98046742f4ddb9b2e79b8514879e75568ac15d179109caeaebf3e0a82af0718e8372c5870af9f96c815662ae274527f65aa5e977b4fd7820b34da5938db370b9138f90138be50d7c51564be260b2d32c0e4ddf82d17a7bef6a7fd0ca61788d469ad71428bf9c346073af2a64d77d44810d7005e3f11a26b0480f6b76c05f82fc5a4bfb36cb5f3ee07a899697550a1a8ae6d59; TSPD_101_DID=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4106380090e31c1c8fd8def8622a1c50a3e582f0eafd739bc15ef7424e7b0df059e5eb21ab4ad20ffe6c716dfc942ac32212737c2234ecd3605f0866; JSESSIONID=2672A16945EAB180F73884357FA2BB9E; TS010ee64b=01eb1053a051b782b53aab456b14e5e86126fddcd77c435749fc42cf8090c3e6430df214e178006e99da16b3ba63dd35389cd570bcc898c325693bb5c6bf2fa10da745e418bc4c4fd29ed0fa8ab2f28ba226a23088; TSf455e12a027=0804a8c53bab20001f043bdeecfedbb603e10cf9f0351c6a3b57e209cc9547ea6d9466fd5ab5a619084bbdc02411300098367f9c2355d52e82091ca0091adaea6f902512689f9eafc18809d98465bf32c3982dd073689f977d410507e484dc82"

set data="{\"dates\":[\"2024-11-11\",\"2024-11-12\",\"2024-11-13\",\"2024-11-14\",\"2024-11-15\"],\"facilityId\":\"6448cee7bf530c0226ea4d4d\",\"positionId\":\"6448cee7bf530c0226ea4d57\",\"x\":1349,\"y\":1238,\"code\":\"010\",\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"2024-11-11\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"},{\"date\":\"2024-11-12\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"},{\"date\":\"2024-11-13\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"},{\"date\":\"2024-11-14\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"},{\"date\":\"2024-11-15\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}"


:start
for /f "tokens=*" %%i in ('curl -o NUL -s -w "%%{http_code}" -X POST %url_test% -H %header% -H %cookie% -d %data%') do set HTTP_STATUS=%%i

REM Output the status code
REM echo HTTP Status: %HTTP_STATUS%

if %HTTP_STATUS% == 200 (
	echo "OK ... "
    pause
) else (
	REM echo %status%	
    goto start
)

