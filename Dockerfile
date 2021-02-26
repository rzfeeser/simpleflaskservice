# This base image container is avail on hub.docker.com
# it has python 3.7 avail on Alpine Linux, a minimalist Linux distro
FROM python:alpine3.7

MAINTAINER Russell Zachary Feeser "RZFeeser@alta3.com"

# copy the file requirements.txt into the image /var/www/requirements.txt
COPY . /var/www/

# set a relative working directory inside our container image
WORKDIR /var/www/

# Use Python package installer to install the Flask library to our image
RUN pip install -r /var/www/requirements.txt

# container is exposed on port 9876
EXPOSE 9876

CMD ["python", "./simpleflaskservice.py"]
