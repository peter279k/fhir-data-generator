import pytest
from fhir_data_generator import TWCoreObservationLabReport as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='obs-lab-example')

@pytest.fixture
def profile_urls():
    return [
        'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Observation-laboratoryResult-twcore'
    ]

@pytest.fixture
def status():
    return 'final'

@pytest.fixture
def category_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/observation-category',
        'code': 'laboratory',
    }]

@pytest.fixture
def code_coding():
    return [{
        'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medical-service-payment-tw',
        'code': '09002C',
    }]

@pytest.fixture
def code_text():
    return '血中尿素氮'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/pat-example',
    }

@pytest.fixture
def effective_datetime():
    return '2022-07-31'

@pytest.fixture
def performer():
    return [{
        'reference': 'Organization/org-hosp-example',
    }]

@pytest.fixture
def value_quantity():
    return {
        'value': 16.6,
        'unit': 'mg/dL',
    }

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Observation',
        'id': 'obs-lab-example',
        'meta': {
            'profile': [
                'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Observation-laboratoryResult-twcore'
            ]
        },
        'status': 'final',
        'category': [{
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/observation-category',
                'code': 'laboratory'
            }]
        }],
        'code': {
            'coding': [{
                'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medical-service-payment-tw',
                'code': '09002C'
            }],
            'text': '血中尿素氮'
        },
        'subject': {
            'reference': 'Patient/pat-example'
        },
        'effectiveDateTime': '2022-07-31',
        'performer': [{
            'reference': 'Organization/org-hosp-example'
        }],
        'valueQuantity': {
            'value': 16.6,
            'unit': 'mg/dL',
        }
    }
