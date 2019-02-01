import requests

class connect_http:

    def __init__(self):
        pass


    def get(self, url, method, request=None):
        req = requests
        res = req.request(method,url, request=request)
        return res.json()



