import pytest
from fhir_data_generator import TWCoreOrganization as Organization


@pytest.fixture
def organization_class():
    return Organization('Organization-cathay')

@pytest.fixture
def profile_urls():
    return [
        'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Organization-co-twcore',
    ]

@pytest.fixture
def identifiers():
    return [{
        'use': 'official',
        'type': {
            'coding': [{
                'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/v2-0203',
                'code': 'UBN'
            }]
        },
        'system': 'https://gcis.nat.gov.tw',
        'value': '03374707'
    }]

@pytest.fixture
def type_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/organization-type',
        'code': 'bus'
    }]

@pytest.fixture
def name():
    return '國泰人壽保險股份有限公司'

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Organization',
        'id' : 'Organization-cathay',
        'meta' : {
            'profile' : ['https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Organization-co-twcore']
        },
        'identifier' : [{
            'use' : 'official',
            'type' : {
                'coding' : [{
                    'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/v2-0203',
                    'code' : 'UBN'
                }]
            },
            'system' : 'https://gcis.nat.gov.tw',
            'value' : '03374707'
        }],
        'type' : [{
            'coding' : [{
                'system' : 'http://terminology.hl7.org/CodeSystem/organization-type',
                'code' : 'bus'
            }]
        }],
        'name' : '國泰人壽保險股份有限公司'
    }
