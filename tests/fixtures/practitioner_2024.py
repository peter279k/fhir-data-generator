import pytest
from fhir_data_generator import PhysicalActivityPractitioner as Practitioner


@pytest.fixture
def practitioner_class():
    return Practitioner(practitioner_id='practitioner-c-example')

@pytest.fixture
def profile_urls():
    return ['https://hapi.fhir.tw/fhir/StructureDefinition/TWCorePractitioner']

@pytest.fixture
def identifiers():
    return [
        {
            'use': 'official',
            'type': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code': 'MB'
                }]
            },
            'system': 'https://www.morefit.com.tw/tw',
            'value': 'S1006'
        }
    ]

@pytest.fixture
def active():
    return True

@pytest.fixture
def name_text():
    return '陳建升'

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Practitioner',
        'id': 'practitioner-c-example',
        'meta': {
            'profile': ['https://hapi.fhir.tw/fhir/StructureDefinition/TWCorePractitioner']
        },
        'identifier': [
            {
                'use': 'official',
                'type': {
                    'coding': [{
                        'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                        'code': 'MB'
                    }]
                },
                'system': 'https://www.morefit.com.tw/tw',
                'value': 'S1006'
            }
        ],
        'active': True,
        'name': [{
            'text': '陳建升',
        }],
    }
