import pytest
from fhir_data_generator import ObservationLtc as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='pasport-observation-heart-rate-example')

@pytest.fixture
def profile_urls():
    return [
        'http://ltc-ig.fhir.tw/StructureDefinition/PASportObservationHeartRate'
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
def note():
    return  [{
      'time': '2024-01-15T09:30:00+08:00',
      'text': '運動前靜息心率，患者狀態穩定，準備開始進行步行運動'
    }]

@pytest.fixture
def body_site_coding():
    return  [{
        'system': 'http://snomed.info/sct',
        'code': '368209003',
        'display': 'Right upper arm structure'
      }]

@pytest.fixture
def code_coding():
    return [{
        'system': 'http://loinc.org',
        'code': '8867-4',
        'display': 'Heart rate'
    }]

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/ltc-patient-chen-ming-hui',
    }

@pytest.fixture
def effective_datetime():
    return '2024-01-15T09:30:00+08:00'

@pytest.fixture
def performer():
    return [{
        'reference': 'Practitioner/ltc-practitioner-example',
    }]

@pytest.fixture
def value_quantity():
    return {
        'value': 72,
        'unit': 'beats/min',
        'system': 'http://unitsofmeasure.org',
        'code': '/min'
    }

@pytest.fixture
def method_coding():
    return  [{
        'system': 'http://snomed.info/sct',
        'code': '37931006',
        'display': 'Auscultation'
      }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Observation',
        'id': 'pasport-observation-heart-rate-example',
        'meta': {
            'profile': ['http://ltc-ig.fhir.tw/StructureDefinition/PASportObservationHeartRate']
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
                'code': '8867-4',
                'display': 'Heart rate'
            }]
        },
        'subject': {
            'reference': 'Patient/ltc-patient-chen-ming-hui'
        },
        'effectiveDateTime': '2024-01-15T09:30:00+08:00',
        'performer': [{
            'reference': 'Practitioner/ltc-practitioner-example'
        }],
        'valueQuantity': {
            'value': 72,
            'unit': 'beats/min',
            'system': 'http://unitsofmeasure.org',
            'code': '/min'
        },
        'note': [{
            'time': '2024-01-15T09:30:00+08:00',
            'text': '運動前靜息心率，患者狀態穩定，準備開始進行步行運動'
        }],
        'bodySite': {
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '368209003',
                'display': 'Right upper arm structure'
            }]
        },
        'method': {
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '37931006',
                'display': 'Auscultation'
            }]
        }
    }
