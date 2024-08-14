import os
import pytest
from urllib.parse import urlencode
from fhir_data_generator import ClientCredentials, AuthorizationCode


@pytest.fixture
def client_secret():
    client_secret_path = './tests/fixtures/client_secret.txt'
    if os.path.isfile(client_secret_path) is True:
        with open(client_secret_path, mode='r', encoding='utf-8') as f:
            contents = f.read()

        the_client_secret = contents[0:-1]

        return the_client_secret

    return False

@pytest.fixture
def client_credential_class():
    client_id = 'admin-cli'
    client_secret = ''
    req_url = 'http://localhost:8080/realms/master/protocol/openid-connect/token'
    client_credentials = ClientCredentials(client_id, client_secret, req_url)

    return client_credentials

@pytest.fixture
def authorization_code_class():
    client_id = 'admin-cli'
    client_secret = ''
    redirect_uri = 'http://redirect.uri'
    req_auth_code_url = 'http://localhost:8080/realms/master/protocol/openid-connect/auth'
    access_token_req_url = 'http://localhost:8080/realms/master/protocol/openid-connect/token'
    form_action_payload = {
        'username': 'admin',
        'password': 'admin',
    }
    authorization_code = AuthorizationCode(client_id, client_secret, redirect_uri, req_auth_code_url, access_token_req_url, form_action_payload)

    return authorization_code
