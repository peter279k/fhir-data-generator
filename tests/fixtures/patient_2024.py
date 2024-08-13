import base64
import pytest
from fhir_data_generator import TWCorePatient as Patient


@pytest.fixture
def patient_class():
    return Patient('pat-example')

@pytest.fixture
def profile_urls():
    return [
        'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Patient-twcore',
    ]

@pytest.fixture
def extension_url():
    return 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/person-age'

@pytest.fixture
def extension_value_age():
    return {
        'value': 32,
        'system': 'http://unitsofmeasure.org',
        'code': 'a'
    }

@pytest.fixture
def extension_extension_coding():
    return [{
        'system': 'urn:iso:std:iso:3166',
        'code': 'TW'
    }]

@pytest.fixture
def extension_extension_url():
    return 'http://hl7.org/fhir/StructureDefinition/patient-nationality'

@pytest.fixture
def identifiers():
    return [
        {
            'use': 'official',
            'type': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code': 'NNxxx',
                    '_code': {
                        'extension': [{
                            'extension': [
                                {
                                    'url': 'suffix',
                                    'valueString': 'TWN'
                                },
                                {
                                    'url': 'valueSet',
                                    'valueCanonical': 'http://hl7.org/fhir/ValueSet/iso3166-1-3'
                                }
                            ],
                            'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/identifier-suffix'
                        }]
                    }
                }]
            },
            'system': 'http://www.moi.gov.tw',
            'value': 'A123456789'
        },
        {
            'use': 'official',
            'type': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code': 'MR'
                }]
            },
            'system': 'https://www.tph.mohw.gov.tw/',
            'value': '8862168'
        }
    ]

@pytest.fixture
def active():
    return True

@pytest.fixture
def name_use():
    return 'official'

@pytest.fixture
def name_text():
    return '陳加玲'

@pytest.fixture
def name_family():
    return 'Chen'

@pytest.fixture
def name_given():
    return ['Chia Lin']

@pytest.fixture
def telecom():
    return [{
        'system': 'phone',
        'value': '0911327999',
        'use': 'mobile',
        'period': {
            'start': '2022-07-31',
            'end': '2024-07-31'
        }
    }]

@pytest.fixture
def gender():
    return 'female'

@pytest.fixture
def birth_date():
    return '1990-01-01'

@pytest.fixture
def address_extension():
    return [
        {
            'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-section',
            'valueString': '三段'
        },
        {
            'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-number',
            'valueString': '210號'
        },
        {
            'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-village',
            'valueString': '大有里'
        },
        {
            'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-neighborhood',
            'valueString': '19鄰'
        },
        {
            'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-lane',
            'valueString': '52巷'
        },
        {
            'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-alley',
            'valueString': '6弄'
        },
        {
            'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-floor',
            'valueString': '2樓'
        },
        {
            'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-room',
            'valueString': 'B室'
        }
    ]

@pytest.fixture
def address_text():
    return '臺北市大同區大有里19鄰承德路三段52巷6弄210號2樓B室'

@pytest.fixture
def address_line():
    return ['承德路']

@pytest.fixture
def address_city():
    return '臺北市'

@pytest.fixture
def address_district():
    return '大同區'

@pytest.fixture
def address_postal_code_extension():
    return [{
        'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-postal-code',
        'valueCodeableConcept': {
            'coding': [{
                'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/postal-code3-tw',
                'code': '103'
            }]
        }
    }]

@pytest.fixture
def marital_status_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/v3-MaritalStatus',
        'code': 'U'
    }]

@pytest.fixture
def photo():
    with open('./tests/fixtures/patient_2024.png', 'rb') as f:
        contents = f.read()

    encoded_image = base64.b64encode(contents)
    encoded_image = encoded_image.decode('utf-8')

    return [{
        'contentType': 'image/jpeg',
        'data': f'{encoded_image}',
        'url': 'patient.png'
    }]

@pytest.fixture
def contact():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/v3-RoleCode',
        'code': 'FTH'
    }]

@pytest.fixture
def contact_name():
    return {
        'use': 'official',
        'text': '李立偉',
        'family': 'Li',
        'given': ['Li Wei']
    }

@pytest.fixture
def contact_telecom():
    return [{
        'system': 'phone',
        'value': '0917159753',
        'use': 'mobile',
        'period': {
            'start': '2022-07-31',
            'end': '2024-07-31'
        }
    }]

@pytest.fixture
def communication_language_coding():
    return [{
        'system': 'urn:ietf:bcp:47', 'code': 'zh-TW'
    }]

@pytest.fixture
def managing_organization():
    return {
        'reference': 'Organization/org-hosp-example'
    }

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Patient',
        'id': 'pat-example',
        'meta': {
            'profile': [
                'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Patient-twcore'
            ]
        },
        'extension': [
            {
                'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/person-age',
                'valueAge': {
                    'value': 32,
                    'system': 'http://unitsofmeasure.org',
                    'code': 'a'
                }
            },
            {
                'extension': [{
                    'url': 'code',
                    'valueCodeableConcept': {
                        'coding': [{
                            'system': 'urn:iso:std:iso:3166',
                            'code': 'TW'
                        }]
                    }
                }],
                'url': 'http://hl7.org/fhir/StructureDefinition/patient-nationality'
            }
        ],
        'identifier': [
            {
                'use': 'official',
                'type': {
                    'coding': [{
                        'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                        'code': 'NNxxx',
                        '_code': {
                            'extension': [{
                                'extension': [
                                    {
                                        'url': 'suffix',
                                        'valueString': 'TWN'
                                    },
                                    {
                                        'url': 'valueSet',
                                        'valueCanonical': 'http://hl7.org/fhir/ValueSet/iso3166-1-3'
                                    }
                                ],
                                'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/identifier-suffix'
                            }]
                        }
                    }]
                },
                'system': 'http://www.moi.gov.tw',
                'value': 'A123456789'
            },
            {
                'use': 'official',
                'type': {
                    'coding': [{
                        'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                        'code': 'MR'
                    }]
                },
                'system': 'https://www.tph.mohw.gov.tw/',
                'value': '8862168'
            }
        ],
        'active': True,
        'name': [{
            'use': 'official',
            'text': '陳加玲',
            'family': 'Chen',
            'given': ['Chia Lin']
        }],
        'telecom': [{
            'system': 'phone',
            'value': '0911327999',
            'use': 'mobile',
            'period': {
                'start': '2022-07-31',
                'end': '2024-07-31'
            }
        }],
        'gender': 'female',
        'birthDate': '1990-01-01',
        'address': [{
            'extension': [
                {
                    'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-section',
                    'valueString': '三段'
                },
                {
                    'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-number',
                    'valueString': '210號'
                },
                {
                    'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-village',
                    'valueString': '大有里'
                },
                {
                    'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-neighborhood',
                    'valueString': '19鄰'
                },
                {
                    'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-lane',
                    'valueString': '52巷'
                },
                {
                    'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-alley',
                    'valueString': '6弄'
                },
                {
                    'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-floor',
                    'valueString': '2樓'
                },
                {
                    'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-room',
                    'valueString': 'B室'
                }
            ],
            'text': '臺北市大同區大有里19鄰承德路三段52巷6弄210號2樓B室',
            'line': ['承德路'],
            'city': '臺北市',
            'district': '大同區',
            '_postalCode': {
                'extension': [{
                    'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-postal-code',
                    'valueCodeableConcept': {
                        'coding': [{
                            'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/postal-code3-tw',
                            'code': '103'
                        }
                    ]}
                }]
            },
            'country': 'TW'
        }],
        'maritalStatus': {
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/v3-MaritalStatus',
                'code': 'U'
            }]
        },
        'photo': [{
            'contentType': 'image/jpeg',
            'data': 'R0lGODlhEwARAPcAAAAAAAAA/+9aAO+1AP/WAP/eAP/eCP/eEP/eGP/nAP/nCP/nEP/nIf/nKf/nUv/nWv/vAP/vCP/vEP/vGP/vIf/vKf/vMf/vOf/vWv/vY//va//vjP/3c//3lP/3nP//tf//vf///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////yH5BAEAAAEALAAAAAATABEAAAi+AAMIDDCgYMGBCBMSvMCQ4QCFCQcwDBGCA4cLDyEGECDxAoAQHjxwyKhQAMeGIUOSJJjRpIAGDS5wCDly4AALFlYOgHlBwwOSNydM0AmzwYGjBi8IHWoTgQYORg8QIGDAwAKhESI8HIDgwQaRDI1WXXAhK9MBBzZ8/XDxQoUFZC9IiCBh6wEHGz6IbNuwQoSpWxEgyLCXL8O/gAnylNlW6AUEBRIL7Og3KwQIiCXb9HsZQoIEUzUjNEiaNMKAAAA7',
            'url': 'patient.png'
        }],
        'contact': [{
            'relationship': [{
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v3-RoleCode',
                    'code': 'FTH'
                }]
            }],
            'name': {
                'use': 'official',
                'text': '李立偉',
                'family': 'Li',
                'given': ['Li Wei']
            },
            'telecom': [{
                'system': 'phone',
                'value': '0917159753',
                'use': 'mobile',
                'period': {
                    'start': '2022-07-31',
                    'end': '2024-07-31'
                }
            }]
        }],
        'communication': [{
            'language': {
                'coding': [{
                    'system': 'urn:ietf:bcp:47', 'code': 'zh-TW'
                }]
            }
        }],
        'managingOrganization': {
            'reference': 'Organization/org-hosp-example'
        }
    }
