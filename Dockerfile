# This base image container is avail on hub.docker.com
# it has python 3.7 avail on Alpine Linux, a minimalist Linux distro
FROM python:alpine3.7

MAINTAINER Russell Zachary Feeser "RZFeeser@alta3.com"

COPY ./requirements.txt /var/www/requirements.txt

# Use Python package installer to install the Flask library to our image
RUN pip install -r /var/www/requirements.txt

# container is exposed on port 9876
EXPOSE 9876

CMD ["python", "./simpleflaskservice.py"]
