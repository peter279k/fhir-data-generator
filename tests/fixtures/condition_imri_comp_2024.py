import pytest
from fhir_data_generator import ConditionImri as Condition


@pytest.fixture
def condition_class():
    return Condition('ConditionChiefComplaint-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/conditionchiefcomplaint-imri'
    ]

@pytest.fixture
def clinical_status_coding():
    return [{
        'system' : 'http://terminology.hl7.org/CodeSystem/condition-clinical',
        'code' : 'active',
        'display' : 'Active'
    }]

@pytest.fixture
def category_coding():
    return [{
        'system' : 'http://loinc.org',
        'code' : '10154-3',
        'display' : 'Chief complaint Narrative - Reported'
    }]

@pytest.fixture
def code_coding():
    return [{
        'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-10-cm-2021-tw',
        'code' : 'K62.5',
        'display' : '肛門及直腸出血'
    }]

@pytest.fixture
def code_text():
    return '肛門及直腸出血'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/Patient-min'
    }

@pytest.fixture
def encounter():
    return {
        'reference': 'Encounter/Encounter-min',
    }

@pytest.fixture
def note():
    return [{
        'text' : 'Anal pain with anal bleeding for few days'
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Condition',
        'id' : 'ConditionChiefComplaint-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/conditionchiefcomplaint-imri']
        },
        'clinicalStatus' : {
            'coding' : [{
                'system' : 'http://terminology.hl7.org/CodeSystem/condition-clinical',
                'code' : 'active',
                'display' : 'Active'
            }]
        },
        'category' : [{
            'coding' : [{
                'system' : 'http://loinc.org',
                'code' : '10154-3',
                'display' : 'Chief complaint Narrative - Reported'
            }]
        }],
        'code' : {
            'coding' : [{
                'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-10-cm-2021-tw',
                'code' : 'K62.5',
                'display' : '肛門及直腸出血'
            }],
            'text' : '肛門及直腸出血'
        },
        'subject' : {
            'reference' : 'Patient/Patient-min'
        },
        'encounter' : {
            'reference' : 'Encounter/Encounter-min'
        },
        'note' : [{
            'text' : 'Anal pain with anal bleeding for few days'
        }]
    }
