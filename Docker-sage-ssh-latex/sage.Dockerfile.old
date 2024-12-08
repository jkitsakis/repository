# Use Ubuntu as the base image
FROM ubuntu:latest

# Create a non-root user
RUN useradd -m -s /bin/bash dockeruser

#Post installations for Ubuntu
ENV TZ=Europe/Athens
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && apt-get install -y tzdata sudo openssh-server nano


# Install required packages
RUN apt-get update && apt-get install -y sagemath jupyter-notebook pandoc abiword wkhtmltopdf

# Install pdflatex and other necessary latex tools
RUN apt-get update && apt-get install -y texlive-latex-base texlive-xetex texlive-fonts-recommended texlive-fonts-extra texlive-lang-greek

# Install abiword to convert pdf-> tex 
# RUN apt-get update && apt-get install -y abiword

RUN apt-get clean 

# Set up a non-root user for running Jupyter Notebook and add user to sudo
RUN echo "dockeruser:dockeruser" | chpasswd && adduser dockeruser sudo

# Expose the Jupyter Notebook port
EXPOSE 8888

# Expose port 22 and start sshd
EXPOSE 22

# Configure SSH server
RUN mkdir /var/run/sshd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config


CMD ["/usr/sbin/sshd", "-D"]

USER dockeruser

# Create a working directory
RUN mkdir /home/dockeruser/pandoc
# Set a working directory for LaTeX files
RUN mkdir /home/dockeruser/texfiles
# Create a working directory
WORKDIR /home/dockeruser/notebooks
