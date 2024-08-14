from fixtures.keycloak_config import *


def test_send(client_secret, client_credential_class):
    assert client_secret is not False

    client_credential_class.client_secret = client_secret
    client_credential_class.send()

    access_token = client_credential_class.retrieve_token()

    assert type(access_token) is str
