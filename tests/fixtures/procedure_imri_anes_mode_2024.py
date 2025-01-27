import pytest
from fhir_data_generator import TWCoreProcedure as Procedure


@pytest.fixture
def procedure_class():
    return Procedure(procedure_id='ProcedureAnesthesiaMode-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/procedure-anesthesiamode-imri'
    ]

@pytest.fixture
def part_of():
    return [{
        'reference' : 'Procedure/Procedure-pro'
    }]

@pytest.fixture
def status():
    return 'completed'

@pytest.fixture
def category():
    return {
        'coding' : [{
            'system' : 'http://snomed.info/sct',
            'code' : '399097000'
        }]
    }

@pytest.fixture
def code_coding():
    return [{
        'system' : 'http://snomed.info/sct',
        'code' : '274507007',
        'display' : 'Operative general anesthesia'
    }]

@pytest.fixture
def code_text():
    return '全身麻醉'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/Patient-min'
    }

@pytest.fixture
def performed_date_time():
    return '2023-09-08T11:25:11+08:00'

@pytest.fixture
def performer():
    return [{
        'actor' : {
            'reference' : 'PractitionerRole/PractitionerRole-anesthesia',
            'display' : '黃依昇'
        }
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Procedure',
        'id' : 'ProcedureAnesthesiaMode-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/procedure-anesthesiamode-imri']
        },
        'partOf' : [{
            'reference' : 'Procedure/Procedure-pro'
        }],
        'status' : 'completed',
        'category' : {
            'coding' : [{
                'system' : 'http://snomed.info/sct',
                'code' : '399097000'
            }]
        },
        'code' : {
            'coding' : [{
                'system' : 'http://snomed.info/sct',
                'code' : '274507007',
                'display' : 'Operative general anesthesia'
            }],
            'text' : '全身麻醉'
        },
        'subject' : {
            'reference' : 'Patient/Patient-min'
        },
        'performedDateTime' : '2023-09-08T11:25:11+08:00',
        'performer' : [{
            'actor' : {
                'reference' : 'PractitionerRole/PractitionerRole-anesthesia',
                'display' : '黃依昇'
            }
        }]
    }
