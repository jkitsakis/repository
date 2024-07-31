#Build and start
docker-compose up -d --build

# Remove unused data
docker system prune --all --volumes

# Remove all services
docker service rm $(docker service ls -q)

# Remove all containers
docker rm -f $(docker ps -aq)

# Remove all images
docker rmi -f $(docker images -aq)

# Remove all volumes
docker volume rm $(docker volume ls -q)

#Print the name of the current context
docker context show

# List contexts
docker context ls

# Remove one or more contexts
docker context rm CONTEXT 

# Connect to docker
docker exec -it sage-container /bin/bash

# status and start ssh
sudo service ssh status
sudo service ssh start


#run 
xhost + # Allow connections from the Docker container
docker-compose up --build
xhost - # Disable connections from the Docker container after usage


---------------------------------------------
Compact Docker Desktop WSL 2 VM to free up space
diskpart docker volume (execute in cmd line by line ) :
------ 
wsl --shutdown
diskpart
select vdisk file="C:\Users\jkits\AppData\Local\Docker\wsl\data\ext4.vhdx"
attach vdisk readonly
compact vdisk
detach vdisk
exit

---------------
automatically shrink the image when files are removed
-------
wsl --manage docker-desktop-data --set-sparse true
-----------------------------------------------




