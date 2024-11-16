# Dockerfile
FROM rocker/rstudio:latest

# Install any necessary R libraries here
RUN R -e "install.packages(c('dplyr', 'ggplot2', 'tidyverse'), repos='http://cran.rstudio.com/')"

# Install system dependencies (if required)
RUN apt-get update && \
    apt-get install -y \
    libxml2-dev \
    libcurl4-openssl-dev \
    libssl-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*



# Expose port for RStudio
EXPOSE 8787

CMD ["/init"]
