import pytest
from fhir_data_generator import SimpleClient


@pytest.fixture
def http_class():
    return SimpleClient('https://hapi.fhir.tw/fhir')
