import urllib.request
import json


def open_url(url, data=None, header=None):
    req = urllib.request.Request(url, data, header)
    response = urllib.request.urlopen(req)
    response_text = response.read().decode()
    #
    return json.loads(response_text)



