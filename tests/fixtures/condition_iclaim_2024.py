import pytest
from fhir_data_generator import TWCoreCondition as Condition


@pytest.fixture
def condition_class():
    return Condition('Condition-C1')

@pytest.fixture
def profile_urls():
    return [
        'https://claim.cgh.org.tw/iclaim/StructureDefinition/condition-iclaim'
    ]

@pytest.fixture
def identifier():
    return [{
        'value': '1080108642',
    }]

@pytest.fixture
def clinical_status_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/condition-clinical',
        'code': 'remission'
    }]

@pytest.fixture
def category_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/condition-category',
        'code': 'encounter-diagnosis'
    }]

@pytest.fixture
def code_coding():
    return [{
        'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-9-cm-2001-tw',
        'code': '842.19',
        'display': '手其他部位扭傷及拉傷',
    }]

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/Patient-C1'
    }

@pytest.fixture
def encounter():
    return {
        'reference': 'Encounter/Encounter-C1',
    }

@pytest.fixture
def recorded_date():
    return '2023-08-07'

@pytest.fixture
def recorder():
    return {
        'reference': 'PractitionerRole/PractitionerRole-pri',
    }

@pytest.fixture
def asserter():
    return {
        'reference': 'PractitionerRole/PractitionerRole-res'
    }

@pytest.fixture
def stage():
    return [{
        'assessment' : [{
            'reference' : 'DiagnosticReport/DiagnosticReport-C1'
        }]
    }]

@pytest.fixture
def note():
    return [{
        'text': '手扭傷後,關節局部腫脹,關節彎曲受限,伸不直或彎曲不了',
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Condition',
        'id' : 'Condition-C1',
        'meta' : {
            'profile' : ['https://claim.cgh.org.tw/iclaim/StructureDefinition/condition-iclaim']
        },
        'identifier' : [{
            'value' : '1080108642'
        }],
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
                'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-9-cm-2001-tw',
                'code' : '842.19',
                'display' : '手其他部位扭傷及拉傷'
            }]
        },
        'subject' : {
            'reference' : 'Patient/Patient-C1'
        },
        'encounter' : {
            'reference' : 'Encounter/Encounter-C1'
        },
        'recordedDate' : '2023-08-07',
        'recorder' : {
            'reference' : 'PractitionerRole/PractitionerRole-pri'
        },
        'asserter' : {
            'reference' : 'PractitionerRole/PractitionerRole-res'
        },
        'stage' : [{
            'assessment' : [{
                'reference' : 'DiagnosticReport/DiagnosticReport-C1'
            }]
        }],
        'note' : [{
            'text' : '手扭傷後,關節局部腫脹,關節彎曲受限,伸不直或彎曲不了'
        }]
    }
