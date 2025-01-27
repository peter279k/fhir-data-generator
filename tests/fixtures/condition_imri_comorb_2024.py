import pytest
from fhir_data_generator import ConditionImri as Condition


@pytest.fixture
def condition_class():
    return Condition('ConditionComorbiditiesandComplications-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/conditioncomorbiditiesandcomplications-imri'
    ]

@pytest.fixture
def clinical_status_coding():
    return [{
        'system' : 'http://terminology.hl7.org/CodeSystem/condition-clinical',
        'code' : 'resolved',
        'display' : 'Resolved'
    }]

@pytest.fixture
def clinical_status_text():
    return '解決'

@pytest.fixture
def category_coding():
    return [{
        'system' : 'http://loinc.org',
        'code' : '55109-3',
        'display' : 'Complications Document'
    }]

@pytest.fixture
def code_coding():
    return [{
        'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-10-cm-2021-tw',
        'code' : 'M96',
        'display' : '術中及術後併發症及肌肉骨骼系統疾患，他處未歸類者'
    }]

@pytest.fixture
def code_text():
    return '術中及術後併發症及肌肉骨骼系統疾患，他處未歸類者'

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
        'id' : 'ConditionComorbiditiesandComplications-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/conditioncomorbiditiesandcomplications-imri']
        },
        'clinicalStatus' : {
            'coding' : [{
                'system' : 'http://terminology.hl7.org/CodeSystem/condition-clinical',
                'code' : 'resolved',
                'display' : 'Resolved'
            }],
            'text' : '解決'
        },
        'category' : [{
            'coding' : [{
                'system' : 'http://loinc.org',
                'code' : '55109-3',
                'display' : 'Complications Document'
            }]
        }],
        'code' : {
            'coding' : [{
                'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-10-cm-2021-tw',
                'code' : 'M96',
                'display' : '術中及術後併發症及肌肉骨骼系統疾患，他處未歸類者'
            }],
            'text' : '術中及術後併發症及肌肉骨骼系統疾患，他處未歸類者'
        },
        'subject' : {
            'reference' : 'Patient/Patient-min'
        },
        'encounter' : {
            'reference' : 'Encounter/Encounter-min'
        },
        'recordedDate' : '2023-09-07T10:00:14+08:00'
    }
