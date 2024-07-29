import pytest
from fhir_data_generator import OrganizationH


@pytest.fixture
def organization_class():
    return OrganizationH('organization-h-example')

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
            'system': 'https://www.vghtpe.gov.tw',
            'value': '0601160016',
        },
    ]

@pytest.fixture
def type_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/organization-type',
        'code': 'prov',
    }]

@pytest.fixture
def name():
    return '臺北醫院'

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Organization',
        'id': 'organization-h-example',
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
                'system': 'https://www.vghtpe.gov.tw', 'value': '0601160016'
            },
        ],
        'type': [
            {
                'coding': [
                    {
                        'system': 'http://terminology.hl7.org/CodeSystem/organization-type',
                        'code': 'prov'
                    },
                ],
            }
        ],
        'name': '臺北醫院',
    }
