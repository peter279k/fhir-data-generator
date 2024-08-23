import pytest
from fhir_data_generator import PhysicalActivityObservation as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='TBW-example')

@pytest.fixture
def profile_urls():
    return [
        'https://hapi.fhir.tw/fhir/StructureDefinition/TBW-sport'
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
        'code': '101683-1',
        'display': 'Body water mass'
    }]

@pytest.fixture
def code_text():
    return 'Body water mass'

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
        'value': 23.9,
        'unit': 'kg',
        'system': 'http://unitsofmeasure.org',
        'code': 'kg'
    }

@pytest.fixture
def has_member():
    return [
        {
            'reference': 'Observation/ICW-example'
        },
        {
            'reference': 'Observation/ECW-example'
        }
    ]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Observation',
        'id': 'TBW-example',
        'meta': {
            'profile': ['https://hapi.fhir.tw/fhir/StructureDefinition/TBW-sport']
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
                'code': '101683-1',
                'display': 'Body water mass'
            }],
            'text': 'Body water mass'
        },
        'subject': {
            'reference': 'Patient/patient-ex-example'
        },
        'effectiveDateTime': '2024-07-01',
        'performer': [{
            'reference': 'Practitioner/practitioner-c-example'
        }],
        'valueQuantity': {
            'value': 23.9,
            'unit': 'kg',
            'system': 'http://unitsofmeasure.org',
            'code': 'kg'
        },
        'hasMember': [
            {
                'reference': 'Observation/ICW-example'
            },
            {
                'reference': 'Observation/ECW-example'
            }
        ]
    }
