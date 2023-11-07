docker-compose up -d --build

1. connect to docker

docker exec -it sage-container /bin/bash

2. status and start ssh
sudo service ssh status
sudo service ssh start

3. Run the pdflatex 
cd ../texfiles
pdflatex filename.tex

4. Run abiword
abiword --to=tex filename.pdf