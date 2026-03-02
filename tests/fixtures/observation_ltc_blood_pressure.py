import pytest
from fhir_data_generator import ObservationLtc as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='ltc-observation-blood-pressure-example')

@pytest.fixture
def profile_urls():
    return [
        'http://ltc-ig.fhir.tw/StructureDefinition/LTCObservationVitalSigns'
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
        'code': '85354-9',
        'display': 'Blood pressure panel with all children optional'
    }]

@pytest.fixture
def code_text():
    return '血壓'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/ltc-patient-chen-ming-hui',
    }

@pytest.fixture
def effective_datetime():
    return '2024-01-15T09:00:00+08:00'

@pytest.fixture
def performer():
    return [{
        'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'
    }]

@pytest.fixture
def component():
    return [{
        'code': {
            'coding': [{
                'system': 'http://loinc.org',
                'code': '8480-6',
                'display': 'Systolic blood pressure'
            }]
        },
        'valueQuantity': {
            'value': 135,
            'unit': 'mmHg',
            'system': 'http://unitsofmeasure.org',
            'code': 'mm[Hg]'
        }
    },
    {
      'code': {
        'coding': [
          {
            'system': 'http://loinc.org',
            'code': '8462-4',
            'display': 'Diastolic blood pressure'
          }
        ]
      },
      'valueQuantity': {
        'value': 85,
        'unit': 'mmHg',
        'system': 'http://unitsofmeasure.org',
        'code': 'mm[Hg]'
      }
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Observation',
        'id': 'ltc-observation-blood-pressure-example',
        'meta': {
            'profile': ['http://ltc-ig.fhir.tw/StructureDefinition/LTCObservationVitalSigns']
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
                'code': '85354-9',
                'display': 'Blood pressure panel with all children optional'
            }],
            'text': '血壓'
        },
        'subject': {
            'reference': 'Patient/ltc-patient-chen-ming-hui'
        },
        'effectiveDateTime': '2024-01-15T09:00:00+08:00',
        'performer': [{
            'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'
        }],
        'component': [{
            'code': {
                'coding': [{
                    'system': 'http://loinc.org',
                    'code': '8480-6',
                    'display': 'Systolic blood pressure'
                }]
            },
            'valueQuantity': {
                'value': 135,
                'unit': 'mmHg',
                'system': 'http://unitsofmeasure.org',
                'code': 'mm[Hg]'
            }
        },
        {
            'code': {
                'coding': [{
                    'system': 'http://loinc.org',
                    'code': '8462-4',
                    'display': 'Diastolic blood pressure'
                }]
            },
            'valueQuantity': {
                'value': 85,
                'unit': 'mmHg',
                'system': 'http://unitsofmeasure.org',
                'code': 'mm[Hg]'
            }
        }]
    }
