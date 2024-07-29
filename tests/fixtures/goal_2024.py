import pytest
from fhir_data_generator import Goal


@pytest.fixture
def goal_class():
    return Goal('goal-example')

@pytest.fixture
def profile_urls():
    return [
        'https://hapi.fhir.tw/fhir/StructureDefinition/Goal-sport',
    ]

@pytest.fixture
def identifiers():
    return [{
        'system': 'https://www.health.ntpc.gov.tw/',
        'value': 's141526',
    }]

@pytest.fixture
def category_coding():
    return [{
        'system': 'https://hapi.fhir.tw/fhir/CodeSystem/tempcode',
        'code': 'PhysicalActivity',
        'display': 'Physical Activity'
    }]

@pytest.fixture
def lifecycle_status():
    return 'proposed'

@pytest.fixture
def category_coding():
    return [{
        'system': 'https://hapi.fhir.tw/fhir/CodeSystem/tempcode',
        'code': 'PhysicalActivity',
        'display': 'Physical Activity'
    }]

@pytest.fixture
def description_text():
    return 'L5-S1椎間盤突出，在六個月內減少突出程度2-3毫米，疼痛評分減少50%'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/patient-tw-example',
    }

@pytest.fixture
def target_measure_coding():
    return [{
        'system': 'http://loinc.org',
        'code': '41950-7',
        'display': 'Number of steps in 24 hour Measured'
    }]

@pytest.fixture
def target_detail_quantity():
    return {
        'value': 5000,
        'unit': 'steps per day',
        'system': 'http://unitsofmeasure.org',
        'code': '/d',
    }

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Goal',
        'id': 'goal-example',
        'meta': {
            'profile': ['https://hapi.fhir.tw/fhir/StructureDefinition/Goal-sport']
        },
        'identifier': [{
            'system': 'https://www.health.ntpc.gov.tw/',
            'value': 's141526'
        }],
        'lifecycleStatus': 'proposed',
        'category': [{
            'coding': [{
                'system': 'https://hapi.fhir.tw/fhir/CodeSystem/tempcode',
                'code': 'PhysicalActivity',
                'display': 'Physical Activity'
            }]
        }],
        'description': {
            'text': 'L5-S1椎間盤突出，在六個月內減少突出程度2-3毫米，疼痛評分減少50%'
        },
        'subject': {
            'reference': 'Patient/patient-tw-example'
        },
        'target': [{
            'measure': {
                'coding': [{
                    'system': 'http://loinc.org',
                    'code': '41950-7',
                    'display': 'Number of steps in 24 hour Measured'
                }]
            },
            'detailQuantity': {
                'value': 5000,
                'unit': 'steps per day',
                'system': 'http://unitsofmeasure.org',
                'code': '/d'
            },
        }]
    }
