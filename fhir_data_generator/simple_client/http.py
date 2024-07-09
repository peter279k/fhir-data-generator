import json
import requests


class Http:
    def __init__(self, server_url):
        self.server_url = server_url
        self.headers = {
            'Accept': 'application/fhir+json',
            'Content-Type': 'application/fhir+json',
        }

    def send(self, path, http_method, headers, json_payload=None):
        for value in enumerate(headers):
            self.headers[value[1]] = headers[value[1]]

        headers = self.headers
        req_url = f'{self.server_url}{path}'

        requester = getattr(requests, http_method)

        if json_payload is None:
            response = requester(req_url, headers=headers)
        else:
            json_str = json.dumps(json_payload)
            response = requester(req_url, headers=headers, data=json_str)

        return response

    def handle_response(self, response):
        if hasattr(response, 'status_code') is False:
            raise AttributeError(f'Given response has invalid status_code attribute!')
        if hasattr(response, 'text') is False:
            raise AttributeError(f'Given response has invalid text attribute!')
        if hasattr(response, 'json') is False:
            raise AttributeError(f'Given response has invalid json attribute!')
        if callable(response.json) is False:
            raise TypeError(f'Given response has invalid json attribute!')

        handled_response = {
            'status': response.status_code,
            'text': response.text,
            'json': response.json(),
        }

        return handled_response
