#!/usr/bin/env python3
import json
import requests

r = requests.get("https://my.hypervisor.us/api/v1/guests/running", headers={ "Authentication": "whatever" })

print(json.dumps(r.json()))
