import pytest
from fhir_data_generator import ConditionImri as Condition


@pytest.fixture
def condition_class():
    return Condition('ConditionDischargeDiagnosis-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/conditiondischargediagnosis-imri'
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
        'code' : '11535-2',
        'display' : 'Hospital discharge Dx Narrative'
    }]

@pytest.fixture
def code_coding():
    return [{
        'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-10-cm-2021-tw',
        'code' : 'K64.4',
        'display' : '痔瘡性殘留皮膚垂下物'
    }]

@pytest.fixture
def code_text():
    return 'Prolapsed hemorrhoids, Gr. III s/p laser hemorrhoidoplasty + partial hemorrhoidectomy'

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
def recorded_date():
    return '2023-09-07T10:00:14+08:00'

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Condition',
        'id' : 'ConditionDischargeDiagnosis-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/conditiondischargediagnosis-imri']
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
                'code' : '11535-2',
                'display' : 'Hospital discharge Dx Narrative'
            }]
        }],
        'code' : {
            'coding' : [{
                'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-10-cm-2021-tw',
                'code' : 'K64.4',
                'display' : '痔瘡性殘留皮膚垂下物'
            }],
            'text' : 'Prolapsed hemorrhoids, Gr. III s/p laser hemorrhoidoplasty + partial hemorrhoidectomy'
        },
        'subject' : {
            'reference' : 'Patient/Patient-min'
        },
        'encounter' : {
            'reference' : 'Encounter/Encounter-min'
        },
        'recordedDate' : '2023-09-07T10:00:14+08:00'
    }
