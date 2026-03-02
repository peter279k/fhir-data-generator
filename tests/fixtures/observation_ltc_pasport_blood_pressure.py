import pytest
from fhir_data_generator import ObservationLtc as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='pasport-observation-blood-pressure-example')

@pytest.fixture
def profile_urls():
    return [
        'http://ltc-ig.fhir.tw/StructureDefinition/PASportObservationBloodPressure'
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
        'reference': 'Practitioner/ltc-practitioner-example'
    }]

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
        'time': '2024-01-15T09:00:00+08:00',
        'text': '運動前血壓測量，收縮壓128/舒張壓82mmHg，數值正常，可安全進行運動'
    }]

@pytest.fixture
def body_site_coding():
    return [{
        'system': 'http://snomed.info/sct',
        'code': '368208006',
        'display': 'Left upper arm structure'
    }]

@pytest.fixture
def method_coding():
    return  [{
        'system': 'http://snomed.info/sct',
        'code': '37931006',
        'display': 'Auscultation'
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
            'value': 128,
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
        'value': 82,
        'unit': 'mmHg',
        'system': 'http://unitsofmeasure.org',
        'code': 'mm[Hg]'
      }
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Observation',
        'id': 'pasport-observation-blood-pressure-example',
        'meta': {
            'profile': ['http://ltc-ig.fhir.tw/StructureDefinition/PASportObservationBloodPressure']
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
            }]
        },
        'subject': {
            'reference': 'Patient/ltc-patient-chen-ming-hui'
        },
        'effectiveDateTime': '2024-01-15T09:00:00+08:00',
        'performer': [{
            'reference': 'Practitioner/ltc-practitioner-example'
        }],
        'interpretation': [{
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation',
                'code': 'N',
                'display': 'Normal'
            }]
        }],
        'note': [{
            'time': '2024-01-15T09:00:00+08:00',
            'text': '運動前血壓測量，收縮壓128/舒張壓82mmHg，數值正常，可安全進行運動'
        }],
        'bodySite': {
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '368208006',
                'display': 'Left upper arm structure'
            }]
        },
        'method': {
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '37931006',
                'display': 'Auscultation'
            }]
        },
        'component': [{
            'code': {
                'coding': [{
                    'system': 'http://loinc.org',
                    'code': '8480-6',
                    'display': 'Systolic blood pressure'
                }]
            },
            'valueQuantity': {
                'value': 128,
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
                'value': 82,
                'unit': 'mmHg',
                'system': 'http://unitsofmeasure.org',
                'code': 'mm[Hg]'
            }
        }]
    }
