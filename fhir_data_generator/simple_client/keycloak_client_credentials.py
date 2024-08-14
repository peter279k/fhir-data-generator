import requests
from urllib.parse import urlencode


class ClientCredentials:
    def __init__(self, client_id: str, client_secret: str, req_url: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = 'client_credentials'
        self.scope = 'openid'

        self.req_url = req_url

        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }

        self.response = None

    def send(self):
        payload = f'client_id={self.client_id}&client_secret={self.client_secret}&grant_type={self.grant_type}&scope={self.scope}'

        response = requests.post(self.req_url, headers=self.headers, data=payload)
        self.response = response

        return response

    def retrieve_token(self):
        print(self.response.text)
        if self.response.status_code != 200:
            raise Exception(f'The response status code is {self.response.status_code}')

        return self.response.json().get('access_token')
