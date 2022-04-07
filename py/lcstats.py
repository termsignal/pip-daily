#!/usr/bin/python3
from dataclasses import field
import os
import sys
import requests
import json
import AppKit

def get():
    client = requests.get("https://leetcode-stats-api.herokuapp.com/donisidro323")
    return client.text


def parse(jsonpayload, field):
    json_obj = json.loads(jsonpayload)
    # os.environ["totalSolved"] = str(json_obj['totalSolved'])
    # os.environ["easySolved"] = json_obj["easySolved"]
    # os.environ["mediumSolved"] = json_obj["mediumSolved"]
    # os.environ["hardSolved"] = json_obj["hardSolved"]
    # os.environ["acceptanceRate"] = json_obj["acceptanceRate"]
    # os.environ["ranking"] = json_obj["ranking"]
    return json_obj[field]

def main():    
    payload = get()
    value = parse(payload, sys.argv[1])
    # sys.stdout.write(value)
    print(value)
    AppKit.NSBeep()



if __name__ == '__main__':
    main()