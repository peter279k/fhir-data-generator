import uuid
import pytest
from fhir_data_generator import Patient


@pytest.fixture
def patient_class():
    return Patient(str(uuid.uuid4()))

@pytest.fixture
def profile_urls():
    return [
        'https://hapi.fhir.tw/fhir/StructureDefinition/MITW-T1-SC3-PatientContact',
    ]

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
def gender():
    return 'male'

@pytest.fixture
def birth_date():
    return '2023-12-13'

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
def contacts():
    return [
        {
            'relationship': [
                {
                    'coding': [
                        {
                          'system': 'http://terminology.hl7.org/CodeSystem/v2-0131',
                            'code': 'CP',
                        },
                    ],
                    'text': 'Contact person',
                },
            ],
            'name': {
                'text': 'Peter Li',
                'family': 'Li',
                'given': [
                    'Peter',
                ],
            },
            'telecom': [
                {
                  'system': 'phone',
                  'value': '0905285349',
                  'use': 'mobile',
                },
                {
                  'system': 'email',
                  'value': 'peter279k@gmail.com',
                },
            ],
         },
    ]

@pytest.fixture
def active():
    return True

@pytest.fixture
def managing_organization():
    return 'Organization/MITW.ForPHR'

@pytest.fixture
def patient_sc3_payload():
    profile_urls = ['https://hapi.fhir.tw/fhir/StructureDefinition/MITW-T1-SC3-PatientContact']

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
            'reference': 'Organization/MITW.ForPHR',
        },
        'birthDate': '2023-12-13',
        'gender': 'male',
        'contact': [
            {
                'relationship': [
                    {
                        'coding': [
                            {
                                'system': 'http://terminology.hl7.org/CodeSystem/v2-0131',
                                'code': 'CP',
                            },
                        ],
                        'text': 'Contact person',
                    },
                ],
                'name': {
                    'text': 'Peter Li',
                    'family': 'Li',
                    'given': [
                        'Peter',
                    ],
                },
                'telecom': [
                    {
                        'system': 'phone',
                        'value': '0905285349',
                        'use': 'mobile',
                    },
                    {
                        'system': 'email',
                        'value': 'peter279k@gmail.com',
                    },
                ],
            },
        ],
        'address': [
            {
                'use': 'home',
                'text': '105台北市松山區民生東路四段133號',
            },
            {
                'country': 'TW',
            },
        ],
    }

@pytest.fixture
def update_patient_sc3_payload():
    profile_urls = ['https://hapi.fhir.tw/fhir/StructureDefinition/MITW-T1-SC3-PatientContact']

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
        'birthDate': '2023-12-13',
        'gender': 'male',
        'managingOrganization': {
            'reference': 'Organization/MITW.ForPHR',
        },
        'contact': [
            {
                'relationship': [
                    {
                        'coding': [
                            {
                                'system': 'http://terminology.hl7.org/CodeSystem/v2-0131',
                                'code': 'CP',
                            },
                        ],
                        'text': 'Contact person',
                    },
                ],
                'name': {
                    'text': 'Peter Li',
                    'family': 'Li',
                    'given': [
                        'Peter',
                    ],
                },
                'telecom': [
                    {
                        'system': 'phone',
                        'value': '0905285349',
                        'use': 'mobile',
                    },
                    {
                        'system': 'email',
                        'value': 'peter279k@gmail.com',
                    },
                ],
            },
        ],
        'address': [
            {
                'use': 'home',
                'text': '105台北市松山區民生東路四段133號',
            },
            {
                'country': 'TW',
            },
        ],
    }
