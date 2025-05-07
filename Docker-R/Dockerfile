FROM rocker/rstudio:latest

# Optional: Set user and root access explicitly
ENV PASSWORD=rstudio
ENV ROOT=TRUE

# Make sure home directory exists with correct permissions
RUN mkdir -p /home/rstudio && \
    chown rstudio:rstudio /home/rstudio

# Install R packages
RUN R -e "install.packages(c('dplyr', 'caret', 'e1071', 'ggplot2', 'tidyverse'), repos='https://cloud.r-project.org')"

EXPOSE 8787


