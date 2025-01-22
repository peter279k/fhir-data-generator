import pytest
from fhir_data_generator import TWCorePractitionerRole as PractitionerRole


@pytest.fixture
def practitioner_role_class():
    return PractitionerRole(practitioner_role_id='PractitionerRole-pri')

@pytest.fixture
def profile_urls():
    return [
        'https://claim.cgh.org.tw/iclaim/StructureDefinition/practitionerrole-iclaim'
    ]

@pytest.fixture
def practitioner():
    return {
        'reference': 'Practitioner/Practitioner-Chen',
        'display': '陳健骨',
    }

@pytest.fixture
def code():
    return [{
        'coding': [{
            'system': 'http://snomed.info/sct',
            'code': '405279007',
            'display': 'Attending physician (occupation)'
        }]
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'PractitionerRole',
        'id' : 'PractitionerRole-pri',
        'meta' : {
            'profile' : ['https://claim.cgh.org.tw/iclaim/StructureDefinition/practitionerrole-iclaim']
        },
        'practitioner' : {
            'reference' : 'Practitioner/Practitioner-Chen',
            'display' : '陳健骨'
        },
        'code' : [{
            'coding' : [{
                'system' : 'http://snomed.info/sct',
                'code' : '405279007',
                'display' : 'Attending physician (occupation)'
            }]
        }]
    }
