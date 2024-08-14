from fixtures.keycloak_config import *


def test_send(client_secret, authorization_code_class):
    assert client_secret is not False

    authorization_code_class.client_secret = client_secret
    authorization_code = authorization_code_class.retrieve_authorization_code()

    assert type(authorization_code) is str

    authorization_code_class.send()

    access_token = authorization_code_class.retrieve_token()

    assert type(access_token) is str
