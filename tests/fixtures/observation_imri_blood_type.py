import pytest
from fhir_data_generator import ObservationIclaimC1 as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='ObservationBloodType-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/observationbloodtype-imri'
    ]

@pytest.fixture
def status():
    return 'final'

@pytest.fixture
def code_coding():
    return [{
        'system' : 'http://loinc.org',
        'code' : '882-1',
        'display' : 'ABO and Rh group [Type] in Blood'
    }]

@pytest.fixture
def code_text():
    return 'ABO and Rh group [Type] in Blood'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/Patient-min',
    }

@pytest.fixture
def effective_datetime():
    return '2023-09-08T11:25:11+08:00'

@pytest.fixture
def value_codeable_concept():
    return {
        'coding' : [{
            'system' : 'http://loinc.org',
            'code' : 'LA21327-4',
            'display' : 'B Pos'
        }]
    }

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Observation',
        'id' : 'ObservationBloodType-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/observationbloodtype-imri']
        },
        'status' : 'final',
        'code' : {
            'coding' : [{
                'system' : 'http://loinc.org',
                'code' : '882-1',
                'display' : 'ABO and Rh group [Type] in Blood'
            }],
            'text' : 'ABO and Rh group [Type] in Blood'
        },
        'subject' : {
            'reference' : 'Patient/Patient-min'
        },
        'effectiveDateTime' : '2023-09-08T11:25:11+08:00',
        'valueCodeableConcept' : {
            'coding' : [{
                'system' : 'http://loinc.org',
                'code' : 'LA21327-4',
                'display' : 'B Pos'
            }]
        }
    }
