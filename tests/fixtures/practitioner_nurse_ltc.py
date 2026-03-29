import pytest
from fhir_data_generator import PractitionerLtc as Practitioner


@pytest.fixture
def practitioner_class():
    return Practitioner(practitioner_id='ltc-practitioner-nurse-example')

@pytest.fixture
def profile_urls():
    return ['http://ltc-ig.fhir.tw/StructureDefinition/LTCPractitioner']

@pytest.fixture
def identifiers():
    return [{
        'use': 'official',
        'type': {
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                'code': 'PRN',
                'display': 'Provider Number'
            }]
        },
        'system': 'http://example.org/fhir/NamingSystem/practitioner-id',
        'value': 'N123456789'
    }]

@pytest.fixture
def active():
    return True

@pytest.fixture
def name():
    return [{
        'use': 'official',
        'text': '王美玲',
        'family': '王',
        'given': ['美玲']
    }]

@pytest.fixture
def telecom():
    return [{
        'system': 'phone',
        'value': '02-29412345',
        'use': 'work'
    },
    {
        'system': 'email',
        'value': 'meiling.wang@ltc-center.tw',
        'use': 'work'
    }]

@pytest.fixture
def gender():
    return 'female'

@pytest.fixture
def qualification():
    return [{
        'identifier': [{
            'system': 'http://example.org/fhir/NamingSystem/nursing-license',
            'value': '護理執照123456'
        }],
        'code': {
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '224535009',
                'display': 'Registered nurse'
            }]
        }
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Practitioner',
        'id': 'ltc-practitioner-nurse-example',
        'meta': {
            'profile': ['http://ltc-ig.fhir.tw/StructureDefinition/LTCPractitioner']
        },
        'identifier': [{
            'use': 'official',
            'type': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code': 'PRN',
                    'display': 'Provider Number'
                }]
            },
            'system': 'http://example.org/fhir/NamingSystem/practitioner-id',
            'value': 'N123456789'
        }],
        'active': True,
        'name': [{
            'use': 'official',
            'text': '王美玲',
            'family': '王',
            'given': ['美玲']
        }],
        'telecom': [{
            'system': 'phone',
            'value': '02-29412345',
            'use': 'work'
        },
        {
            'system': 'email',
            'value': 'meiling.wang@ltc-center.tw',
            'use': 'work'
        }],
        'gender': 'female',
        'qualification': [{
            'identifier': [{
                'system': 'http://example.org/fhir/NamingSystem/nursing-license',
                'value': '護理執照123456'
            }],
            'code': {
                'coding': [{
                    'system': 'http://snomed.info/sct',
                    'code': '224535009',
                    'display': 'Registered nurse'
                }]
            }
        }]
    }
