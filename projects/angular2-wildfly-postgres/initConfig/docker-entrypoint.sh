#!/bin/sh
echo "----------- In docker-entrypoint.sh ------------"

cd $CONFIG_TEMP_DIR
echo "---> Printing $CONFIG_TEMP_DIR contents : " 
find . -type f \( -name "environment.ts" \) -exec sed -i 's/country/'"$SITE"'/g' {} \;
find . -type f \( -name "environment.ts" \) -exec sed -i 's/site_url/'"$APP_IP"'/g' {} \;
find . -type f \( -name "environment.ts" \) -exec sed -i 's/site_port/'"$APP_PORT"'/g' {} \;
find . -type f \( -name "environment.ts" \) -exec sed -i 's/a_url_ip/'"$A_URL_IP"'/g' {} \;
find . -type f \( -name "environment.ts" \) -exec sed -i 's/a_url_port/'"$A_URL_PORT"'/g' {} \;
find . -type f \( -name "environment.ts" \) -exec sed -i 's/tim_format/'"$TIME_FORMAT"'/g' {} \;
find . -type f \( -name "environment.ts" \) -exec sed -i 's/dat_format/'"$DATE_FORMAT"'/g' {} \;
find . -type f \( -name "environment.ts" \) -exec sed -i 's/keycloak_loc/'"$KEYCLOAK_LOC"'/g' {} \;

vi environment.ts \;
