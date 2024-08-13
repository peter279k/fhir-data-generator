import pytest
from fhir_data_generator import TWCorePractitionerRole as PractitionerRole


@pytest.fixture
def practitioner_role_class():
    return PractitionerRole(practitioner_role_id='praro-dr-example')

@pytest.fixture
def profile_urls():
    return [
        'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/PractitionerRole-twcore'
    ]

@pytest.fixture
def identifiers():
    return [{
        'use': 'official',
        'type': {
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                'code': 'MD'
            }]
        },
        'system': 'https://www.tph.mohw.gov.tw',
        'value': 'KP00017'
    }]

@pytest.fixture
def active():
    return True

@pytest.fixture
def period():
      return {
        'start': '2022-07-31',
        'end': '2024-07-31'
    }

@pytest.fixture
def practitioner():
    return {
        'reference': 'Practitioner/pra-dr-example',
        'display': '王依昇'
    }

@pytest.fixture
def code():
    return [{
        'coding': [{
            'system': 'http://snomed.info/sct',
            'code': '394802001',
            'display': 'General medicine'
        }]
    }]

@pytest.fixture
def specialty_coding():
    return [{
        'system': 'http://snomed.info/sct',
        'code': '418960008',
        'display': 'Otolaryngology'
    }]

@pytest.fixture
def location():
    return [{
        'reference': 'Location/loc-ent-example',
        'display': '衛生福利部臺北醫院耳鼻喉科'
    }]

@pytest.fixture
def telecom():
    return [{
        'system': 'phone',
        'value': '0993277826',
        'use': 'mobile'
    }]

@pytest.fixture
def available_time():
    return [{
        'daysOfWeek': ['mon', 'tue', 'wed', 'thu', 'fri'],
        'allDay': False,
        'availableStartTime': '08:00:00',
        'availableEndTime': '16:00:00'
    }]

@pytest.fixture
def not_available():
    return [{
        'description': '家中有事請假',
        'during': {
            'start': '2023-08-01',
            'end': '2023-08-15'
        }
    }]

@pytest.fixture
def availability_exceptions():
    return '若遇到緊急狀況可能會影響工作日'

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'PractitionerRole',
        'id': 'praro-dr-example',
        'meta': {
            'profile': [
                'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/PractitionerRole-twcore'
            ]
        },
        'identifier': [{
            'use': 'official',
            'type': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code': 'MD'
                }]
            },
            'system': 'https://www.tph.mohw.gov.tw',
            'value': 'KP00017'
        }],
        'active': True,
        'period': {
            'start': '2022-07-31',
            'end': '2024-07-31'
        },
        'practitioner': {
            'reference': 'Practitioner/pra-dr-example',
            'display': '王依昇'
        },
        'code': [{
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '394802001',
                'display': 'General medicine'
            }]
        }],
        'specialty': [{
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '418960008',
                'display': 'Otolaryngology'
            }]
        }],
        'location': [{
            'reference': 'Location/loc-ent-example',
            'display': '衛生福利部臺北醫院耳鼻喉科'
        }],
        'telecom': [{
            'system': 'phone',
            'value': '0993277826',
            'use': 'mobile'
        }],
        'availableTime': [{
            'daysOfWeek': ['mon', 'tue', 'wed', 'thu', 'fri'],
            'allDay': False,
            'availableStartTime': '08:00:00',
            'availableEndTime': '16:00:00'
        }],
        'notAvailable': [{
            'description': '家中有事請假',
            'during': {
                'start': '2023-08-01',
                'end': '2023-08-15'
            }
        }],
        'availabilityExceptions': '若遇到緊急狀況可能會影響工作日'
    }
