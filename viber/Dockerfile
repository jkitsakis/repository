FROM ubuntu:16.04
#RUN apt-get update && apt-get install -y x11-apps


RUN apt-get update -y 
RUN apt-get install -y apt-transport-https ca-certificates krb5-locales libasn1-8-heimdal libcurl3-gnutls libffi6 libgmp10 libgnutls30 libgssapi-krb5-2 libgssapi3-heimdal libhcrypto4-heimdal libheimbase1-heimdal libheimntlm0-heimdal libhogweed4 libhx509-5-heimdal libidn11 libk5crypto3 libkeyutils1 libkrb5-26-heimdal libkrb5-3 libkrb5support0 libldap-2.4-2 libnettle6 libp11-kit0 libroken18-heimdal librtmp1 libsasl2-2 libsasl2-modules libsasl2-modules-db libsqlite3-0 libssl1.0.0 libtasn1-6  libwind0-heimdal openssl
RUN apt-get install -y libpulse0 libasound2 libnss3 libxcomposite1 libxcursor1 libxdamage1 libcurl3 libgstreamer-plugins-base1.0-0 libgstreamer1.0-0 gstreamer1.0-plugins-base libharfbuzz0b manpages-dev 
RUN apt-get install -y perl libxcb-render0 libxcb-shm0 libcairo2 libjack-jackd2-0 libtag1v5 libv4lconvert0 libpango-1.0-0 po-debconf libtwolame0 libxi6 libva1 libzvbi0 libsidplay1v5 libgraphite2-3 libgtk2.0-0 libxtst6 libass5 libxslt1-dev
RUN apt-get install -y gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly gstreamer1.0-pulseaudio gstreamer1.0-libav
RUN apt-get install -y libdv4 libdvdnav4 libbdplus0  libxss1 
RUN apt-get install -y libqt5gui5  module-init-tools

# install nvidia driver
RUN apt-get install -y binutils mesa-utils
ADD NVIDIA-Linux-x86_64-375.66.run /tmp/NVIDIA-Linux-x86_64-375.66.run
RUN sh /tmp/NVIDIA-Linux-x86_64-375.66.run -a -N --ui=none --no-kernel-module
RUN rm /tmp/NVIDIA-Linux-x86_64-375.66.run



COPY ./viber.deb /tmp/viber.deb
RUN dpkg -i /tmp/viber.deb  
RUN rm /tmp/viber.deb

ENV QT_XKB_CONFIG_ROOT=/usr/share/X11/xkb

# Set locale (fix locale warnings)
#RUN localedef -v -c -i en_US -f UTF-8 en_US.UTF-8 || true
#RUN echo "Europe/Athens" > /etc/timezone

# Set up the launch wrapper - sets up PulseAudio to work correctly
RUN echo 'export PULSE_SERVER="tcp:localhost:64713"' >> /usr/local/bin/viber-pulseaudio
RUN echo 'PULSE_LATENCY_MSEC=60 /opt/viber/Viber' >> /usr/local/bin/viber-pulseaudio
RUN chmod 755 /usr/local/bin/viber-pulseaudio


