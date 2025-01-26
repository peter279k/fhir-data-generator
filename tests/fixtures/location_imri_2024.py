import pytest
from fhir_data_generator import LocationImri as Location


@pytest.fixture
def location_class():
    return Location('Location-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/location-imri',
    ]

@pytest.fixture
def identifier():
    return [{
        'value' : '4012S'
    }]

@pytest.fixture
def name():
    return '病床'

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Location',
        'id' : 'Location-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/location-imri']
        },
        'identifier' : [{
            'value' : '4012S'
        }],
        'name' : '病床'
    }
