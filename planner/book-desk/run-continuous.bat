@echo off 

set url_httpbin="https://httpbin.org/post"

set url_planner="https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/deskbooking"

set header="Content-Type: application/json"

set cookie="Cookie: Path=/; Path=/; Path=/; _ga=GA1.1.2086248922.1725605193; _ga_PV0JVKBGJ5=GS1.1.1728549146.3.1.1728549241.0.0.0; TS00000000076=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4109d0002c414daca58a0b699f46146bcbde638c98ad92ed06571e023144e38b763b9466c6b7bf992381b930f3125a803c7b3e4e3bda2704b04d7c23c1bf8fbb57c98046742f4ddb9b2e79b8514879e75568ac15d179109caeaebf3e0a82af0718e8372c5870af9f96c815662ae274527f65aa5e977b4fd7820b34da5938db370b9138f90138be50d7c51564be260b2d32c0e4ddf82d17a7bef6a7fd0ca61788d469ad71428bf9c346073af2a64d77d44810d7005e3f11a26b0480f6b76c05f82fc5a4bfb36cb5f3ee07a899697550a1a8ae6d59; TSPD_101_DID=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4106380090e31c1c8fd8def8622a1c50a3e582f0eafd739bc15ef7424e7b0df059e5eb21ab4ad20ffe6c716dfc942ac32212737c2234ecd3605f0866; JSESSIONID=2672A16945EAB180F73884357FA2BB9E; TS010ee64b=01eb1053a0f1cae4b46f32b5664cccc3d3201f2afd0dc6894dc4418613ac4baaa4095870d1e0d73a9ce4d4ccd496155f8879de596c251cf9fdbc0bac0c4021bda1d0ce818425a220d44625218f1e26304f916fa8c6; TSf455e12a027=0804a8c53bab200044f2149a37e41771308643a91dab88feab50f65cf6a6059614cc0234636cc956080b5b4480113000093035b14e7c91fc00e29f354bd565b84fc5b121a97761df3b2227070bac90750d67f206e014e389deea662ec1b4d38a"

set url=%url_planner%
set mon=2024-11-18
set mon_position=\"facilityId\":\"6448cee7bf530c0226ea4d4d\",\"positionId\":\"6448cee7bf530c0226ea4d55\",\"x\":1225,\"y\":1504,\"code\":\"008\"
set tue=2024-11-19
set tue_position=\"facilityId\":\"6448cee7bf530c0226ea4d4d\",\"positionId\":\"6448cee7bf530c0226ea4d57\",\"x\":1349,\"y\":1238,\"code\":\"010\"
set wed=2024-11-20
set wed_position=\"facilityId\":\"6448cee7bf530c0226ea4d4d\",\"positionId\":\"6448cee7bf530c0226ea4d59\",\"x\":1382,\"y\":1171,\"code\":\"012\"
set thu=2024-11-21
set thu_position=\"facilityId\":\"6448d14dbf530c0226ea4d6a\",\"positionId\":\"6448d14dbf530c0226ea4d6f\",\"x\":1026,\"y\":201,\"code\":\"048\"
set fri=2024-11-22
set fri_position=\"facilityId\":\"6448d14dbf530c0226ea4d6a\",\"positionId\":\"6448d14dbf530c0226ea4d88\",\"x\":1247,\"y\":921,\"code\":\"046\"


set dataMon="{\"dates\":[\"%mon%\"],%mon_position%,\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"%mon%\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}"

set dataTue="{\"dates\":[\"%tue%\"],%tue_position%,\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"%tue%\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}"

set dataWed="{\"dates\":[\"%wed%\"],%wed_position%,\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"%wed%\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}"

set dataThu="{\"dates\":[\"%thu%\"],%thu_position%,\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"%thu%\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}"

set dataFri="{\"dates\":[\"%fri%\"],%fri_position%,\"parking\":[{\"parkingRequested\":false,\"plateNumber\":\"\",\"type\":\"All\"}],\"datesAndType\":[{\"date\":\"%fri%\",\"type\":\"0036\",\"clientName\":\"\",\"clientAddress\":\"\"}]}"



:start
echo %time% starting ...
start /b curl  -X POST %url%  -H %header% -H %cookie% -d %dataMon% >>log.txt
start /b curl  -X POST %url%  -H %header% -H %cookie% -d %dataTue% 
start /b curl  -X POST %url%  -H %header% -H %cookie% -d %dataWed% 
start /b curl  -X POST %url%  -H %header% -H %cookie% -d %dataThu% 
start /b curl  -X POST %url%  -H %header% -H %cookie% -d %dataFri% 
echo %time% ended 
goto start 
