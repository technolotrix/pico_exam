import json
import time
import requests

url = 'https://api.staging.pico.tools/loader/guest'


class APIClient():

    def __init__(self, json_headers=False):
        self.json_content = "application/json"
        self.form_content = "application/x-www-form-urlencoded"

        self.headers = {"Accept": "application/json"}
        self.headers["Content-Type"] = self.json_content if json_headers == True else self.form_content

    def make_request(self, verb, url, data, timeit=False):
        r = requests.request
        kwargs = {
            "headers": self.headers,
            #"verify": False
            }

        if verb == "GET":
            kwargs["params"] = data
        elif self.headers["Content-Type"] == self.form_content:
            kwargs["data"] = data
        else:
            kwargs["data"] = json.dumps(data)

        start = time.time()
        response = r(verb, url, **kwargs)
        end = time.time()

        if timeit:
            delta = end - start
            return delta
        return response
