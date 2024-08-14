from fixtures.simple_client import *


def test_http_instance(http_class):
    assert http_class.server_url == 'https://hapi.fhir.tw/fhir'
