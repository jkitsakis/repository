# Use the official Ubuntu base image
FROM ubuntu:20.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV DISPLAY=host.docker.internal:0

# Update the package list and install required packages
RUN apt-get update && apt-get install -y \
    openjdk-11-jdk \
    wget \
    xauth \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Download and install Weka
RUN wget https://downloads.sourceforge.net/project/weka/weka-3-9/3.9.6/weka-3-9-6-azul-zulu-linux.zip
RUN apt-get install -y unzip
RUN unzip weka-3-9-6-azul-zulu-linux.zip -d /opt
RUN rm weka-3-9-6-azul-zulu-linux.zip

# Set up environment variables for Weka
ENV WEKA_HOME /opt/weka-3-9-6
ENV PATH $WEKA_HOME:$PATH

# Copy a script to run Weka
COPY run_weka.sh /usr/local/bin/run_weka.sh
RUN chmod +x /usr/local/bin/run_weka.sh

# Expose necessary ports (if needed, for VNC)
#EXPOSE 5900

# Entry point to run Weka
ENTRYPOINT ["/usr/local/bin/run_weka.sh"]
