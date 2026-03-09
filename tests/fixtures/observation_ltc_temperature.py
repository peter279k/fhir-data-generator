import pytest
from fhir_data_generator import ObservationLtc as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='pasport-observation-body-temperature-example')

@pytest.fixture
def profile_urls():
    return [
        'http://ltc-ig.fhir.tw/StructureDefinition/PASportObservationBodyTemperature'
    ]

@pytest.fixture
def status():
    return 'final'

@pytest.fixture
def category_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/observation-category',
        'code': 'vital-signs',
        'display': 'Vital Signs'
    }]

@pytest.fixture
def code_coding():
    return [{
        'system': 'http://loinc.org',
        'code': '8310-5',
        'display': 'Body temperature'
    }]

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/ltc-patient-chen-ming-hui',
    }

@pytest.fixture
def effective_datetime():
    return '2024-01-15T08:45:00+08:00'

@pytest.fixture
def performer():
    return [{
        'reference': 'Practitioner/ltc-practitioner-example'
    }]

@pytest.fixture
def value_quantity():
    return {
        'value': 36.5,
        'unit': 'Cel',
        'system': 'http://unitsofmeasure.org',
        'code': 'Cel'
    }

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Observation',
        'id': 'pasport-observation-body-temperature-example',
        'meta': {
            'profile': ['http://ltc-ig.fhir.tw/StructureDefinition/PASportObservationBodyTemperature']
        },
        'status': 'final',
        'category': [{
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/observation-category',
                'code': 'vital-signs',
                'display': 'Vital Signs'
            }]
        }],
        'code': {
            'coding': [{
                'system': 'http://loinc.org',
                'code': '8310-5',
                'display': 'Body temperature'
            }]
        },
        'subject': {
            'reference': 'Patient/ltc-patient-chen-ming-hui'
        },
        'effectiveDateTime': '2024-01-15T08:45:00+08:00',
        'performer': [{
            'reference': 'Practitioner/ltc-practitioner-example'
        }],
        'valueQuantity': {
            'value': 36.5,
            'unit': 'Cel',
            'system': 'http://unitsofmeasure.org',
            'code': 'Cel'
        }
    }
