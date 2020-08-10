# This base image container is avail on hub.docker.com
# it has python 3.7 avail on Alpine Linux, a minimalist Linux distro
FROM python:alpine3.7
COPY . /app
WORKDIR /app
# Use Python package installer to install the Flask library to our image
RUN pip install -r requirements.txt
# container is exposed on port 9876
EXPOSE 9876
CMD python ./simpleflaskservice.py
