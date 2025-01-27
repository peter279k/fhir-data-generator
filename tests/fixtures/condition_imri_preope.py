import pytest
from fhir_data_generator import ConditionImri as Condition


@pytest.fixture
def condition_class():
    return Condition('Condition-preope')

@pytest.fixture
def profile_urls():
    return [
        'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Condition-twcore'
    ]

@pytest.fixture
def clinical_status_coding():
    return [{
        'system' : 'http://terminology.hl7.org/CodeSystem/condition-clinical',
        'code' : 'remission'
    }]

@pytest.fixture
def category_coding():
    return [{
        'system' : 'http://terminology.hl7.org/CodeSystem/condition-category',
        'code' : 'encounter-diagnosis'
    }]

@pytest.fixture
def code_coding():
    return [{
        'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-10-cm-2021-tw',
        'code' : 'K82.4'
    }]

@pytest.fixture
def code_text():
    return '膽囊膽固醇沈著症'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/Patient-min'
    }

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Condition',
        'id' : 'Condition-preope',
        'meta' : {
            'profile' : ['https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Condition-twcore']
        },
        'clinicalStatus' : {
            'coding' : [{
                'system' : 'http://terminology.hl7.org/CodeSystem/condition-clinical',
                'code' : 'remission'
            }]
        },
        'category' : [{
            'coding' : [{
                'system' : 'http://terminology.hl7.org/CodeSystem/condition-category',
                'code' : 'encounter-diagnosis'
            }]
        }],
        'code' : {
            'coding' : [{
                'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-10-cm-2021-tw',
                'code' : 'K82.4'
            }],
            'text' : '膽囊膽固醇沈著症'
        },
        'subject' : {
            'reference' : 'Patient/Patient-min'
        }
    }
