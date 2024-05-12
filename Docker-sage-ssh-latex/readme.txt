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

#Remove one or more contexts
docker context rm CONTEXT 


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



1. connect to docker

docker exec -it sage-container /bin/bash

2. status and start ssh
sudo service ssh status
sudo service ssh start

3. Run the pdflatex 
cd ../texfiles


4. Run abiword
abiword --to=tex filename.pdf

5.  Convert tex to pdf 
pdflatex Quiz3-question7.tex


matrix code :  $C=\begin{bmatrix} -2 & 1 & -1 \\ 1 & -2 & 1 \\ -1 & 1 & -2 \end{bmatrix}$
thita expression: Given $z=e^{−y}sin(x)$ the expression $∂^2z / ∂x^2 + ∂^2z/∂y^2 $ equals
upper arrow: $f_1(overrightarrow{x})
(in a sagemath markdown cell).


$ ∂^2z / ∂x^2 + ∂^2z/∂y^2 $

To create latex :
1. ask ChatGPT to provide latex code
2. copy code in notepad++
3. replace 
   \( -> $
   \) -> $
   \[ -> $
   \] -> $
   \$ -> $
   \^{} -> ^
   &= -> =
   \begin{align*} -> DELETE
   \end{align*} -> DELETE
   ---------
   $
					
  \begin{bmatrix}
  
  -> $ \begin{bmatrix}
  
  -------
   \end{bmatrix}
					
  $
  
  -> \end{bmatrix}  $
  ----------------
  \right\textbar{} -> DELETE
  \sum\emph{\{i=1\}^\{3\}} - >  \sum_{i=1}^{3}

4. In case of error type "end"