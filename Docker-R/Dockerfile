# Dockerfile
FROM rocker/rstudio:latest

# Set working directory
WORKDIR /home/rstudio

# Install system dependencies (if required)
RUN apt-get update && \
    apt-get install -y \
    libxml2-dev \
    libcurl4-openssl-dev \
    libssl-dev

RUN apt-get clean && rm -rf /var/lib/apt/lists/*


# Install any necessary R libraries here
RUN R -e "install.packages(c('dplyr', 'caret', 'e1071', 'ggplot2', 'tidyverse'), repos='https://cloud.r-project.org')" && rm -rf /var/lib/apt/lists/*

	
# Expose port for RStudio
EXPOSE 8787

CMD ["/init"]