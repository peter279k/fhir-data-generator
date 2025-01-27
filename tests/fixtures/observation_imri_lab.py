import pytest
from fhir_data_generator import ObservationIclaimC1 as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='ObservationLaboratory-lab')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/observation-laboratory-imri'
    ]

@pytest.fixture
def status():
    return 'final'

@pytest.fixture
def category_coding():
    return [{
        'system' : 'http://loinc.org',
        'code' : '30954-2',
        'display' : 'Relevant diagnostic tests/laboratory data Narrative'
    }]

@pytest.fixture
def code_coding():
    return [{
        'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medical-service-payment-tw',
        'code' : '08003C',
        'display' : '血色素檢查'
    }]

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/Patient-min',
    }

@pytest.fixture
def effective_datetime():
    return '2023-09-06'

@pytest.fixture
def value_quantity():
    return {
        'value' : 15.9,
        'unit' : 'g/dL'
    }

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Observation',
        'id' : 'ObservationLaboratory-lab',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/observation-laboratory-imri']
        },
        'status' : 'final',
        'category' : [{
            'coding' : [{
                'system' : 'http://loinc.org',
                'code' : '30954-2',
                'display' : 'Relevant diagnostic tests/laboratory data Narrative'
            }]
        }],
        'code' : {
            'coding' : [{
                'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medical-service-payment-tw',
                'code' : '08003C',
                'display' : '血色素檢查'
            }]
        },
        'subject' : {
            'reference' : 'Patient/Patient-min'
        },
        'effectiveDateTime' : '2023-09-06',
        'valueQuantity' : {
            'value' : 15.9,
            'unit' : 'g/dL'
        }
    }
