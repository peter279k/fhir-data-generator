import pytest
from fhir_data_generator import Patient


@pytest.fixture
def patient_class():
    return Patient()

@pytest.fixture
def profile_urls():
    return [
        'https://hapi.fhir.tw/fhir/StructureDefinition/Patient-MITW2022-T1SC2',
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
                }
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
            ],
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
    return 'Organization/MITW.ForContact'

@pytest.fixture
def names():
    return [
        {
            'use': 'official',
            'family': 'Li',
            'given': [
                'Peter'
            ],
            'text': 'Peter Li'
        },
    ]

@pytest.fixture
def addresses():
    return [
        {
            'text': '8F, No.133, Sec.4 MingSheng E. Rd, Taipei City 105, Taiwan.',
            'line': [
                ''
            ],
            'city': 'Taipei',
            'district': '',
            'postalCode': '105',
            'country': 'Taiwan',
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
            'system': 'phone',
            'value': '0905285349',
            'use': 'mobile',
        },
        {
            'system': 'email',
            'value': 'peter279k@gmail.com',
        },
        {
            'system': 'url',
            'value': '',
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
                    'text': 'Contact Person'
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
                {
                  'system': 'url',
                  'value': '',
                },
            ],
            'address': {
                'text': '8F, No.133, Sec.4 MingSheng E. Rd, Taipei City 105, Taiwan.',
                'line': [
                    ''
                ],
                'city': 'Taipei',
                'district': '',
                'postalCode': '105',
                'country': 'Taiwan',
            },
         },
    ]

@pytest.fixture
def patient_sc2_payload():
    profile_urls = ['https://hapi.fhir.tw/fhir/StructureDefinition/Patient-MITW2022-T1SC2']

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
                        }
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
                    ],
                },
                'system': 'https://www.tph.mohw.gov.tw/',
                'value': '123456789',
            },
        ],
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
            {
                'system': 'url',
                'value': '',
            },
        ],
        'address': [
            {
                'text': '8F, No.133, Sec.4 MingSheng E. Rd, Taipei City 105, Taiwan.',
                'line': [''],
                    'city': 'Taipei',
                    'district': '',
                    'postalCode': '105',
                    'country': 'Taiwan',
            },
        ],
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
                        'text': 'Contact Person'
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
                    {
                        'system': 'url',
                        'value': '',
                    },
                ],
                'address': {
                    'text': '8F, No.133, Sec.4 MingSheng E. Rd, Taipei City 105, Taiwan.',
                    'line': [''],
                    'city': 'Taipei',
                    'district': '',
                    'postalCode': '105',
                    'country': 'Taiwan',
                },
            },
        ],
        'active': True,
        'managingOrganization': {
            'reference': 'Organization/MITW.ForContact'
        },
        'name': [
            {
                'use': 'official',
                'family': 'Li',
                'given': [
                    'Peter'
                ],
                'text': 'Peter Li'
            },
        ],
        'birthDate': '2023-12-13',
        'gender': 'male',
    }
