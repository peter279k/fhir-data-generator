import pytest
from fhir_data_generator import PractitionerRoleLtc as PractitionerRole


@pytest.fixture
def practitioner_role_class():
    return PractitionerRole(practitioner_role_id='ltc-practitioner-role-nurse-example')

@pytest.fixture
def profile_urls():
    return [
        'http://ltc-ig.fhir.tw/StructureDefinition/LTCPractitionerRole'
    ]

@pytest.fixture
def active():
    return True

@pytest.fixture
def practitioner():
    return {
        'reference': 'Practitioner/ltc-practitioner-nurse-example'
    }

@pytest.fixture
def organization():
    return {
        'reference': 'Organization/ltc-organization-example'
    }

@pytest.fixture
def code():
    return [{
        'coding': [{
            'system': 'http://snomed.info/sct',
            'code': '224535009',
            'display': 'Registered nurse'
        }]
    }]

@pytest.fixture
def specialty():
    return [{
        'coding': [{
            'system': 'http://snomed.info/sct',
            'code': '394609007',
            'display': 'General surgery (qualifier value)'
        }]
    }]

@pytest.fixture
def telecom():
    return [{
        'system': 'phone',
        'value': '02-29412345',
        'use': 'work'
    },
    {
        'system': 'email',
        'value': 'meiling.wang@ltc-center.tw',
        'use': 'work'
    }]

@pytest.fixture
def available_time():
    return [{
        'daysOfWeek': [
            'mon',
            'tue',
            'wed',
            'thu',
            'fri'
        ],
        'availableStartTime': '08:00:00',
        'availableEndTime': '17:00:00'
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'PractitionerRole',
        'id': 'ltc-practitioner-role-nurse-example',
        'meta': {
            'profile': ['http://ltc-ig.fhir.tw/StructureDefinition/LTCPractitionerRole']
        },
        'active': True,
        'practitioner': {
            'reference': 'Practitioner/ltc-practitioner-nurse-example'
        },
        'organization': {
            'reference': 'Organization/ltc-organization-example'
        },
        'code': [{
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '224535009',
                'display': 'Registered nurse'
            }]
        }],
        'specialty': [{
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '394609007',
                'display': 'General surgery (qualifier value)'
            }]
        }],
        'telecom': [{
            'system': 'phone',
            'value': '02-29412345',
            'use': 'work'
        },
        {
            'system': 'email',
            'value': 'meiling.wang@ltc-center.tw',
            'use': 'work'
        }],
        'availableTime': [{
            'daysOfWeek': [
                'mon',
                'tue',
                'wed',
                'thu',
                'fri'
            ],
            'availableStartTime': '08:00:00',
            'availableEndTime': '17:00:00'
        }]
    }
