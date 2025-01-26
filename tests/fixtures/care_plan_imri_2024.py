import pytest
from fhir_data_generator import CarePlanImri as CarePlan


@pytest.fixture
def care_plan_class():
    return CarePlan('CarePlan-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/careplan-imri',
    ]

@pytest.fixture
def status():
    return 'completed'

@pytest.fixture
def intent():
    return 'proposal'

@pytest.fixture
def description():
    return '出院指示'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/Patient-min',
    }

@pytest.fixture
def encounter():
    return {
        'reference': 'Encounter/Encounter-min',
    }

@pytest.fixture
def activity():
    return [{
        'reference' : {
            'reference' : 'MedicationRequest/MedicationRequest-min'
        }
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'CarePlan',
        'id' : 'CarePlan-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/careplan-imri']
        },
        'status' : 'completed',
        'intent' : 'proposal',
        'description' : '出院指示',
        'subject' : {
            'reference' : 'Patient/Patient-min'
        },
        'encounter' : {
            'reference' : 'Encounter/Encounter-min'
        },
        'activity' : [{
            'reference' : {
                'reference' : 'MedicationRequest/MedicationRequest-min'
            }
        }]
    }
