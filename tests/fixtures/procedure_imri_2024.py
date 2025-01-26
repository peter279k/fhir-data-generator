import pytest
from fhir_data_generator import TWCoreProcedure as Procedure


@pytest.fixture
def procedure_class():
    return Procedure(procedure_id='Procedure-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/procedure-imri'
    ]

@pytest.fixture
def status():
    return 'completed'

@pytest.fixture
def category():
    return {
        'coding' : [{
            'system' : 'http://loinc.org',
            'code' : '8724-7',
            'display' : 'Surgical operation note description Narrative'
        }]
    }

@pytest.fixture
def code_coding():
    return [{
        'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-10-pcs-2021-tw',
        'code' : '06BY0ZC',
        'display' : '開放性痔靜脈叢部分切除術'
    }]

@pytest.fixture
def code_text():
    return '開放性痔靜脈叢部分切除術'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/Patient-min'
    }

@pytest.fixture
def encounter():
    return {
        'reference' : 'Encounter/Encounter-min'
    }

@pytest.fixture
def performed_date_time():
    return '2023-09-08T11:25:11+08:00'

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Procedure',
        'id' : 'Procedure-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/procedure-imri']
        },
        'status' : 'completed',
        'category' : {
            'coding' : [{
                'system' : 'http://loinc.org',
                'code' : '8724-7',
                'display' : 'Surgical operation note description Narrative'
            }]
        },
        'code' : {
            'coding' : [{
                'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-10-pcs-2021-tw',
                'code' : '06BY0ZC',
                'display' : '開放性痔靜脈叢部分切除術'
            }],
            'text' : '開放性痔靜脈叢部分切除術'
        },
        'subject' : {
            'reference' : 'Patient/Patient-min'
        },
        'encounter' : {
            'reference' : 'Encounter/Encounter-min'
        },
        'performedDateTime' : '2023-09-08T11:25:11+08:00'
    }
