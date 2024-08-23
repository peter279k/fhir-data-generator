import pytest
from fhir_data_generator import PhysicalActivityObservation as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='gaitcycle-l-example')

@pytest.fixture
def profile_urls():
    return [
        'https://hapi.fhir.tw/fhir/StructureDefinition/GaitCycle-sport'
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
        'system': 'http://snomed.info/sct',
        'code': '363837002',
        'display': 'Measure of gait'
    }]

@pytest.fixture
def code_text():
    return 'Measure of gait'

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
def value_quantity():
    return {
        'value': 18.3,
        'unit': 'kg/m2',
        'system': 'http://unitsofmeasure.org',
        'code': 'kg/m2',
    }

@pytest.fixture()
def body_site():
    return {
        'coding': [{
            'system': 'http://snomed.info/sct',
            'code': '22335008',
            'display': 'Structure of left foot'
        }]
    }

@pytest.fixture()
def component():
    return [{
        'code': {
            'coding': [{
                'system': 'https://hapi.fhir.tw/fhir/CodeSystem/gait-cycle',
                'code': '1',
                'display': '支撐期(stance phase)'
            }]
        },
        'valueQuantity': {
            'value': 60,
            'unit': '%',
            'system': 'http://unitsofmeasure.org',
            'code': '%'
        }
    },
    {
        'code': {
            'coding': [{
                'system': 'https://hapi.fhir.tw/fhir/CodeSystem/gait-cycle',
                'code': '2',
                'display': '擺動期(swing phase)'
            }]
        },
        'valueQuantity': {
            'value': 40,
            'unit': '%',
            'system': 'http://unitsofmeasure.org',
            'code': '%'
        }
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Observation',
        'id': 'gaitcycle-l-example',
        'meta': {
            'profile': ['https://hapi.fhir.tw/fhir/StructureDefinition/GaitCycle-sport']
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
                'system': 'http://snomed.info/sct',
                'code': '363837002',
                'display': 'Measure of gait'
            }],
            'text': 'Measure of gait'
        },
        'subject': {
            'reference': 'Patient/patient-ex-example'
        },
        'effectiveDateTime': '2024-07-01',
        'performer': [{
            'reference': 'Practitioner/practitioner-c-example'
        }],
        'bodySite': {
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '22335008',
                'display': 'Structure of left foot'
            }]
        },
        'component': [{
            'code': {
                'coding': [{
                    'system': 'https://hapi.fhir.tw/fhir/CodeSystem/gait-cycle',
                    'code': '1',
                    'display': '支撐期(stance phase)'
                }]
            },
            'valueQuantity': {
                'value': 60,
                'unit': '%',
                'system': 'http://unitsofmeasure.org',
                'code': '%'
            }
        },
        {
            'code': {
                'coding': [{
                    'system': 'https://hapi.fhir.tw/fhir/CodeSystem/gait-cycle',
                    'code': '2',
                    'display': '擺動期(swing phase)'
                }]
            },
            'valueQuantity': {
                'value': 40,
                'unit': '%',
                'system': 'http://unitsofmeasure.org',
                'code': '%'
            }
        }]
    }
