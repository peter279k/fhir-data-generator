import pytest
from fhir_data_generator import Patient


@pytest.fixture
def patient_class():
    return Patient()

@pytest.fixture
def profile_urls():
    return [
        'https://hapi.fhir.tw/fhir/StructureDefinition/Patient-MITW2022-T1SC1',
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
        'value': 'E262344368',
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
def inactive():
    return False

@pytest.fixture
def active():
    return True

@pytest.fixture
def managing_organization():
    return 'Organization/MITW.ForIdentifier'

@pytest.fixture
def names():
    return [
        {
            'use': 'official',
            'text': '李小明',
            'family': '李',
            'given': ['小明'],
        },
    ]

@pytest.fixture
def addresses():
    return [
        {
            'use': 'home',
            'text': '105台北市松山區民生東路四段133號',
        },
        {
            'country': 'TW',
        },
    ]

@pytest.fixture
def gender():
    return 'male'

@pytest.fixture
def birth_date():
    return '2023-12-13'

@pytest.fixture
def telecoms():
    return [
        {
            'use': 'home',
            'system': 'phone',
            'value': '0905285349',
        },
    ]

@pytest.fixture
def patient_sc1_payload():
    profile_urls = ['https://hapi.fhir.tw/fhir/StructureDefinition/Patient-MITW2022-T1SC1']

    return  {
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
                'value': 'E262344368',
            },
            {
                'use': 'official',
                'type': {
                    'coding': [
                        {
                            'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                            'code': 'MR',
                        },
                    ],
                },
                'system': 'https://www.tph.mohw.gov.tw/',
                'value': '123456789',
            },
        ],
        'active': True,
        'managingOrganization': {
            'reference': 'Organization/MITW.ForIdentifier',
        },
        'name': [
            {
                'use': 'official',
                'text': '李小明',
                'family': '李',
                'given': ['小明'],
            },
        ],
        'gender': 'male',
        'birthDate': '2023-12-13',
        'address': [
            {
                'use': 'home',
                'text': '105台北市松山區民生東路四段133號',
            },
            {
                'country': 'TW',
            },
        ],
        'telecom': [
            {
                'use': 'home',
                'system': 'phone',
                'value': '0905285349',
            },
        ],
    }
