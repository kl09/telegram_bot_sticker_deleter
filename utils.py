import requests
import json


class Request:
    def __init__(self, url: str = None):
        self.url = url
        self.result_data = None

    def get(self, params=None):
        self.result_data = requests.get(self.url, params)

        return self

    @property
    def result(self):
        return self.result_data

    @property
    def content(self):
        return json.loads(self.result_data.content.decode('utf-8')) if self.result_data.status_code is 200 else {}
