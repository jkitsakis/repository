@echo off
rem  ---- Copy the Public Key to VM : 1.Git Bash 2. ssh-copy-id ubuntu@192.168.56.105 3.Restart vm
SET VM_URL=192.168.56.105
SET VM_USER=ubuntu
SET VM_PASSWORD=admin
SET VM_LOGIN=%VM_USER%@%VM_URL%
SET SG_SERVER=10.240.165.32
SET TH_SERVER=10.240.165.52
SET MY_SERVER=10.240.163.31
SET TA_SERVER=10.240.165.152
SET DOCKER_SERVER=192.168.99.100
SET JAVA_HOME=C:\Program Files\Java\jdk1.8.0_45
SET JBOSS_HOME=D:\Kitsakis\Projects\ACTS\wildfly8.2.0
SET M2_HOME=D:\Kitsakis\Projects\ACTS\maven-3.3.9
SET MAVEN_OPTS=-Xmx1024m  -Dfile.encoding=UTF8
SET DEVELOPMENT_HOME=D:\Kitsakis\Projects\ACTS\workspace
SET GIT_HOME=C:\Program Files\Git
SET GIT_EYE_HOME=D:\Kitsakis\Projects\ACTS\GitEye 
SET LINUX_DEVELOPMENT_HOME=/D/Kitsakis/Projects/ACTS/workspace
SET DBMAINTAIN_HOME=D:\Kitsakis\Projects\ACTS\dbmaintain-2.4
SET JDBC_DRIVER=D:\Kitsakis\Projects\ACTS\dbmaintain-2.4\postgresql-9.1-901.jdbc4.jar
SET PATH=%PATH%;C:\Program Files\Git\bin;C:\windows\system32;%M2_HOME%\bin;C:\Program Files (x86)\Notepad++;
SET JAVA_OPTS=%JAVA_OPTS%;-Djboss.bind.address=%VM_URL%;-Djboss.bind.address.management=%VM_URL%;-Djboss.bind.address.unsecure=%VM_URL%
SET JAVA_OPTS=%JAVA_OPTS%;-Djboss.binding.address=%VM_URL%;-Djboss.binding.address.management=%VM_URL%;-Djboss.binding.address.unsecure=%VM_URL%
SET JAVA_OPTS=%JAVA_OPTS%;-Dcom.sun.management.jmxremote;-Dcom.sun.management.jmxremote.port=9000
SET JAVA_OPTS=%JAVA_OPTS%;-Dcom.sun.management.jmxremote.ssl=false;-Dcom.sun.management.jmxremote.authenticate=false
SET JAVA_OPTS=%JAVA_OPTS%;-Djava.rmi.server.hostname=%VM_URL%;-Dcom.sun.management.jmxremote.rmi.port=9000
SET JAVA_OPTS=%JAVA_OPTS% -Xms512M -Xmx4096M

rem --- DB credentials --- 
rem SG:  SG_SERVER 5432 transit postgres postgres
rem TH:  TH_SERVER 5432 transit postgres postgres
rem MY:  MY_SERVER 5432 transit postgres postgres
rem TA:  TA_SERVER 5432 transit postgres postgres
rem VM: VM_URL 5432 transit acts acts
rem DOCKER :  DOCKER_SERVER transit postgres postgres

SET PGHOST=%VM_URL%
SET PGPORT=5432
SET PGDATABASE=transit
SET PGUSER=acts
SET PGPASSWORD=acts

:start
cls   
title ACTS CONSOLE on %VM_URL% 
echo    
echo        ---------------------------      
echo              Main Menu       
echo        ---------------------------
echo   VM :%VM_URL%, SG :%SG_SERVER%, TH :%TH_SERVER%, MY :%MY_SERVER%
echo   Ubuntu VM : %VM_URL% %VM_LOGIN%
echo   Other VMs : root/password
echo        ---------------------------
echo   0. Exit 
echo   -
echo   1. Transit-Build  
echo   -
echo   2. Transit-Build No tests
echo   -
echo   3. UI Build
echo   -
echo   4. UI Deploy to VM ,   4_1. to SG,    4_2. to TH,    4_3. for MY
echo   -
echo   5. WAR Deploy to VM,   5_1. to SG,    5_2. to TH,    5_3. to MY
echo   -
echo   6. Server logs: VM,    6_1.  SG,      6_2.  TH ,     6_3.  MY,
echo   -
echo   8. Run Integration Tests
echo   - 
echo   ----Flyway on %PGHOST%----
echo   -
echo   10. Migrate, 10_1. Clean, 10_2 Info, 10_3 Validate, 10_4 Baseline, 10_5 Repair, 10_6 Export-db
echo   -
echo   -----------------------------------------
echo   ---- Utilities ----
echo   -----------------------------------------
echo   vm. VM login
echo   - 
echo   start. Start VM ACTS
echo   - 
echo   stop. Stop VM ACTS
echo   - 
echo   gitbash. Git Bash
echo   -
echo   artifactory.  Clean deploy to Artifactory
echo   -
echo   version. Update Version
echo   -
rem echo   checkversions. Check pom Versions
rem echo   -
rem echo   updatedep. Update Dependency Version
rem echo   -
rem echo   giteye. GitEye
rem echo   -
rem echo   ci. Contineous Tests
rem echo   -

echo   -----------------------------------------
echo   ---- JgitFlow ----
echo   -----------------------------------------
echo   fstart. feature-start
echo   -
echo   ffinish. feature-finish
echo   -
echo   hstart. hotfix-start
echo   -
echo   hfinish. hotfix-finish
echo   -
echo   rstart. release-start
echo   -
echo   rfinish. release-finish
rem echo   -
rem echo   cmnrstart. release-start-cmn-msg
rem echo   -
rem echo   cmnrfinish. release-finish-cmn-msg


  
set /p opt=Type option: 

if "%opt%"=="fstart" goto fstart
if "%opt%"=="ffinish" goto ffinish
if "%opt%"=="rstart" goto rstart
if "%opt%"=="rfinish" goto rfinish
if "%opt%"=="hstart" goto hstart
if "%opt%"=="hfinish" goto hfinish
if "%opt%"=="cmnrstart" goto rstart-cmn-msg
if "%opt%"=="cmnrfinish" goto rfinish-cmn-msg
if "%opt%"=="stop" goto acts-docker-compose_stop
if "%opt%"=="start" goto acts-docker-compose_start
if "%opt%"=="vm" goto login
if "%opt%"=="swagger" goto swagger
if "%opt%"=="ci" goto ci
if "%opt%"=="jcl" goto jcl_run
if "%opt%"=="refnum" goto refnum_build
if "%opt%"=="refnumclient" goto refnumclient_build
if "%opt%"=="gms" goto gms_build
if "%opt%"=="decl" goto cmn_decl
if "%opt%"=="cmn" goto cmn_build
if "%opt%"=="acsn" goto acsn
if "%opt%"=="gitbash" goto gitbash
if "%opt%"=="artifactory" goto trs_deploy_artifactory
if "%opt%"=="version" goto version
if "%opt%"=="giteye" goto giteye
if "%opt%"=="chown" goto chown
if "%opt%"=="checkversions" goto checkdependencies
if "%opt%"=="updatedep" goto updatedependency

rem 10. Migrate, 10_1. Clean, 10_2 Info, 10_3 Validate, 10_4 Baseline, 10_5 Repair 
if "%opt%"=="10_6" goto export-db
if "%opt%"=="10_5" goto flyway_repair
if "%opt%"=="10_4" goto flyway_baseline
if "%opt%"=="10_3" goto flyway_validate
if "%opt%"=="10_2" goto flyway_info
if "%opt%"=="10_1" goto flyway_clean
if "%opt%"=="10" goto flyway_migrate
if "%opt%"=="9_2" goto dbschema_export
if "%opt%"=="9_1" goto dbmaintain_delete
if "%opt%"=="9" goto dbmaintain_update
if "%opt%"=="8" goto integration_tests
if "%opt%"=="6_1" goto server_log_sg
if "%opt%"=="6_2" goto server_log_th
if "%opt%"=="6_3" goto server_log_my
if "%opt%"=="6" goto server_log_vm 
if "%opt%"=="5_3" goto deploy_my
if "%opt%"=="5_2" goto deploy_th 
if "%opt%"=="5_1" goto deploy_sg 
if "%opt%"=="5" goto deploy_vm 
if "%opt%"=="4_1" goto ui_deploy_sg
if "%opt%"=="4_2" goto ui_deploy_th
if "%opt%"=="4_3" goto ui_deploy_my
if "%opt%"=="4" goto ui_deploy_vm
if "%opt%"=="3" goto ui_build
if "%opt%"=="2" goto trs_build_no_tests
if "%opt%"=="1" goto trs_build
if "%opt%"=="0" goto exit
goto start

:exit
cls
exit

:login
title %VM_URL% Terminal
cls
ssh %VM_USER%@%VM_URL%
pause
goto start

:version 
cd %DEVELOPMENT_HOME%\transit
set /p v="Enter Version: "
mvn versions:set -DnewVersion=%v%
pause
goto start

:chown
ssh -t %VM_LOGIN% "sudo chown -R ubuntu /var/lib/docker/volumes"
pause
goto start

:checkdependencies
cd %DEVELOPMENT_HOME%\transit
mvn versions:display-property-updates
pause
goto start

:updatedependency
cd %DEVELOPMENT_HOME%\transit
set /p v="Enter Dependency to Update: "
mvn versions:update-property -Dproperty=%v%
pause
goto start


:gitbash  
cd %DEVELOPMENT_HOME%\transit
rem start C:\Windows\SysWOW64\cmd.exe /c "C:\Program Files\Git\git-bash.exe" 
start "Title : %DEVELOPMENT_HOME%" "%GIT_HOME%\git-bash.exe"
pause
goto start

:giteye
cd %GIT_EYE_HOME%
start GitEye.exe -clean
pause
goto start 

:ci
cd %DEVELOPMENT_HOME%\acts
call mvn clean verify -Dwebdriver.remote.url=http://%VM_URL%:4444/wd/hub -Dwebdriver.remote.driver=chrome -Dwebdriver.remote.os=WINDOWS
pause
goto start 


:acts-docker-compose_start
ssh %VM_LOGIN% "cd /home/ubuntu/iac; docker-compose start"
rem timeout 5 >nul
rem ssh %VM_LOGIN% "cd /home/ubuntu/iac/acts; docker-compose start"
pause
goto start

:acts-docker-compose_stop
ssh %VM_LOGIN% "cd /home/ubuntu/iac; docker-compose stop"
rem ssh %VM_LOGIN% "cd /home/ubuntu/iac/acts; docker-compose stop"
pause
goto start

:hfinish
cd %DEVELOPMENT_HOME%\transit
call mvn jgitflow:hotfix-finish -X
pause
goto start 

:hstart
cd %DEVELOPMENT_HOME%\transit
call mvn jgitflow:hotfix-start -X
pause
goto start 

:rstart
cd %DEVELOPMENT_HOME%\transit
call mvn jgitflow:release-start -X
pause
goto start 

:rstart-cmn-msg
cd %DEVELOPMENT_HOME%\cmn-message-spec
call mvn jgitflow:release-start -X
pause
goto start 

:rfinish
cd %DEVELOPMENT_HOME%\transit
call mvn jgitflow:release-finish -X
pause
goto start 

:rfinish-cmn-msg
cd %DEVELOPMENT_HOME%\cmn-message-spec
call mvn jgitflow:release-finish -X
pause
goto start 



:ffinish
cd %DEVELOPMENT_HOME%\transit
call mvn jgitflow:feature-finish
pause
goto start 


:fstart
cd %DEVELOPMENT_HOME%\transit
call mvn jgitflow:feature-start
pause
goto start 

:swagger
cd %DEVELOPMENT_HOME%\transit
call mvn clean install -DskipTests -Pswagger
pause
goto start 

:jcl_run
cd %DEVELOPMENT_HOME%\transit
call jvisualvm
pause
goto start 

:refnumclient_build
cd %DEVELOPMENT_HOME%\cmn-ref-num-client
call mvn clean install -U -DskipTests
pause
goto start 

:refnum_build
cd %DEVELOPMENT_HOME%\cmn-ref-num-gen
call mvn clean install -U -DskipTests
pause
goto start 

:acsn
cd %DEVELOPMENT_HOME%\acsn-gateway
call mvn clean install -U 
pause
goto start 

:gms_build
cd %DEVELOPMENT_HOME%\gms-guarantees
call mvn clean install -DskipTests
pause
goto start 

:cmn_build
cd %DEVELOPMENT_HOME%\cmn-message-spec
call mvn clean install
pause
goto start 

:cmn_decl
cd %DEVELOPMENT_HOME%\cmn-declaration
call mvn clean install -DskipTests
pause
goto start 

:db_populate_data
cd %DEVELOPMENT_HOME%\transit\integration-tests
call mvn clean install -DskipTests
call mvn -Dtest=PopulateDBData test
pause
goto start 

:integration_tests
 cd %DEVELOPMENT_HOME%\transit\integration-tests
rem cd %DEVELOPMENT_HOME%\transit\
call mvn clean install -U -X -Dtest=RegisterDeclarationIT
pause
goto start 



:dbmaintain_delete
rem cd %DBMAINTAIN_HOME%
rem call dbmaintain.bat clearDatabase
cd %DEVELOPMENT_HOME%\transit\rdbms 
call mvn org.dbmaintain:dbmaintain-maven-plugin:clearDatabase -X -P clearDatabase
pause
goto start 

:dbmaintain_update
cd %DEVELOPMENT_HOME%\transit\rdbms 
rem call %DBMAINTAIN_HOME%\dbmaintain.bat updateDatabase
call mvn org.dbmaintain:dbmaintain-maven-plugin:updateDatabase -X -P createDb
pause
goto start

rem 10. Migrate, 10_1. Clean, 10_2 Info, 10_3 Validate, 10_4 Baseline, 10_5 Repair 
:flyway_migrate
cd %DEVELOPMENT_HOME%\transit\transit-db 
call mvn flyway:migrate
pause
goto start

:flyway_clean
cd %DEVELOPMENT_HOME%\transit\transit-db 
call mvn flyway:clean
pause
goto start

:flyway_info
cd %DEVELOPMENT_HOME%\transit\transit-db  
call mvn flyway:info
pause
goto start

:flyway_validate
cd %DEVELOPMENT_HOME%\transit\transit-db 
call mvn flyway:validate
pause
goto start

:flyway_baseline
cd %DEVELOPMENT_HOME%\transit\transit-db 
call mvn compile flyway:baseline
pause
goto start

:flyway_repair
cd %DEVELOPMENT_HOME%\transit\transit-db 
call mvn flyway:repair
pause
goto start

:flyway_init
cd %DEVELOPMENT_HOME%\transit\transit-db 
call mvn flyway:init
pause
goto start

:export-db
cd %DEVELOPMENT_HOME%\transit
call mvn clean install -DskipTests  -Pdb
pause
goto start 


:dbmaintain_refnum_delete
cd %DEVELOPMENT_HOME%\cmn-ref-num-gen\rdbms 
call mvn org.dbmaintain:dbmaintain-maven-plugin:clearDatabase -X -P clearDatabase
pause
goto start 

:dbmaintain_refnum_update
cd %DEVELOPMENT_HOME%\cmn-ref-num-gen\rdbms 
call mvn org.dbmaintain:dbmaintain-maven-plugin:updateDatabase -X -P createDb
pause
goto start

:dbschema_export
rem     <!-- transit\domain-model - mvn -X hibernate3:hbm2ddl , in domain-model\target\hibernate3\sql-->    
cd %DEVELOPMENT_HOME%\transit\transit-web-api
call mvn -X hibernate3:hbm2ddl -e
pause
goto start



:ui_build
cd %DEVELOPMENT_HOME%\transit-ui 
rem call npm install
rem call bower install
call grunt build --force
pause
goto start 



:ui_deploy_vm 
ssh -p 22 %VM_USER%@%VM_URL% 'rm -r /var/lib/docker/volumes/iac_acts_static/_data/transit/*'
scp -r  %LINUX_DEVELOPMENT_HOME%/transit-ui/dist/* %VM_USER%@%VM_URL%:/var/lib/docker/volumes/iac_acts_static/_data/transit 
pause
goto start

:deploy_vm  
scp  -r   %LINUX_DEVELOPMENT_HOME%/transit/transit-web-api/target/transit-web-api-*.war %VM_USER%@%VM_URL%:/var/lib/docker/volumes/iac_wildfly_deployments/_data
rem cd %DEVELOPMENT_HOME%\transit
rem call mvn wildfly:undeploy -Ddeploy.force=true  -Dwildfly.artifactId.name=transit-web-api  -Dwildfly.deploy.hostname=%VM_URL%  -Dwildfly.deploy.port=9990  -Dwildfly.deploy.username=admin -Dwildfly.deploy.password=admin 

rem cd %DEVELOPMENT_HOME%\transit\transit-web-api
rem call mvn wildfly:deploy -Ddeploy.force=true  -Dwildfly.artifactId.name=transit-web-api -Dwildfly.deploy.hostname=%VM_URL%  -Dwildfly.deploy.port=9990 -Dwildfly.deploy.username=admin -Dwildfly.deploy.password=admin 

pause
goto start

:ui_deploy_sg
ssh -p 22 root@%SG_SERVER% 'rm -r /var/lib/docker/volumes/iaz_app_static/_data/transit/*'
scp -r  %LINUX_DEVELOPMENT_HOME%/transit-ui/dist/* root@%SG_SERVER%:/var/lib/docker/volumes/iaz_app_static/_data/transit
pause
goto start

:deploy_sg 
scp  -r   %LINUX_DEVELOPMENT_HOME%/transit/transit-web-api/target/transit-web-api-*.war root@%SG_SERVER%:/var/lib/docker/volumes/iaz_app_deployments/_data
rem  cd %DEVELOPMENT_HOME%\transit
rem call mvn wildfly:undeploy -Ddeploy.force=true  -Dwildfly.artifactId.name=transit-web-api  -Dwildfly.deploy.hostname=%SG_SERVER%  -Dwildfly.deploy.port=9991  -Dwildfly.deploy.username=admin -Dwildfly.deploy.password=admin 

rem cd %DEVELOPMENT_HOME%\transit\transit-web-api
rem call mvn wildfly:deploy -Ddeploy.force=true  -Dwildfly.artifactId.name=transit-web-api -Dwildfly.deploy.hostname=%SG_SERVER%  -Dwildfly.deploy.port=9991 -Dwildfly.deploy.username=admin -Dwildfly.deploy.password=admin 

pause
goto start

:ui_deploy_th
ssh -p 22 root@%TH_SERVER% 'rm -r /var/lib/docker/volumes/iaz_app_static/_data/transit/*'
scp -r  %LINUX_DEVELOPMENT_HOME%/transit-ui/dist/* root@%TH_SERVER%:/var/lib/docker/volumes/iaz_app_static/_data/transit
pause
goto start

:deploy_th  
scp  -r   %LINUX_DEVELOPMENT_HOME%/transit/transit-web-api/target/transit-web-api-*.war root@%TH_SERVER%:/var/lib/docker/volumes/iaz_app_deployments/_data
rem cd %DEVELOPMENT_HOME%\transit
rem call mvn wildfly:undeploy -Ddeploy.force=true  -Dwildfly.artifactId.name=transit-web-api  -Dwildfly.deploy.hostname=%TH_SERVER%  -Dwildfly.deploy.port=9991  -Dwildfly.deploy.username=admin -Dwildfly.deploy.password=admin 

rem cd %DEVELOPMENT_HOME%\transit\transit-web-api
rem call mvn wildfly:deploy -Ddeploy.force=true  -Dwildfly.artifactId.name=transit-web-api -Dwildfly.deploy.hostname=%TH_SERVER%  -Dwildfly.deploy.port=9991 -Dwildfly.deploy.username=admin -Dwildfly.deploy.password=admin 

pause
goto start

:ui_deploy_my
ssh -p 22 root@%MY_SERVER% 'rm -r /var/lib/docker/volumes/iaz_app_static/_data/transit/*'
scp -r  %LINUX_DEVELOPMENT_HOME%/transit-ui/dist/* root@%MY_SERVER%:/var/lib/docker/volumes/iaz_app_static/_data/transit 
pause
goto start

:deploy_my  
scp  -r   %LINUX_DEVELOPMENT_HOME%/transit/transit-web-api/target/transit-web-api-*.war root@%MY_SERVER%:/var/lib/docker/volumes/iaz_app_deployments/_data

rem cd %DEVELOPMENT_HOME%\transit
rem call mvn wildfly:undeploy -Ddeploy.force=true  -Dwildfly.artifactId.name=transit-web-api  -Dwildfly.deploy.hostname=%MY_SERVER%  -Dwildfly.deploy.port=9991  -Dwildfly.deploy.username=admin -Dwildfly.deploy.password=admin 

rem cd %DEVELOPMENT_HOME%\transit\transit-web-api
rem call mvn wildfly:deploy -Ddeploy.force=true  -Dwildfly.artifactId.name=transit-web-api -Dwildfly.deploy.hostname=%MY_SERVER%  -Dwildfly.deploy.port=9991 -Dwildfly.deploy.username=admin -Dwildfly.deploy.password=admin 

pause
goto start


:server_log_vm 
cd %DEVELOPMENT_HOME%\logs\vm
del *
scp  %VM_USER%@%VM_URL%:/var/lib/docker/volumes/iac_wildlfy_logs/_data/server.log %LINUX_DEVELOPMENT_HOME%/logs/vm
cd %DEVELOPMENT_HOME%\logs\vm
start "C:\Program Files\Notepad++\notepad++.exe" server.log
pause 
goto start 

:server_log_sg  
cd %DEVELOPMENT_HOME%\logs\sg
del * 
scp  root@%SG_SERVER%:/var/lib/docker/volumes/iaz_app_log/_data/server.log %LINUX_DEVELOPMENT_HOME%/logs/sg
rem ssh -p 22 wildfly@%SG_SERVER% 'scp  wildfly@%SG_SERVER%:/var/lib/docker/volumes/iaz_app_log/_data/server.log %LINUX_DEVELOPMENT_HOME%/logs/sg'
cd %DEVELOPMENT_HOME%\logs\sg
start "C:\Program Files\Notepad++\notepad++.exe" server.log
pause 
goto start

:server_log_th 
cd %DEVELOPMENT_HOME%\logs\th
del *
scp  root@%TH_SERVER%:/var/lib/docker/volumes/iaz_app_log/_data/server.log %LINUX_DEVELOPMENT_HOME%/logs/th
rem ssh -p 22 root@%TH_SERVER% 'scp  root@%TH_SERVER%:/var/lib/docker/volumes/iaz_app_log/_data/server.log %LINUX_DEVELOPMENT_HOME%/logs/th'
cd %DEVELOPMENT_HOME%\logs\th
start "C:\Program Files\Notepad++\notepad++.exe" server.log
pause 
goto start

:server_log_my 
cd %DEVELOPMENT_HOME%\logs\my
del *
scp  root@%MY_SERVER%:/var/lib/docker/volumes/iaz_app_log/_data/server.log %LINUX_DEVELOPMENT_HOME%/logs/my
rem ssh -p 22 root@%MY_SERVER% 'scp  root@%MY_SERVER%:/var/lib/docker/volumes/iaz_app_log/_data/server.log %LINUX_DEVELOPMENT_HOME%/logs/my'
cd %DEVELOPMENT_HOME%\logs\my
start "C:\Program Files\Notepad++\notepad++.exe" server.log
pause 
goto start


:trs_build
cd %DEVELOPMENT_HOME%\transit
call mvn clean install -U
pause
goto start 

:rds_build
cd %DEVELOPMENT_HOME%\rds-codelists
call mvn clean install -U
pause
goto start 

:trs_deploy_artifactory
cd %DEVELOPMENT_HOME%\transit
call mvn clean source:jar  deploy
pause
goto start

:trs_build_no_tests
cd %DEVELOPMENT_HOME%\transit
call mvn clean install -U -DskipTests
pause
goto start

:wildfly
title WildFly
call %JBOSS_HOME%\bin\standalone.bat -c standalone-full.xml
pause
goto start

:ui_deploy
rem rm -fr %JBOSS_HOME%\standalone\deployments\transit-ui
cd %DEVELOPMENT_HOME%\transit-ui\
call grunt serve 
rem xcopy /S /Y %DEVELOPMENT_HOME%\transit-ui\dist %JBOSS_HOME%\standalone\deployments\transit-ui
pause
goto start



:trs_deploy
cd %DEVELOPMENT_HOME%\transit\app
call mvn wildfly:deploy
pause
goto start

:web_api_deploy
cd %DEVELOPMENT_HOME%\transit\transit-web-api
call mvn wildfly:deploy
pause
goto start

:trs_undeploy
rem call %JBOSS_HOME%/bin/jboss-cli.bat --connect --controller=localhost:9990 --user=admin --password=admin123! --command="undeploy transit-app-1.0.0-SNAPSHOT.ear" 
rem call %JBOSS_HOME%/bin/jboss-cli.bat connect --controller=localhost:9990 --user=admin --password=admin123! --command="undeploy transit-app-1.0.0-SNAPSHOT.ear" 
cd %DEVELOPMENT_HOME%\transit\app
call mvn wildfly:undeploy
cd %JBOSS_HOME%\standalone\deployments\
rm -fr transit-app*.war
rm -fr transit-app*.war.*
pause
goto start

pause