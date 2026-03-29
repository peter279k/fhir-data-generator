import pytest
from fhir_data_generator import OrganizationLtc


@pytest.fixture
def organization_class():
    return OrganizationLtc('ltc-organization-example')

@pytest.fixture
def profile_urls():
    return [
        'http://ltc-ig.fhir.tw/StructureDefinition/Organization-twltc',
    ]

@pytest.fixture
def identifiers():
    return [{
        'use': 'usual',
        'type': {
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                'code': 'PRN',
                'display': 'Provider Number'
            }]
        },
        'system': 'http://www.moi.gov.tw',
        'value': '0131060029'
    }]

@pytest.fixture
def active():
    return True

@pytest.fixture
def types():
    return [{
        'coding': [{
            'system': 'http://terminology.hl7.org/CodeSystem/organization-type',
            'code': 'prov',
            'display': 'Healthcare Provider'
        }]
    }]

@pytest.fixture
def name():
    return '新北市私立安康老人長期照顧中心（養護型）'

@pytest.fixture
def telecom():
    return [{
        'system': 'phone',
        'value': '02-29412345',
        'use': 'work'
    },
    {
        'system': 'fax',
        'value': '02-29412346',
        'use': 'work'
    }]

@pytest.fixture
def address():
    return [{
        'use': 'work',
        'type': 'physical',
        'text': '新北市中和區安康路二段123號',
        'line': ['安康路二段123號'],
        'city': '中和區',
        'state': '新北市',
        'postalCode': '23511',
        'country': 'TW'
    }]

@pytest.fixture
def contact():
    return [{
        'purpose': {
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/contactentity-type',
                'code': 'ADMIN',
                'display': 'Administrative'
            }]
        },
        'name': {
            'use': 'official',
            'family': '王',
            'given': ['志明']
        },
        'telecom': [{
            'system': 'phone',
            'value': '02-29412345',
            'use': 'work'
        }]
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Organization',
        'id': 'ltc-organization-example',
        'meta': {
            'profile': ['http://ltc-ig.fhir.tw/StructureDefinition/Organization-twltc']
        },
        'identifier': [{
            'use': 'usual',
            'type': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code': 'PRN',
                    'display': 'Provider Number'
                }]
            },
            'system': 'http://www.moi.gov.tw',
            'value': '0131060029'
        }],
        'active': True,
        'type': [{
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/organization-type',
                'code': 'prov',
                'display': 'Healthcare Provider'
            }]
        }],
        'name': '新北市私立安康老人長期照顧中心（養護型）',
        'telecom': [{
            'system': 'phone',
            'value': '02-29412345',
            'use': 'work'
        },
        {
            'system': 'fax',
            'value': '02-29412346',
            'use': 'work'
        }],
        'address': [{
            'use': 'work',
            'type': 'physical',
            'text': '新北市中和區安康路二段123號',
            'line': ['安康路二段123號'],
            'city': '中和區',
            'state': '新北市',
            'postalCode': '23511',
            'country': 'TW'
        }],
        'contact': [{
            'purpose': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/contactentity-type',
                    'code': 'ADMIN',
                    'display': 'Administrative'
                }]
            },
            'name': {
                'use': 'official',
                'family': '王',
                'given': ['志明']
            },
            'telecom': [{
                'system': 'phone',
                'value': '02-29412345',
                'use': 'work'
            }]
        }]
    }
