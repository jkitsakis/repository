CREATE USER acts WITH PASSWORD 'acts';

CREATE DATABASE keycloak ; 
GRANT ALL PRIVILEGES ON DATABASE keycloak TO acts;

CREATE DATABASE transit ;
GRANT ALL PRIVILEGES ON DATABASE transit TO acts;
