import pytest
from fhir_data_generator import TWCoreMedicationRequest as MedicationRequest


@pytest.fixture
def medication_request_class():
    return MedicationRequest('MedicationRequest-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/medicationrequest-imri',
    ]

@pytest.fixture
def status():
    return 'active'

@pytest.fixture
def intent():
    return 'proposal'

@pytest.fixture
def medication_codeable_concept():
    return {
        'coding' : [{
            'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medication-nhi-tw',
            'code' : 'A003092100',
            'display' : 'ASPIRIN TABLETS 500MG \'S.Y.\''
        }]
    }

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/Patient-min'
    }

@pytest.fixture
def encounter():
    return {
        'reference': 'Encounter/Encounter-min'
    }

@pytest.fixture
def requester():
    return {
        'reference': 'Practitioner/Practitioner-min'
    }

@pytest.fixture
def performer():
    return {
        'reference' : 'Practitioner/Practitioner-min'
    }

@pytest.fixture
def based_on():
    return [{
        'reference' : 'CarePlan/CarePlan-min'
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'MedicationRequest',
        'id' : 'MedicationRequest-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/medicationrequest-imri']
        },
        'status' : 'active',
        'intent' : 'proposal',
        'medicationCodeableConcept' : {
            'coding' : [{
                'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medication-nhi-tw',
                'code' : 'A003092100',
                'display' : 'ASPIRIN TABLETS 500MG \'S.Y.\''
            }]
        },
        'subject' : {
            'reference' : 'Patient/Patient-min'
        },
        'encounter' : {
            'reference' : 'Encounter/Encounter-min'
        },
        'requester' : {
            'reference' : 'Practitioner/Practitioner-min'
        },
        'performer' : {
            'reference' : 'Practitioner/Practitioner-min'
        },
        'basedOn' : [{
            'reference' : 'CarePlan/CarePlan-min'
        }]
    }
