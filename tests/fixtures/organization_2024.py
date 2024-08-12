import pytest
from fhir_data_generator import TWCoreOrganization as Organization


@pytest.fixture
def organization_class():
    return Organization('org-hosp-example')

@pytest.fixture
def profile_urls():
    return [
        'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Organization-hosp-twcore',
    ]

@pytest.fixture
def identifiers():
    return [{
        'use': 'official',
        'type': {
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                'code': 'PRN'
            }]
        },
        'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/organization-identifier-tw',
        'value': '0131060029'
    }]

@pytest.fixture
def type_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/organization-type',
        'code': 'prov'
    }]

@pytest.fixture
def name():
    return '衛生福利部臺北醫院'

@pytest.fixture
def telecom():
    return [{
        'system': 'phone',
        'value': '0222765566'
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Organization',
        'id': 'org-hosp-example',
        'meta': {
            'profile': [
                'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Organization-hosp-twcore'
            ]
        },
        'identifier': [{
            'use': 'official',
            'type': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code': 'PRN'
                }]
            },
            'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/organization-identifier-tw',
            'value': '0131060029'
        }],
        'type': [{
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/organization-type',
                'code': 'prov'
            }]
        }],
        'name': '衛生福利部臺北醫院',
        'telecom': [{
            'system': 'phone',
            'value': '0222765566'
        }]
    }
