#!/bin/sh
echo "----------- In docker-entrypoint.sh ------------"

cd $APP_DIR
echo "---> Printing $APP_DIR contents : " 
ls

cd $APP_DIR/src/environments
echo "---> Printing $APP_DIR/src/environments contents : " 
ls

#echo "Clearing existing environment.ts files"
#rm -rf $APP_DIR/app_config/* 
#
#echo "Clearing existing environment.ts files"
#rm -rf $APP_DIR/src/environments/* 
#
#echo "Copying configuration..."
#cp -rf $CONFIG_TEMP_DIR/* $APP_DIR/app_config/
#
#echo "Copying to APP_DIR..."
#cd $APP_DIR/app_config/
#find . -name "environment.ts" -exec cp {} ../src/environments/ \;
#
#echo "listing  APP_DIR..."
#cd  $APP_DIR
#ls
#
#echo "listing  APP_DIR/src/environments/..."
#cd  $APP_DIR/src/environments/
#ls
#
#echo "listing  / "
#cd /