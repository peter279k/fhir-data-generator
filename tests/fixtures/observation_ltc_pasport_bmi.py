import pytest
from fhir_data_generator import ObservationLtc as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='pasport-observation-bmi-example')

@pytest.fixture
def profile_urls():
    return [
        'http://ltc-ig.fhir.tw/StructureDefinition/PASportObservationBodyMassIndex'
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
        'code': '39156-5',
        'display': 'Body mass index (BMI) [Ratio]'
    }]

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/ltc-patient-chen-ming-hui',
    }

@pytest.fixture
def effective_datetime():
    return '2024-01-15T08:30:00+08:00'

@pytest.fixture
def performer():
    return [{
        'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'
    }]

@pytest.fixture
def value_quantity():
    return {
        'value': 23.8,
        'unit': 'kg/m2',
        'system': 'http://unitsofmeasure.org',
        'code': 'kg/m2'
    }

@pytest.fixture
def interpretation():
    return [{
        'coding': [{
            'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation',
            'code': 'N',
            'display': 'Normal'
        }]
    }]

@pytest.fixture
def note():
    return  [{
      'time': '2024-01-15T08:30:00+08:00',
      'text': 'BMI值23.8，屬於正常範圍，建議維持目前體重並透過運動增強體能'
    }]

@pytest.fixture
def derived_from():
    return [{
        'reference': 'Observation/pasport-observation-weight-example'
    },
    {
        'reference': 'Observation/pasport-observation-height-example'
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Observation',
        'id': 'pasport-observation-bmi-example',
        'meta': {
            'profile': ['http://ltc-ig.fhir.tw/StructureDefinition/PASportObservationBodyMassIndex']
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
                'code': '39156-5',
                'display': 'Body mass index (BMI) [Ratio]'
            }]
        },
        'subject': {
            'reference': 'Patient/ltc-patient-chen-ming-hui'
        },
        'effectiveDateTime': '2024-01-15T08:30:00+08:00',
        'performer': [{
            'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'
        }],
        'valueQuantity': {
            'value': 23.8,
            'unit': 'kg/m2',
            'system': 'http://unitsofmeasure.org',
            'code': 'kg/m2'
        },
        'interpretation': [{
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation',
                'code': 'N',
                'display': 'Normal'
            }]
        }],
        'note': [{
            'time': '2024-01-15T08:30:00+08:00',
            'text': 'BMI值23.8，屬於正常範圍，建議維持目前體重並透過運動增強體能'
        }],
        'derivedFrom': [{
            'reference': 'Observation/pasport-observation-weight-example'
        },
        {
            'reference': 'Observation/pasport-observation-height-example'
        }]
    }
