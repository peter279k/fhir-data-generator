import pytest
from fhir_data_generator import Http


@pytest.fixture
def http_class():
    return Http('https://hapi.fhir.tw/fhir')
