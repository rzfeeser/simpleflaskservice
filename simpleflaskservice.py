#!/usr/bin/python3
"""Russell Zachary Feeser | Alta3 Research
   @rzfeeser              | https://alta3.com

GitHub:
https://github.com/rzfeeser/simpleflaskservice/README.md

Endpoints:
/env
/health
/info
/alta3
/talkingparrot
   ?say=Hello%20Parrot (say=string)
   
"""

import os
from time import sleep

from flask import Flask
from flask import request
from flask import jsonify

# Set the version of the Flask Server
VERSION = "0.1"
if os.getenv("VERSION") is not None:
    VERSION = os.getenv("VERSION")

# Set the port to listen on
PORT = 9876
if os.getenv("PORT0") is not None:
    PORT = os.getenv("PORT0")

# Set the HEALTH_DELAY
HEALTH_DELAY = 0
if os.getenv("HEALTH_DELAY") is not None:
    HEALTH_DELAY = os.getenv("HEALTH_DELAY")


app = Flask(__name__)


## Environmental Variables - /env
@app.route("/env")
def captain_planet():
    settings = { }
    settings["version"] = VERSION
    settings["env"] = {}
    settings["env"] = dict(os.environ) 
    return jsonify(settings)


## Health Status - /health
@app.route("/health")
def health():
    healthzee = {}
    healthzee["healthy"] = True
    healthzee["version"] = VERSION
    healthzee["delay in seconds"] = HEALTH_DELAY
    sleep(HEALTH_DELAY)               # wait this long in seconds
    return jsonify(healthzee)


## Info - /info
@app.route("/info")
def info():
    deepdive = {}
    deepdive["from"] = request.remote_addr  # the IP address of the requestor
    deepdive["host"] = request.host     # the IP:port of the flask server
    deepdive["version"] = VERSION
    return jsonify(deepdive)


## Talking Parrot - /talkingparrot?say=Hello%20Parrot
@app.route("/talkingparrot")
def talkingparrot():
    pollysays = {}
    # get value of "say", if not present, default ""
    pollysays["you"] = request.args.get("say", "")
    pollysays["parrot"] = f"SQUAWK!! {pollysays.get('you')}".rstrip() # remove ws if args.get returns empty
    pollysays["version"] = f"I am talking parrot version {VERSION}"
    # return JSON version of pollysays dictionary
    return jsonify(pollysays)


## Alta3 Research - /alta3
@app.route("/alta3")
def alta3():
    alta = {}
    alta["version"] = VERSION
    alta["thanks"] = "Thank you for training with Alta3 Research!"
    alta["alta3"] = {}
    alta["alta3"]["homepage"] = "https://alta3.com"
    alta["alta3"]["youtube"] = "https://www.youtube.com/user/Alta3Research/videos"
    alta["alta3"]["posters"] = "https://alta3.com/posters"
    return jsonify(alta)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
