import pytest
from fhir_data_generator import ObservationLtc as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='ltc-observation-vital-signs-panel-example')

@pytest.fixture
def profile_urls():
    return [
        'http://ltc-ig.fhir.tw/StructureDefinition/LTCObservationVitalSignsPanel'
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
        'code': '85353-1',
        'display': 'Vital signs, weight, height, head circumference, oxygen saturation and BMI panel'
    }]

@pytest.fixture
def code_text():
    return '一組生命徵象檢驗檢查'

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
        'reference': 'Practitioner/ltc-practitioner-physician-aa12-example'
    }]

@pytest.fixture
def note():
    return [{
        'time': '2024-01-15T08:00:00+08:00',
        'text': '生命徵象檢查完成，各項指標均在正常範圍內'
    }]

@pytest.fixture
def has_member():
    return [{
        'reference': 'Observation/ltc-observation-blood-pressure-example'
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Observation',
        'id': 'ltc-observation-vital-signs-panel-example',
        'meta': {
            'profile': ['http://ltc-ig.fhir.tw/StructureDefinition/LTCObservationVitalSignsPanel']
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
                'code': '85353-1',
                'display': 'Vital signs, weight, height, head circumference, oxygen saturation and BMI panel'
            }],
            'text': '一組生命徵象檢驗檢查'
        },
        'subject': {
            'reference': 'Patient/ltc-patient-chen-ming-hui'
        },
        'effectiveDateTime': '2024-01-15T08:00:00+08:00',
        'performer': [{
            'reference': 'Practitioner/ltc-practitioner-physician-aa12-example'
        }],
        'note': [{
            'time': '2024-01-15T08:00:00+08:00',
            'text': '生命徵象檢查完成，各項指標均在正常範圍內'
        }],
        'hasMember': [{
            'reference': 'Observation/ltc-observation-blood-pressure-example'
        }]
    }
