import pytest
from fhir_data_generator import PhysicalActivityObservation as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='weighttraining-example')

@pytest.fixture
def profile_urls():
    return [
        'https://hapi.fhir.tw/fhir/StructureDefinition/WeightTraining-sport',
    ]

@pytest.fixture
def status():
    return 'final'

@pytest.fixture
def category_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/observation-category',
        'code': 'activity',
        'display': 'Activity'
    }]

@pytest.fixture
def code_coding():
    return [{
        'system': 'http://loinc.org',
        'code': 'LA11839-0',
        'display': 'Weights'
    }]

@pytest.fixture
def code_text():
    return 'Weights'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/patient-ex-example',
    }

@pytest.fixture
def effective_datetime():
    return '2024-07-01'

@pytest.fixture
def performer():
    return [{
        'reference': 'Practitioner/practitioner-c-example',
    }]

@pytest.fixture
def value_codeable_concept():
    return {
        'coding': [{
            'system': 'http://snomed.info/sct',
            'code': '229115003',
            'display': 'Bench press'
        }]
    }

@pytest.fixture
def component():
    return [{
        'code': {
            'coding': [{
                'system': 'https://hapi.fhir.tw/fhir/CodeSystem/sport-training',
                'code': 'training-wt',
                'display': '訓練重量'
            }]
        },
        'valueQuantity': {
            'value': 50,
            'unit': 'kg',
            'system': 'http://unitsofmeasure.org',
            'code': 'kg'
        }
    },
    {
        'code': {
            'coding': [{
                'system': 'https://hapi.fhir.tw/fhir/CodeSystem/sport-training',
                'code': 'sets',
                'display': '訓練組數'
            }]
        },
            'valueQuantity': {
                'value': 1
            }
        },
        {
        'code': {
            'coding': [{
                'system': 'http://loinc.org',
                'code': '100298-9',
                'display': 'Repetition count'
            }]
        },
        'valueQuantity': {
            'value': 30
        }
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Observation',
        'id': 'weighttraining-example',
        'meta': {
            'profile': ['https://hapi.fhir.tw/fhir/StructureDefinition/WeightTraining-sport']
        },
        'status': 'final',
        'category': [{
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/observation-category',
                'code': 'activity',
                'display': 'Activity'
            }]
        }],
        'code': {
            'coding': [{
                'system': 'http://loinc.org',
                'code': 'LA11839-0',
                'display': 'Weights'
            }],
            'text': 'Weights'
        },
        'subject': {
            'reference': 'Patient/patient-ex-example'
        },
        'effectiveDateTime': '2024-07-01',
        'performer': [{
            'reference': 'Practitioner/practitioner-c-example'
        }],
        'valueCodeableConcept': {
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '229115003',
                'display': 'Bench press'
            }]
        },
        'component': [{
            'code': {
                'coding': [{
                    'system': 'https://hapi.fhir.tw/fhir/CodeSystem/sport-training',
                    'code': 'training-wt',
                    'display': '訓練重量'
                }]
            },
            'valueQuantity': {
                'value': 50,
                'unit': 'kg',
                'system': 'http://unitsofmeasure.org',
                'code': 'kg'
            }
        },
        {
            'code': {
                'coding': [{
                    'system': 'https://hapi.fhir.tw/fhir/CodeSystem/sport-training',
                    'code': 'sets',
                    'display': '訓練組數'
                }]
            },
            'valueQuantity': {
                'value': 1
            }
        },
        {
            'code': {
                'coding': [{
                    'system': 'http://loinc.org',
                    'code': '100298-9',
                    'display': 'Repetition count'
                }]
            }, 'valueQuantity': {
                'value': 30
            }
        }]
    }
