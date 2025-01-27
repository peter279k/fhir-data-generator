import pytest
from fhir_data_generator import ObservationIclaimC1 as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='ObservationBloodLoss-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/observationbloodloss-imri'
    ]

@pytest.fixture
def part_of():
    return [{
        'reference' : 'Procedure/Procedure-pro'
    }]

@pytest.fixture
def status():
    return 'final'

@pytest.fixture
def code_coding():
    return [{
        'system' : 'http://loinc.org',
        'code' : '59770-8',
        'display' : 'Procedure estimated blood loss Narrative'
    }]

@pytest.fixture
def code_text():
    return 'Procedure estimated blood loss Narrative'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/Patient-min',
    }

@pytest.fixture
def effective_datetime():
    return '2023-09-08T11:25:11+08:00'

@pytest.fixture
def value_quantity():
    return {
        'value' : 1,
        'unit' : 'C.C.'
    }

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Observation',
        'id' : 'ObservationBloodLoss-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/observationbloodloss-imri']
        },
        'partOf' : [{
            'reference' : 'Procedure/Procedure-pro'
        }],
        'status' : 'final',
        'code' : {
            'coding' : [{
                'system' : 'http://loinc.org',
                'code' : '59770-8',
                'display' : 'Procedure estimated blood loss Narrative'
            }],
            'text' : 'Procedure estimated blood loss Narrative'
        },
        'subject' : {
            'reference' : 'Patient/Patient-min'
        },
        'effectiveDateTime' : '2023-09-08T11:25:11+08:00',
        'valueQuantity' : {
            'value' : 1,
            'unit' : 'C.C.'
        }
    }
