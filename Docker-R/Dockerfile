# Dockerfile
FROM rocker/rstudio:latest



# Install system dependencies (if required)
RUN apt-get update && \
    apt-get install -y \
    libxml2-dev \
    libcurl4-openssl-dev \
    libssl-dev \
	tcl8.6 tk8.6 libtcl8.6 libtk8.6 tk-dev  && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install any necessary R libraries here
RUN R -e "install.packages(c('dplyr', 'caret', 'e1071', 'ggplot2', 'tidyverse'), repos='https://cloud.r-project.org')"

#RUN mkdir -p /home/rstudio && \
#    chown -R rstudio:rstudio /home/rstudio
	
# Expose port for RStudio
EXPOSE 8787

CMD ["/init"]
