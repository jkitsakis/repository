#!/bin/bash

# Set the display to use the host's X server
export DISPLAY=${DISPLAY:-:0}

# Start Weka
java -jar /opt/weka-3-9-6/weka.jar
