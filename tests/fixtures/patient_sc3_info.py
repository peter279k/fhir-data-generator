import pytest
from fhir_data_generator import Patient


@pytest.fixture
def patient_class():
    return Patient()

@pytest.fixture
def profile_urls():
    return [
        'https://hapi.fhir.tw/fhir/StructureDefinition/Patient-MITW2022-T1SC3',
    ]

@pytest.fixture
def identifiers():
    identifier1 = {
        'use': 'official',
        'type': {
            'coding': [
                {
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code': 'NI',
                },
            ],
        },
        'system': 'http://www.moi.gov.tw/',
        'value': 'M123456789',
    }
    identifier2 = {
        'use': 'official',
        'type': {
            'coding': [
                {
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code': 'MR',
                },
            ]
        },
        'system': 'https://www.tph.mohw.gov.tw/',
        'value': '123456789',
    }

    return [identifier1, identifier2]

@pytest.fixture
def active():
    return True

@pytest.fixture
def managing_organization():
    return 'Organization/MITW.ForPHR'

@pytest.fixture
def patient_sc3_payload():
    profile_urls = ['https://hapi.fhir.tw/fhir/StructureDefinition/Patient-MITW2022-T1SC3']

    return {
        'resourceType': 'Patient',
        'meta': {
            'profile': profile_urls,
        },
        'identifier': [
            {
                'use': 'official',
                'type': {
                    'coding': [
                        {
                            'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                            'code': 'NI',
                        },
                    ],
                },
                'system': 'http://www.moi.gov.tw/',
                'value': 'M123456789',
            },
            {
                'use': 'official',
                'type': {
                    'coding': [
                        {
                            'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                            'code': 'MR',
                        },
                    ]
                },
                'system': 'https://www.tph.mohw.gov.tw/',
                'value': '123456789',
            },
        ],
        'active': True,
        'managingOrganization': {
            'reference': 'Organization/MITW.ForPHR',
        },
    }
