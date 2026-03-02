import pytest
from fhir_data_generator import ObservationLtc as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='pasport-observation-body-fat-percentage-example')

@pytest.fixture
def profile_urls():
    return [
        'http://ltc-ig.fhir.tw/StructureDefinition/PASportObservationBodyFatPercentage'
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
        'code': '41982-0',
        'display': 'Percentage of body fat Measured'
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
        'value': 28.5,
        'unit': '%',
        'system': 'http://unitsofmeasure.org',
        'code': '%'
    }

@pytest.fixture
def interpretation():
    return [{
      'coding': [
        {
          'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation',
          'code': 'N',
          'display': 'Normal'
        }
      ]
    }]

@pytest.fixture
def note():
    return [{
        'time': '2024-01-15T08:45:00+08:00',
        'text': '體脂率28.5%，位於女性正常範圍內。建議透過有氧運動和肌力訓練來優化身體組成'
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
            'value': 21,
            'unit': '%',
            'system': 'http://unitsofmeasure.org',
            'code': '%'
        },
        'high': {
            'value': 33,
            'unit': '%',
            'system': 'http://unitsofmeasure.org',
            'code': '%'
        },
        'text': '女性正常範圍'
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Observation',
        'id': 'pasport-observation-body-fat-percentage-example',
        'meta': {
            'profile': ['http://ltc-ig.fhir.tw/StructureDefinition/PASportObservationBodyFatPercentage']
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
                'code': '41982-0',
                'display': 'Percentage of body fat Measured'
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
            'value': 28.5,
            'unit': '%',
            'system': 'http://unitsofmeasure.org',
            'code': '%'
        },
        'interpretation': [{
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation',
                'code': 'N',
                'display': 'Normal'
            }]
        }],
        'note': [{
            'time': '2024-01-15T08:45:00+08:00',
            'text': '體脂率28.5%，位於女性正常範圍內。建議透過有氧運動和肌力訓練來優化身體組成'
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
                'value': 21,
                'unit': '%',
                'system': 'http://unitsofmeasure.org',
                'code': '%'
            },
            'high': {
                'value': 33,
                'unit': '%',
                'system': 'http://unitsofmeasure.org',
                'code': '%'
            },
            'text': '女性正常範圍'
        }]
    }
