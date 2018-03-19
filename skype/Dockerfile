FROM ubuntu:16.04 
#RUN apt-get update && apt-get install -y x11-apps


RUN dpkg --add-architecture i386
#RUN echo "deb http://archive.canonical.com/ubuntu maverick partner" >> /etc/apt/sources.list 
RUN apt-get update && apt-get -fy install apt-transport-https tzdata gconf-service libatk1.0-0 libcairo2 libcups2 libfontconfig1 libfreetype6 libgconf-2-4 libgdk-pixbuf2.0-0 libgtk2.0-0
RUN apt-get update && apt-get -fy install libasound2 libnspr4 libnss3 libsecret-1-0 libx11-xcb1 libxss1 libxtst6
RUN apt-get update && apt-get -fy install pulseaudio
COPY ./skypeforlinux-64.deb /tmp/skypeforlinux-64.deb

RUN dpkg -i /tmp/skypeforlinux-64.deb  
RUN rm /tmp/skypeforlinux-64.deb
	

RUN echo "Europe/Athens" > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata


