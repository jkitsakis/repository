FROM ubuntu:20.04


#Post installations for Ubuntu
ENV TZ=Europe/Athens
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && apt-get install -y tzdata sudo openssh-server nano

# Install additional tools like LaTeX, Jupyter Notebook, and Pandoc
RUN apt-get update && apt-get install -y sagemath texlive-latex-base texlive-xetex \
    texlive-fonts-recommended texlive-fonts-extra texlive-lang-greek \
    jupyter-notebook pandoc abiword wkhtmltopdf && apt-get clean

RUN apt-get clean 

# Create a non-root user
RUN useradd -m -s /bin/bash dockeruser
RUN echo "dockeruser:dockeruser" | chpasswd && adduser dockeruser sudo


# Expose necessary ports
EXPOSE 8888
EXPOSE 22

# Set user and working directory
USER dockeruser
WORKDIR /home/dockeruser
