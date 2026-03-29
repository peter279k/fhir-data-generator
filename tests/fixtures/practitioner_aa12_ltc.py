import pytest
from fhir_data_generator import PractitionerLtc as Practitioner


@pytest.fixture
def practitioner_class():
    return Practitioner(practitioner_id='ltc-practitioner-physician-aa12-example')

@pytest.fixture
def profile_urls():
    return ['http://ltc-ig.fhir.tw/StructureDefinition/LTCPractitioner']

@pytest.fixture
def identifiers():
    return [{
        'use': 'official',
        'system': 'https://www.tph.mohw.gov.tw',
        'value': 'DR001234'
    },
    {
        'use': 'official',
        'system': 'http://www.immigration.gov.tw',
        'value': 'A123456789'
    }]

@pytest.fixture
def name():
    return [{
        'text': '王醫師',
        'family': '王',
        'given': ['志明'],
        'prefix': ['Dr.']
    }]

@pytest.fixture
def telecom():
    return [{
        'system': 'phone',
        'value': '02-23123456',
        'use': 'work'
    },
    {
        'system': 'email',
        'value': 'dr.wang@hospital.tw',
        'use': 'work'
    }]

@pytest.fixture
def address():
    return [{
        'text': '台北市中正區重慶南路一段122號',
        'line': ['重慶南路一段122號'],
        'city': '台北市',
        'district': '中正區',
        'postalCode': '100',
        'country': 'TW'
    }]

@pytest.fixture
def gender():
    return 'male'

@pytest.fixture
def birth_date():
    return '1975-06-15'

@pytest.fixture
def qualification():
    return [{
        'identifier': [{
            'system': 'https://www.mohw.gov.tw',
            'value': 'MD123456'
        }],
        'code': {
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/v2-0360',
                'code': 'MD',
                'display': 'Doctor of Medicine'
            }]
        },
        'period': {
            'start': '2000-07-01'
        },
        'issuer': {
            'display': '台灣大學醫學院'
        }
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Practitioner',
        'id': 'ltc-practitioner-physician-aa12-example',
        'meta': {
            'profile': ['http://ltc-ig.fhir.tw/StructureDefinition/LTCPractitioner']
        },
        'identifier': [{
            'use': 'official',
            'system': 'https://www.tph.mohw.gov.tw',
            'value': 'DR001234'
        },
        {
            'use': 'official',
            'system': 'http://www.immigration.gov.tw',
            'value': 'A123456789'
        }],
        'name': [{
            'text': '王醫師',
            'family': '王',
            'given': ['志明'],
            'prefix': ['Dr.']
        }],
        'telecom': [{
            'system': 'phone',
            'value': '02-23123456',
            'use': 'work'
        },
        {
            'system': 'email',
            'value': 'dr.wang@hospital.tw',
            'use': 'work'
        }],
        'address': [{
            'text': '台北市中正區重慶南路一段122號',
            'line': ['重慶南路一段122號'],
            'city': '台北市',
            'district': '中正區',
            'postalCode': '100',
            'country': 'TW'
        }],
        'gender': 'male',
        'birthDate': '1975-06-15',
        'qualification': [{
            'identifier': [{
                'system': 'https://www.mohw.gov.tw',
                'value': 'MD123456'
            }],
            'code': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0360',
                    'code': 'MD',
                    'display': 'Doctor of Medicine'
                }]
            },
            'period': {
                'start': '2000-07-01'
            },
            'issuer': {
                'display': '台灣大學醫學院'
            }
        }]
    }
