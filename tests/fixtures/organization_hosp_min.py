import pytest
from fhir_data_generator import TWCoreOrganization as Organization


@pytest.fixture
def organization_class():
    return Organization('OrganizationHosp-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/organization-hosp-imri',
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
        'value': '1101020018'
    }]

@pytest.fixture
def type_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/organization-type',
        'code': 'prov'
    }]

@pytest.fixture
def name():
    return '國泰醫療財團法人國泰綜合醫院'

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Organization',
        'id' : 'OrganizationHosp-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/organization-hosp-imri']
        },
        'identifier' : [{
            'use' : 'official',
            'type' : {
                'coding' : [{
                    'system' : 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code' : 'PRN'
                }]
            },
            'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/organization-identifier-tw',
            'value' : '1101020018'
        }],
        'type' : [{
            'coding' : [{
                'system' : 'http://terminology.hl7.org/CodeSystem/organization-type',
                'code' : 'prov'
            }]
        }],
        'name' : '國泰醫療財團法人國泰綜合醫院'
    }
