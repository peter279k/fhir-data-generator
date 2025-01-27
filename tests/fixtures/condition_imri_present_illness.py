import pytest
from fhir_data_generator import ConditionImri as Condition


@pytest.fixture
def condition_class():
    return Condition('ConditionPresentIllness-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/conditionpresentillness-imri'
    ]

@pytest.fixture
def clinical_status_coding():
    return [{
        'system' : 'http://terminology.hl7.org/CodeSystem/condition-clinical',
        'code' : 'remission',
        'display' : 'Remission'
    }]

@pytest.fixture
def category_coding():
    return [{
        'system' : 'http://loinc.org',
        'code' : '10164-2',
        'display' : 'History of Present illness Narrative'
    }]

@pytest.fixture
def code_coding():
    return [{
        'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-10-cm-2021-tw',
        'code' : 'A15.0',
        'display' : '肺結核'
    }]

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
def expected_payload():
    return {
        'resourceType' : 'Condition',
        'id' : 'ConditionPresentIllness-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/conditionpresentillness-imri']
        },
        'clinicalStatus' : {
            'coding' : [{
                'system' : 'http://terminology.hl7.org/CodeSystem/condition-clinical',
                'code' : 'remission',
                'display' : 'Remission'
            }]
        },
        'category' : [{
            'coding' : [{
                'system' : 'http://loinc.org',
                'code' : '10164-2',
                'display' : 'History of Present illness Narrative'
            }]
        }],
        'code' : {
            'coding' : [{
                'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-10-cm-2021-tw',
                'code' : 'A15.0',
                'display' : '肺結核'
            }]
        },
        'subject' : {
            'reference' : 'Patient/Patient-min'
        },
        'encounter' : {
            'reference' : 'Encounter/Encounter-min'
        }
    }
