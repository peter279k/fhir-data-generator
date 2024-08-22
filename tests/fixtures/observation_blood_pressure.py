import pytest
from fhir_data_generator import TWCoreObservationBloodPressure as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='obs-bloodPressure-example')

@pytest.fixture
def profile_urls():
    return [
        'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Observation-bloodPressure-twcore'
    ]

@pytest.fixture
def status():
    return 'final'

@pytest.fixture
def category_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/observation-category',
        'code': 'vital-signs',
        'display': 'Vital Signs',
    }]

@pytest.fixture
def code_coding():
    return [{
        'system': 'http://loinc.org',
        'code': '85354-9',
        'display': 'Blood pressure panel with all children optional',
    }]

@pytest.fixture
def code_text():
    return 'Blood pressure panel with all children optional'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/pat-example',
    }

@pytest.fixture
def effective_datetime():
    return '2022-07-31'

@pytest.fixture
def performer():
    return [{
        'reference': 'Practitioner/pra-dr-example',
    }]

@pytest.fixture
def component():
    return [
        {
            'code': {
                'coding': [{
                    'system': 'http://loinc.org',
                    'code': '8480-6',
                    'display': 'Systolic blood pressure'
                }]
            },
            'valueQuantity': {
                'value': 110,
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
                'value': 56,
                'unit': 'mmHg',
                'system': 'http://unitsofmeasure.org',
                'code': 'mm[Hg]'
            }
        },
    ]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Observation',
        'id': 'obs-bloodPressure-example',
        'meta': {
            'profile': [
                'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Observation-bloodPressure-twcore'
            ]
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
            'text': 'Blood pressure panel with all children optional'
        },
        'subject': {
            'reference': 'Patient/pat-example'
        },
        'effectiveDateTime': '2022-07-31',
        'performer': [{
            'reference': 'Practitioner/pra-dr-example'
        }],
        'component': [
            {
                'code': {
                    'coding': [{
                        'system': 'http://loinc.org',
                        'code': '8480-6',
                        'display': 'Systolic blood pressure'
                    }]
                },
                'valueQuantity': {
                    'value': 110,
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
                    'value': 56,
                    'unit': 'mmHg',
                    'system': 'http://unitsofmeasure.org',
                    'code': 'mm[Hg]'
                }
            },
        ]
    }
