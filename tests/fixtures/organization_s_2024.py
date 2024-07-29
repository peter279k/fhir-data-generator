import pytest
from fhir_data_generator import OrganizationS


@pytest.fixture
def organization_class():
    return OrganizationS('organization-s-example')

@pytest.fixture
def profile_urls():
    return [
        'https://hapi.fhir.tw/fhir/StructureDefinition/TWCoreOrganization',
    ]

@pytest.fixture
def identifiers():
    return [
        {
            'use': 'official',
            'type': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code': 'PRN'
                }],
            },
            'system': 'https://www.morefit.com.tw',
            'value': '85037366',
        },
    ]

@pytest.fixture
def type_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/organization-type',
        'code': 'team',
    }]

@pytest.fixture
def name():
    return 'morefit'

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Organization',
        'id': 'organization-s-example',
        'meta': {
            'profile': ['https://hapi.fhir.tw/fhir/StructureDefinition/TWCoreOrganization']
        },
        'identifier': [
            {
                'use': 'official',
                'type': {
                    'coding': [{
                        'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                        'code': 'PRN'
                    }]
                },
                'system': 'https://www.morefit.com.tw',
                'value': '85037366',
            },
        ],
        'type': [
            {
                'coding': [
                    {
                        'system': 'http://terminology.hl7.org/CodeSystem/organization-type',
                        'code': 'team'
                    },
                ],
            }
        ],
        'name': 'morefit',
    }
