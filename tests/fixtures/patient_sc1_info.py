import uuid
import pytest
from fhir_data_generator import Patient


@pytest.fixture
def patient_class():
    return Patient(patient_id=uuid.uuid4().hex)

@pytest.fixture
def profile_urls():
    return [
        'https://hapi.fhir.tw/fhir/StructureDefinition/MITW-T1-SC1-PatientCore',
    ]

@pytest.fixture
def patient_id():
    return '22526'

@pytest.fixture
def identifiers():
    identifier1 = {
        'use': 'official',
        'system': 'http://www.boca.gov.tw',
        'type': {
            'coding': [
                {
                    'system': 'http://www.boca.gov.tw',
                    'code': 'PPN',
                    'display': 'Passport number',
                },
            ],
        },
        'value': 'E262344368'[2:],
    }
    identifier2 = {
        'use': 'official',
        'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
        'type': {
            'coding': [
                {
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code': 'MR',
                    'display': 'Medical record number',
                },
            ]
        },
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
    profile_urls = ['https://hapi.fhir.tw/fhir/StructureDefinition/MITW-T1-SC1-PatientCore']

    return {
        'resourceType': 'Patient',
        'meta': {
            'profile': profile_urls,
        },
        'identifier': [
            {
                'use': 'official',
                'system': 'http://www.boca.gov.tw',
                'type': {
                    'coding': [
                        {
                            'system': 'http://www.boca.gov.tw',
                            'code': 'PPN',
                            'display': 'Passport number',
                        },
                    ],
                },
                'value': 'E262344368'[2:],
            },
            {
                'use': 'official',
                'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                'type': {
                    'coding': [
                        {
                            'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                            'code': 'MR',
                            'display': 'Medical record number',
                        },
                    ],
                },
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

@pytest.fixture
def update_patient_sc1_payload():
    profile_urls = ['https://hapi.fhir.tw/fhir/StructureDefinition/MITW-T1-SC1-PatientCore']

    return {
        'resourceType': 'Patient',
        'id': '22526',
        'meta': {
            'profile': profile_urls,
        },
        'identifier': [
            {
                'use': 'official',
                'system': 'http://www.boca.gov.tw',
                'type': {
                    'coding': [
                        {
                            'system': 'http://www.boca.gov.tw',
                            'code': 'PPN',
                            'display': 'Passport number',
                        },
                    ],
                },
                'value': 'E262344368'[2:],
            },
            {
                'use': 'official',
                'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                'type': {
                    'coding': [
                        {
                            'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                            'code': 'MR',
                            'display': 'Medical record number',
                        },
                    ],
                },
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
