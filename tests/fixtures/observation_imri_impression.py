import pytest
from fhir_data_generator import ObservationIclaimC1 as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='ObservationImpression-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/observation-impression-imri'
    ]

@pytest.fixture
def status():
    return 'preliminary'

@pytest.fixture
def category_coding():
    return [{
        'system' : 'http://loinc.org',
        'code' : '46241-6',
        'display' : 'Hospital admission diagnosis Narrative - Reported'
    }]

@pytest.fixture
def code_coding():
    return [{
        'system' : 'http://loinc.org',
        'code' : '32438-4',
        'display' : 'Physical findings of Hemorrhoid'
    }]

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/Patient-min',
    }

@pytest.fixture
def effective_datetime():
    return '2023-09-07'

@pytest.fixture
def value_string():
    return 'Prolapsed mixed hemorrhoids'

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Observation',
        'id' : 'ObservationImpression-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/observation-impression-imri']
        },
        'status' : 'preliminary',
        'category' : [{
            'coding' : [{
                'system' : 'http://loinc.org',
                'code' : '46241-6',
                'display' : 'Hospital admission diagnosis Narrative - Reported'
            }]
        }],
        'code' : {
            'coding' : [{
                'system' : 'http://loinc.org',
                'code' : '32438-4',
                'display' : 'Physical findings of Hemorrhoid'
            }]
        },
        'subject' : {
            'reference' : 'Patient/Patient-min'
        },
        'effectiveDateTime' : '2023-09-07',
        'valueString' : 'Prolapsed mixed hemorrhoids'
    }
