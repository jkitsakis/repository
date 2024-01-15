# setting base image
FROM jupyter/scipy-notebook

# get necessary python modules
RUN pip install scikit-surprise
