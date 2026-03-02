import pytest
from fhir_data_generator import ObservationLtc as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='pasport-observation-weight-example')

@pytest.fixture
def profile_urls():
    return [
        'http://ltc-ig.fhir.tw/StructureDefinition/PASportObservationWeight'
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
        'code': '29463-7',
        'display': 'Body weight'
    }]

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/ltc-patient-chen-ming-hui',
    }

@pytest.fixture
def effective_datetime():
    return '2024-01-15T08:00:00+08:00'

@pytest.fixture
def performer():
    return [{
        'reference': 'Practitioner/ltc-practitioner-example'
    }]

@pytest.fixture
def value_quantity():
    return {
        'value': 65.5,
        'unit': 'kg',
        'system': 'http://unitsofmeasure.org',
        'code': 'kg'
    }

@pytest.fixture
def note():
    return [{
        'time': '2024-01-15T08:00:00+08:00',
        'text': '運動計畫開始前基線體重測量，較上月減輕0.8公斤，患者狀況良好'
    }]

@pytest.fixture
def method_coding():
    return [{
        'system': 'http://snomed.info/sct',
        'code': '363808001',
        'display': 'Measured body weight'
    }]

@pytest.fixture
def component():
    return [{
        'code': {
            'coding': [{
                'system': 'http://loinc.org',
                'code': '8350-1',
                'display': 'Weight W clothes Measured'
            }]
        },
        'valueQuantity': {
            'value': 80,
            'unit': 'kg',
            'system': 'http://unitsofmeasure.org',
            'code': 'kg'
        }
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Observation',
        'id': 'pasport-observation-weight-example',
        'meta': {
            'profile': ['http://ltc-ig.fhir.tw/StructureDefinition/PASportObservationWeight']
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
                'code': '29463-7',
                'display': 'Body weight'
            }]
        },
        'subject': {
            'reference': 'Patient/ltc-patient-chen-ming-hui'
        },
        'effectiveDateTime': '2024-01-15T08:00:00+08:00',
        'performer': [{
            'reference': 'Practitioner/ltc-practitioner-example'
        }],
        'valueQuantity': {
            'value': 65.5,
            'unit': 'kg',
            'system': 'http://unitsofmeasure.org',
            'code': 'kg'
        },
        'note': [{
            'time': '2024-01-15T08:00:00+08:00',
            'text': '運動計畫開始前基線體重測量，較上月減輕0.8公斤，患者狀況良好'
        }],
        'method': {
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '363808001',
                'display': 'Measured body weight'
            }]
        },
        'component': [{
            'code': {
                'coding': [{
                    'system': 'http://loinc.org',
                    'code': '8350-1',
                    'display': 'Weight W clothes Measured'
                }]
            },
            'valueQuantity': {
                'value': 80,
                'unit': 'kg',
                'system': 'http://unitsofmeasure.org',
                'code': 'kg'
            }
        }]
    }
