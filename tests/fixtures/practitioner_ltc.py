import pytest
from fhir_data_generator import PractitionerLtc as Practitioner


@pytest.fixture
def practitioner_class():
    return Practitioner(practitioner_id='ltc-practitioner-example')

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
                'code': 'MD'
            }]
        },
        'system': 'http://example.org/fhir/NamingSystem/hospital-license',
        'value': 'KMD12345'
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
        'value': '02-87654321',
        'use': 'work'
    },
    {
        'system': 'email',
        'value': 'meiling.wang@ltc-hospital.tw',
        'use': 'work'
    }]

@pytest.fixture
def address():
    return [{
        'use': 'work',
        'type': 'both',
        'text': '台北市大安區復興南路二段201號',
        'line': ['復興南路二段201號'],
        'city': '台北市',
        'district': '大安區',
        'postalCode': '106',
        'country': 'TW'
    }]

@pytest.fixture
def gender():
    return 'female'

@pytest.fixture
def birth_date():
    return '1975-06-10'

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Practitioner',
        'id': 'ltc-practitioner-example',
        'meta': {
            'profile': ['http://ltc-ig.fhir.tw/StructureDefinition/LTCPractitioner']
        },
        'identifier': [{
            'use': 'official',
            'type': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code': 'MD'
                }]
            },
            'system': 'http://example.org/fhir/NamingSystem/hospital-license',
            'value': 'KMD12345'
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
            'value': '02-87654321',
            'use': 'work'
        },
        {
            'system': 'email',
            'value': 'meiling.wang@ltc-hospital.tw',
            'use': 'work'
        }],
        'address': [{
            'use': 'work',
            'type': 'both',
            'text': '台北市大安區復興南路二段201號',
            'line': ['復興南路二段201號'],
            'city': '台北市',
            'district': '大安區',
            'postalCode': '106',
            'country': 'TW'
        }],
        'gender': 'female',
        'birthDate': '1975-06-10'
    }
