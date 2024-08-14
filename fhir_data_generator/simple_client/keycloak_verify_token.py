import requests


class VerifyToken:
    def __init__(self, req_url: str, client_id: str, access_token: str):
        self.req_url = req_url
        self.headers = {'client_id': client_id, 'Authorization': f'Bearer {access_token}'}

    def is_verified(self):
        response = requests.get(self.req_url, headers=self.headers)

        return response.ok
