import pytest
from fhir_data_generator import TWCoreComposition as Composition


@pytest.fixture
def composition_class():
    return Composition('com-example')

@pytest.fixture
def profile_urls():
    return [
        'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Composition-twcore',
    ]

@pytest.fixture
def status():
    return 'final'

@pytest.fixture
def type_coding():
    return [{
        'system': 'http://loinc.org',
        'code': '11503-0',
        'display': 'Medical records'
    }]

@pytest.fixture
def category():
    return [{
        'coding': [{
            'system': 'http://loinc.org', 'code': '47039-3'
        }]
    }]

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/pat-example'
    }

@pytest.fixture
def date():
    return '2023-09-10T10:30:00Z'

@pytest.fixture
def author():
    return [{
        'reference': 'Practitioner/pra-dr-example'
    }]

@pytest.fixture
def title():
    return '陳加玲的病摘'

@pytest.fixture
def confidentiality():
    return 'R'

@pytest.fixture
def attester():
    return [{
        'mode': 'personal',
        'time': '2023-09-10T11:00:00Z',
        'party': {
            'reference': 'Practitioner/pra-dr-example'
        }
    }]

@pytest.fixture
def custodian():
    return {
        'reference': 'Organization/org-hosp-example'
    }

@pytest.fixture
def event_code():
    return [{
        'coding': [{
            'system': 'http://terminology.hl7.org/CodeSystem/v3-ActCode',
            'code': 'MEDLIST',
            'display': 'medication list'
        }]
    }]

@pytest.fixture
def event_period():
    return {
        'start': '2023-09-10T08:00:00Z',
        'end': '2023-09-15T09:30:00Z'
    }

@pytest.fixture
def section_entry():
    return [
        {
            'reference': 'Practitioner/pra-dr-example'
        },
        {
            'reference': 'Observation/obs-bloodPressure-example'
        },
        {
            'reference': 'MedicationRequest/med-req-cod-example'
        }
    ]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Composition',
        'id': 'com-example',
        'meta': {
            'profile': [
                'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Composition-twcore'
            ]
        },
        'status': 'final',
        'type': {
            'coding': [
                {
                    'system': 'http://loinc.org',
                    'code': '11503-0',
                    'display': 'Medical records'
                }
            ]
        },
        'category': [
            {
                'coding': [
                    {
                        'system': 'http://loinc.org', 'code': '47039-3'
                    }
                ]
            }
        ],
        'subject': {
            'reference': 'Patient/pat-example'
        },
        'date': '2023-09-10T10:30:00Z',
        'author': [
            {
                'reference': 'Practitioner/pra-dr-example'
            }
        ],
        'title': '陳加玲的病摘',
        'confidentiality': 'R',
        'attester': [
            {
                'mode': 'personal',
                'time': '2023-09-10T11:00:00Z',
                'party': {
                    'reference': 'Practitioner/pra-dr-example'
                }
            }
        ],
        'custodian': {
            'reference': 'Organization/org-hosp-example'
        },
        'event': [
            {
                'code': [
                    {
                        'coding': [
                            {
                                'system': 'http://terminology.hl7.org/CodeSystem/v3-ActCode',
                                'code': 'MEDLIST',
                                'display': 'medication list'
                            }
                        ]
                    }
                ],
                'period': {
                    'start': '2023-09-10T08:00:00Z',
                    'end': '2023-09-15T09:30:00Z'
                }
            }
        ],
        'section': [
            {
                'entry': [
                    {
                        'reference': 'Practitioner/pra-dr-example'
                    },
                    {
                        'reference': 'Observation/obs-bloodPressure-example'
                    },
                    {
                        'reference': 'MedicationRequest/med-req-cod-example'
                    }
                ]
            }
        ]
    }
