# simpleflaskservice

![rzfeeser-simpleflaskservice](https://raw.githubusercontent.com/rzfeeser/simpleflaskservice/9120566295df958912f2eb97860175a2fb2a9bd1/images/rzfeeser-simpleflaskservice.png)

This repo provides a simple Python-Flask Server with several RESTful APIs for learning and testing. I created it to learn about running containers within Pods in Kubernetes, but could be used to test across many orchestrated environments. Deployed on a virtual machine, or baremetal, it could be a useful tool demonstrating HTTP connectivity.  

The current release of this code can be deployed from the GitHub Container Repository (GHCR): [https://github.com/rzfeeser/simpleflaskservice/pkgs/container/simpleflaskservice](https://github.com/rzfeeser/simpleflaskservice/pkgs/container/simpleflaskservice)

Alternatively, this code can easily be transformed into a docker image following the steps included in this repo. Steps on deploying code found in this repository can be found at the bottom of the README file.

## simpleflaskserver 0.1 API endpoints 

### /env [0.1]

        HTTP/1.1 200 OK
        $HTTP_HEADERZ
         {
             "env": # dump of available environmental variables,
             "version": $VERSION
         }


### /health [0.1]

        HTTP/1.1 200 OK
        $HEADER_FIELDS
         {
             "delay in seconds": $HEALTH_DELAY,
             "version": $VERSION,
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
                     "posters": "https://alta3.com/posters",
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


By setting the following environment variables, you can change the runtime behaviour of simpleservice:

    - PORT0 - the port simpleservice is serving on
    - VERSION - the value of version returned in the JSON response of the /endpoint0 endpoint
    - HEALTH_DELAY - delay in milliseconds that the /health endpoint responds

## How to Run this Code

1. First, `git clone` the repository to your local machine.

   `git clone https://github.com/rzfeeser/simpleflaskservice`

0. Ensure Python 3.6+ has been installed on Debian / Ubuntu Machines

    `sudo apt install python3-pip`

0. Ensure Python 3.6+ has been installed, then use `pip` to install Flask.

   `python3 -m pip install flask`

0. Run the code with Python 3.6+

    `python3 simpleflaskservice.py`
        
0. Set the environmental variable `VERSION` to "24601" and `PORT0` to "8887", then launch the server.

    `VERSION=24601 PORT0=8887 python3 simpleflaskservice.py`

## How to Deploy on Docker

1. First build an image.

    `sudo docker build -t simpleservice -f Dockerfile .`

0. Launch the image in docker with the port `9010` pointing to `9876`, and without hogging up the screen (`-d`).

    `docker run -d -p 9010:9876 simpleflaskservice`

0. **OR** Launch the image in docker with a random port pointing to the exposed ports.

    `docker run -P simpleflaskservice`

## Deploy from GitHub Container Repository (GHCR)

1. Launch the image in docker with the port `9010` pointing to `9876`, and without hogging up the screen (`-d`)

    `docker run -d -p 9010:9876 ghcr.io/rzfeeser/simpleflaskservice:sha256-f1ce1835b0d4492a22447ac9243decbf0928605f4a71fb29ad2fd506144261a1`
