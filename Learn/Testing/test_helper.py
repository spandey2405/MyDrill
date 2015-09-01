__author__ = 'spandey2405'

import requests
import json
import sys
def ping(hostname):
    import os
    response = os.system("ping6 -c 1 -W 2 " + hostname + " > /dev/null 2>&1")

    if response == 0:
        return "True"
    else:
        return "False"

def get_data(BR,endpoint):
    url = "http://"+BR+endpoint
    try:
        print "Connecting to BR : ",url
        data = hit_url(url)
    except:
        print "Border Router Not Connected"
        sys.exit(0)
    return data

def hit_url(url):
    response = requests.get(url, timeout=1)
    graph_motes = json.loads(response.text)
    return graph_motes['routes']

