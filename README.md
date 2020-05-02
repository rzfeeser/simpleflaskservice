# simpleflaskservice

This repo provides a simple Python-Flask Server with several RESTful APIs for learning and testing. I created it to learn about running containers within Pods in Kubernetes, but could be used to test across many orchestrated environments. Deployed on a virtual machine, or baremetal, it could be a useful tool demonstrating HTTP connectivity.  

The current release of this code is also available as a containerized image on https://hub.docker.io/.  

Alternatively, this code can easily be transformed into a docker image following the steps included in this repo. Steps on deploying code found in this repository can be found at the bottom of the README file.

## simpleflaskserver 0.1 API endpoints

### /env [0.1]

### /health [0.1]

### /info [0.1]

### /talkingparrot/[ANYTHING] [0.1]
Returns a 200 containing the [ANYTHING] string sent to the API endpoint.


## How to transform this code into a Docker Image

0. Install docker and have it working to the point where you can launch containers. Instructions to do this are outside the scope of this README.md, but refer to https://docker.io for instructions on getting up and running.

0. git clone the repository to your local machine.



## Running the Docker Image

## How to Deploy this Image on Kubernetes

0. Create the following manifest.

## Deploying on Bare Metal

0. Clone the repository to your local machine

0. 
