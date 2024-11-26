@echo off

set url_httpbin="https://httpbin.org/post"

set url_planner="https://myplanner.netcompany-intrasoft.com/deskbooking/api/v1/deskbooking"

set header="Content-Type: application/json"

set header-agent= "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

set cookie="Cookie: Path=/; Path=/; Path=/; Path=/; _ga=GA1.1.2086248922.1725605193; _ga_PV0JVKBGJ5=GS1.1.1728549146.3.1.1728549241.0.0.0; TS00000000076=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4109d0002c414daca58a0b699f46146bcbde638c98ad92ed06571e023144e38b763b9466c6b7bf992381b930f3125a803c7b3e4e3bda2704b04d7c23c1bf8fbb57c98046742f4ddb9b2e79b8514879e75568ac15d179109caeaebf3e0a82af0718e8372c5870af9f96c815662ae274527f65aa5e977b4fd7820b34da5938db370b9138f90138be50d7c51564be260b2d32c0e4ddf82d17a7bef6a7fd0ca61788d469ad71428bf9c346073af2a64d77d44810d7005e3f11a26b0480f6b76c05f82fc5a4bfb36cb5f3ee07a899697550a1a8ae6d59; TSPD_101_DID=0804a8c53bab2800052b11046155e2079d406b493688b1c1eae347c0cdc79b6a22bbc0c27f3b3f57d05d3f07d9fd062808406f9e4106380090e31c1c8fd8def8622a1c50a3e582f0eafd739bc15ef7424e7b0df059e5eb21ab4ad20ffe6c716dfc942ac32212737c2234ecd3605f0866; JSESSIONID=4599061E1541B164CBC4BDD7F55DE028; TS010ee64b=01eb1053a0f6f6f23a29f27619d60704571850da0545418beef40b6f73e23095eb90b9253a0a52a27ed30ba009e4bf047106ec5d8fd1261a929cbece0fd12fff0c914e8a36e901a3391d53936c7b8a90926a6c2e37; TSf455e12a027=0804a8c53bab2000eaa7276aee6300b6160403a410580b3c359e257a2af9428981c60ec559a5187708ca518a06113000e10cb65dafe54890b7bdc0a509d3d8258943268e4a4e9e7e22669beb9a532fc83067b55f9c880984504962f6ecd0bce1"

set url=%url_planner%

set mon=2024-12-02
set tue=2024-12-03
set wed=2024-12-04
set thu=2024-12-05
set fri=2024-12-06

echo %time%
REM risky desks : 012
start  cmd /c AMALIASMesazzine-008.bat %mon% 
start  cmd /c AMALIASMesazzine-010.bat %tue% 
start  cmd /c AMALIASMesazzine-012.bat %wed% 
start  cmd /c AMALIAS1Floor-044.bat %thu% 
start  cmd /c AMALIASMesazzine-016.bat %fri% 

pause