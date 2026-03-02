import pytest
from fhir_data_generator import ObservationLtc as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='pasport-observation-skeletal-muscle-mass-example')

@pytest.fixture
def profile_urls():
    return [
        'http://ltc-ig.fhir.tw/StructureDefinition/PASportObservationSkeletalMuscleMass'
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
        'system': 'http://ltc-ig.fhir.tw/CodeSystem/TempCodeCS-Sport',
        'code': 'SMM',
        'display': '骨骼肌重'
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
        'value': 20.8,
        'unit': 'kg',
        'system': 'http://unitsofmeasure.org',
        'code': 'kg'
    }

@pytest.fixture
def interpretation():
    return  [{
        'coding': [{
            'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation',
            'code': 'L',
            'display': 'Low'
        }]
    }]

@pytest.fixture
def note():
    return  [{
        'time': '2024-01-15T08:45:00+08:00',
        'text': '骨骼肌重20.8公斤，略低於年齡標準。建議增加阻力訓練以提升肌肉量，預防肌少症'
    }]

@pytest.fixture
def method_coding():
    return [{
        'system': 'http://snomed.info/sct',
        'code': '252465000',
        'display': 'Pulse oximetry'
    }]

@pytest.fixture
def device():
    return {
        'display': 'InBody 270 身體組成分析儀'
    }

@pytest.fixture
def reference_range():
    return [{
        'low': {
            'value': 22,
            'unit': 'kg',
            'system': 'http://unitsofmeasure.org',
            'code': 'kg'
        },
        'high': {
            'value': 27,
            'unit': 'kg',
            'system': 'http://unitsofmeasure.org',
            'code': 'kg'
        },
        'text': '65歲女性正常範圍'
    }]

@pytest.fixture
def component():
    return [{
        'code': {
            'coding': [{
                'system': 'http://ltc-ig.fhir.tw/CodeSystem/TempCodeCS-Sport',
                'code': 'SMI',
                'display': '肌肉質量指數'
            }]
        },
        'valueQuantity': {
            'value': 7.6,
            'unit': 'kg/m2',
            'system': 'http://unitsofmeasure.org',
            'code': 'kg/m2'
        }
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Observation',
        'id': 'pasport-observation-skeletal-muscle-mass-example',
        'meta': {
            'profile': ['http://ltc-ig.fhir.tw/StructureDefinition/PASportObservationSkeletalMuscleMass']
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
                'system': 'http://ltc-ig.fhir.tw/CodeSystem/TempCodeCS-Sport',
                'code': 'SMM',
                'display': '骨骼肌重'
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
            'value': 20.8,
            'unit': 'kg',
            'system': 'http://unitsofmeasure.org',
            'code': 'kg'
        },
        'interpretation': [{
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation',
                'code': 'L',
                'display': 'Low'
            }]
        }],
        'note': [{
            'time': '2024-01-15T08:45:00+08:00',
            'text': '骨骼肌重20.8公斤，略低於年齡標準。建議增加阻力訓練以提升肌肉量，預防肌少症'
        }],
        'method': {
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '252465000',
                'display': 'Pulse oximetry'
            }]
        },
        'device': {
            'display': 'InBody 270 身體組成分析儀'
        },
        'referenceRange': [{
            'low': {
                'value': 22,
                'unit': 'kg',
                'system': 'http://unitsofmeasure.org',
                'code': 'kg'
            },
            'high': {
                'value': 27,
                'unit': 'kg',
                'system': 'http://unitsofmeasure.org',
                'code': 'kg'
            },
            'text': '65歲女性正常範圍'
        }],
        'component': [{
            'code': {
                'coding': [{
                    'system': 'http://ltc-ig.fhir.tw/CodeSystem/TempCodeCS-Sport',
                    'code': 'SMI',
                    'display': '肌肉質量指數'
                }]
            },
            'valueQuantity': {
                'value': 7.6,
                'unit': 'kg/m2',
                'system': 'http://unitsofmeasure.org',
                'code': 'kg/m2'
            }
        }]
    }
