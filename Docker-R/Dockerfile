# Use the rocker/rstudio base image
FROM rocker/rstudio:latest

# Set environment variables
ENV PASSWORD=rstudio
ENV USER=rstudio

# Expose RStudio server port
EXPOSE 8787

# Set working directory (optional)
WORKDIR /home/$USER

# Run RStudio as the specified user
CMD ["/init"]
