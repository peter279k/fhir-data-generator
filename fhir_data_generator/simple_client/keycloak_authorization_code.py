import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlsplit, parse_qs, urlencode


class AuthorizationCode:
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, req_auth_code_url: str, access_token_req_url: str, form_action_payload: dict):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.grant_type = 'authorization_code'
        self.scope = 'openid'
        self.response_type = 'code'
        self.req_auth_code_url = req_auth_code_url
        self.access_token_req_url = access_token_req_url
        self.authorization_code = None
        self.req_session = None
        self.response = None
        self.req_auth_code_headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        self.auth_code_headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
        }
        self.form_action_payload = form_action_payload

        if form_action_payload.get('username') is None:
            raise Exception('username is not found in the form_action_payload!')
        if form_action_payload.get('password') is None:
            raise Exception('password is not found in the form_action_payload!')

    def retrieve_authorization_code(self):
        req_session = requests.Session()

        encoded_query = urlencode(
            {
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'scope': self.scope,
                'response_type': self.response_type,
                'redirect_uri': self.redirect_uri,
            }
        )

        req_auth_code_url = f'{self.req_auth_code_url}?{encoded_query}'
        response = req_session.get(req_auth_code_url)

        if response.ok is False:
            return response.json()

        time.sleep(1)
        soup = BeautifulSoup(response.text, 'html.parser')
        form_action = soup.select_one('form')

        if form_action.get('action') is None:
            raise Exception('Retrieving form action URL is failed')

        form_action_url = form_action['action']
        response = req_session.post(form_action_url, headers=self.req_auth_code_headers, data=self.form_action_payload, allow_redirects=False)

        if response.headers.get('Location') is None:
            raise Exception('Location header is not found')

        parsed_url = urlsplit(response.headers['Location'])
        parsed_query = parse_qs(parsed_url.query)

        if parsed_query.get('code') is None or len(parsed_query['code']) < 1:
            raise Exception('code param is not found')

        authorization_code = parsed_query['code'][0]
        self.authorization_code = authorization_code
        self.req_session = req_session

        return authorization_code

    def send(self):
        payload = urlencode(
            {
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'code': self.authorization_code,
                'redirect_uri': self.redirect_uri,
                'grant_type': self.grant_type,
            }
        )

        response = self.req_session.post(self.access_token_req_url, headers=self.auth_code_headers, data=payload, allow_redirects=False)
        self.response = response

        return response

    def retrieve_token(self):
        if self.response.status_code != 200:
            raise Exception(f'The response status code is {self.response.status_code}')

        return self.response.json().get('access_token')
