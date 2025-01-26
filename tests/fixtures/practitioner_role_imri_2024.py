import pytest
from fhir_data_generator import TWCorePractitionerRole as PractitionerRole


@pytest.fixture
def practitioner_role_class():
    return PractitionerRole(practitioner_role_id='PractitionerRole-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/practitionerrole-imri'
    ]

@pytest.fixture
def practitioner():
    return {
        'reference': 'Practitioner/Practitioner-min',
        'display': '劉伊詩',
    }

@pytest.fixture
def code():
    return [{
        'coding' : [{
            'system' : 'http://snomed.info/sct',
            'code' : '304292004',
            'display' : 'Surgeon'
        }]
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'PractitionerRole',
        'id' : 'PractitionerRole-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/practitionerrole-imri']
        },
        'practitioner' : {
            'reference' : 'Practitioner/Practitioner-min',
            'display' : '劉伊詩'
        },
        'code' : [{
            'coding' : [{
                'system' : 'http://snomed.info/sct',
                'code' : '304292004',
                'display' : 'Surgeon'
            }]
        }]
    }
