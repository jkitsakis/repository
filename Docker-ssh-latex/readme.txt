1. connect to docker

docker exec -it sage-container /bin/bash

2. status and start ssh
sudo service ssh status
sudo service ssh start

3. Run the pdflatex 
cd ../texfiles
pdflatex your_document.tex