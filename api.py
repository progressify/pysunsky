import hashlib
from configparser import ConfigParser

import requests


class OpenApiService:

    def __init__(self, config_path='./'):
        config = ConfigParser()
        config.read(f'{config_path}config.ini')
        self.key = config["SUNSKY"]["key"]
        self.secret = config["SUNSKY"]["secret"]

    def call(self, api_url, a_parameters):
        a_parameters['signature'] = self.sign(a_parameters)
        r = requests.post(api_url, data=a_parameters)
        return r.text

    def download(self, api_url, a_parameters, path):
        a_parameters['signature'] = self.sign(a_parameters)
        r = requests.post(api_url, data=a_parameters)
        with open(path, 'wb') as file:
            file.write(r.content)

    def sign(self, a_parameters):
        signature = ''
        a_parameters['key'] = self.key
        for item in self.__ksort(a_parameters):
            signature += item[1]

        signature = f'{signature}@{self.secret}'
        m = hashlib.md5(signature.encode('utf-8'))
        return m.hexdigest()

    def __ksort(self, d):
        return [(k, d[k]) for k in sorted(d.keys())]
