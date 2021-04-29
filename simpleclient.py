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

SVRADDRESS = "http://0.0.0.0:9876"

import requests


def main():
    """interactions with defined endpoints"""
    for endpoint in ["env", "health", "info", "alta3"]:
        r = requests.get(f"{SVRADDRESS}/{endpoint}")
        assert r.status_code == 200


    r = requests.get(f"{SVRADDRESS}/talkingparrot?say=Hello%20Parrot")
    assert r.status_code == 200

if __name__ == "__main__":
    main()
