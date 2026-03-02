import pytest
from fhir_data_generator import ObservationLtc as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='pasport-observation-height-example')

@pytest.fixture
def profile_urls():
    return [
        'http://ltc-ig.fhir.tw/StructureDefinition/PASportObservationHeight'
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
        'code': '8302-2',
        'display': 'Body height'
    }]

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/ltc-patient-chen-ming-hui',
    }

@pytest.fixture
def effective_datetime():
    return '2024-01-15T08:15:00+08:00'

@pytest.fixture
def performer():
    return [{
        'reference': 'Practitioner/ltc-practitioner-example'
    }]

@pytest.fixture
def value_quantity():
    return {
        'value': 165.8,
        'unit': 'cm',
        'system': 'http://unitsofmeasure.org',
        'code': 'cm'
    }

@pytest.fixture
def note():
    return [{
        'time': '2024-01-15T08:15:00+08:00',
        'text': '身高165.8公分，用於計算BMI及設計個人化運動計畫'
    }]

@pytest.fixture
def method_coding():
    return  [{
        'system': 'http://snomed.info/sct',
        'code': '363808001',
        'display': 'Measured body weight'
      }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Observation',
        'id': 'pasport-observation-height-example',
        'meta': {
            'profile': ['http://ltc-ig.fhir.tw/StructureDefinition/PASportObservationHeight']
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
                'code': '8302-2',
                'display': 'Body height'
            }]
        },
        'subject': {
            'reference': 'Patient/ltc-patient-chen-ming-hui'
        },
        'effectiveDateTime': '2024-01-15T08:15:00+08:00',
        'performer': [{
            'reference': 'Practitioner/ltc-practitioner-example'
        }],
        'valueQuantity': {
            'value': 165.8,
            'unit': 'cm',
            'system': 'http://unitsofmeasure.org',
            'code': 'cm'
        },
        'note': [{
            'time': '2024-01-15T08:15:00+08:00',
            'text': '身高165.8公分，用於計算BMI及設計個人化運動計畫'
        }],
        'method': {
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '363808001',
                'display': 'Measured body weight'
            }]
        }
    }
