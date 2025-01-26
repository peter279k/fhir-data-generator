import pytest
from fhir_data_generator import TWCorePractitioner as Practitioner


@pytest.fixture
def practitioner_class():
    return Practitioner(practitioner_id='Practitioner-min')

@pytest.fixture
def profile_urls():
    return ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/practitioner-imri']

@pytest.fixture
def name():
    return [{
        'use': 'official',
        'text': '劉伊詩',
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Practitioner',
        'id' : 'Practitioner-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/practitioner-imri']
        },
        'name' : [{
            'use' : 'official',
            'text' : '劉伊詩'
        }]
    }
