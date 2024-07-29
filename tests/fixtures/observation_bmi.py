import pytest
from fhir_data_generator import Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='obs-bmi-example')

@pytest.fixture
def profile_urls():
    return [
        'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Observation-bmi-twcore'
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
        'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/loinc-tw',
        'code': '39156-5',
        'display': 'Body mass index (BMI) [Ratio]',
    }]

@pytest.fixture
def code_text():
    return 'Body mass index (BMI) [Ratio]'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/pat-example',
    }

@pytest.fixture
def effective_datetime():
    return '2024-07-29'

@pytest.fixture
def performer():
    return [{
        'reference': 'Practitioner/pra-dr-example',
    }]

@pytest.fixture
def value_quantity():
    return {
        'value': 18.3,
        'unit': 'kg/m2',
        'system': 'http://unitsofmeasure.org',
        'code': 'kg/m2',
    }

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Observation',
        'id': 'obs-bmi-example',
        'meta': {
            'profile': [
                'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Observation-bmi-twcore'
            ],
        },
        'status': 'final',
        'category': [
            {
                'coding': [
                    {
                        'system': 'http://terminology.hl7.org/CodeSystem/observation-category',
                        'code': 'vital-signs',
                        'display': 'Vital Signs'
                    }
                ]
            }
        ],
        'code': {
            'coding': [
                {
                    'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/loinc-tw',
                    'code': '39156-5',
                    'display': 'Body mass index (BMI) [Ratio]'
                }
            ],
            'text': 'Body mass index (BMI) [Ratio]'
        },
        'subject': {
            'reference': 'Patient/pat-example'
        },
        'effectiveDateTime': '2024-07-29',
        'performer': [
            {
                'reference': 'Practitioner/pra-dr-example'
            },
        ],
        'valueQuantity': {
            'value': 18.3,
            'unit': 'kg/m2',
            'system': 'http://unitsofmeasure.org',
            'code': 'kg/m2'
        }
    }
