# simpleflaskservice

This repo provides a simple Python-Flask Server with several RESTful APIs for learning and testing. I created it to learn about running containers within Pods in Kubernetes, but could be used to test across many orchestrated environments. Deployed on a virtual machine, or baremetal, it could be a useful tool demonstrating HTTP connectivity.  

The current release of this code is also available as a containerized image on https://hub.docker.io/.  

Alternatively, this code can easily be transformed into a docker image following the steps included in this repo. Steps on deploying code found in this repository can be found at the bottom of the README file.

## simpleflaskserver 0.1 API endpoints

### /env [0.1]

        HTTP/1.1 200 OK
        $HTTP_HEADERZ
         {
             "env": "$DUMP_OF_ENVIRONMENT_VARS",
             "version": "$VERSION"
         }


### /health [0.1]

        HTTP/1.1 200 OK
        $HEADER_FIELDS
         {
             "healthy": true
         }


### /info [0.1]

        HTTP/1.1 200 OK
        $HTTP_HEADERZ
         {
             "from": "$REMOTE_IP",
             "host": ""$HOST:$PORT"",
             "version": "$VERSION"
         }


### /alta3 [0.1]

        HTTP/1.1 200 OK
        $HTTP_HEADERZ
         {
             "thanks": "Thank You for training with Alta3 Research!",
             "alta3":
                 {
                     "homepage": "https://alta3.com",
                     "youtube": "https://www.youtube.com/user/Alta3Research/videos"
                 },
             "version": "$VERSION"
         }


### /talkingparrot/?say=[ANYTHING] [0.1]
Returns a 200 containing a "SQUAKK!!" + the [ANYTHING] string sent to the API endpoint.

        HTTP/1.1 200 OK
        $HTTP_HEADERZ
         {
             "you": "Polly want a cracker?",
             "parrot": "SQUAWK!! Polly want a cracker?",
             "version": "I am talking parrot version $VERSION"
         }


## How to transform this code into a Docker Image

0. Install docker and have it working to the point where you can launch containers. Instructions to do this are outside the scope of this README.md, but refer to https://docker.io for instructions on getting up and running.

0. git clone the repository to your local machine.



## Running the Docker Image

## How to Deploy this Image on Kubernetes

0. Create the following manifest.

## Deploying on Bare Metal

0. Clone the repository to your local machine

0. 
