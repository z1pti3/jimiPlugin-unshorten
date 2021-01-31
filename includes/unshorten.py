import requests
import json
from pathlib import Path

class _unshorten():
    url = "https://unshorten.me"
    
    def __init__(self, ca=None, requestTimeout=30):
        self.requestTimeout = requestTimeout
        if ca:
            self.ca = Path(ca)
        else:
            self.ca = None

    def apiCall(self,endpoint,methord="GET",data=None):
        kwargs={}
        kwargs["timeout"] = self.requestTimeout
        if self.ca:
            kwargs["verify"] = self.ca
        try:
            if methord == "GET":
                response = requests.get("{0}/{1}".format(self.url,endpoint), **kwargs)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            return 0, "Connection Timeout"
        if response.status_code == 200:
            return json.loads(response.text), response.status_code
        return response.text, response.status_code

    def unshortenURL(self,url):
        response, statusCode = self.apiCall("json/{0}".format(url))
        return response, statusCode
