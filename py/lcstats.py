#!/usr/bin/python3
from dataclasses import field
import os
import sys
import requests
import json
import AppKit

def get():
    call_endpoint = "https://leetcode-stats-api.herokuapp.com/" + os.getenv('LCUSERNAME')
    client = requests.get(call_endpoint)
    return client.text


def parse(jsonpayload, field):
    json_obj = json.loads(jsonpayload)
    return json_obj[field]

def main():    
    payload = get()
    value = parse(payload, sys.argv[1])
    # sys.stdout.write(value)
    print(value)
    AppKit.NSBeep()



if __name__ == '__main__':
    main()