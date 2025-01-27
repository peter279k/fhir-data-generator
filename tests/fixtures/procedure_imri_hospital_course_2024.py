import pytest
from fhir_data_generator import TWCoreProcedure as Procedure


@pytest.fixture
def procedure_class():
    return Procedure(procedure_id='ProcedureHospitalCourse-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/procedurehospitalcourse-imri'
    ]

@pytest.fixture
def status():
    return 'completed'

@pytest.fixture
def code_coding():
    return [{
        'system' : 'http://loinc.org',
        'code' : '8648-8'
    }]

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
def note():
    return [{
        'text' : 'After admission, prepare operation work-up was done. The surgical method of laparoscopic cholecystectomy was done on 10/20/2023. Post operative wound pain could tolerance under analgesic drug. During the hospitalization, vital signs were stable, post operative wound appeared: no oozing, no redness or other infection signs were noted, no tenderness. To education of wound care, discharge today and outpatient department follow up was arrange.'
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Procedure',
        'id' : 'ProcedureHospitalCourse-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/procedurehospitalcourse-imri']
        },
        'status' : 'completed',
        'code' : {
            'coding' : [{
                'system' : 'http://loinc.org',
                'code' : '8648-8'
            }]
        },
        'subject' : {
            'reference' : 'Patient/Patient-min'
        },
        'encounter' : {
            'reference' : 'Encounter/Encounter-min'
        },
        'note' : [{
            'text' : 'After admission, prepare operation work-up was done. The surgical method of laparoscopic cholecystectomy was done on 10/20/2023. Post operative wound pain could tolerance under analgesic drug. During the hospitalization, vital signs were stable, post operative wound appeared: no oozing, no redness or other infection signs were noted, no tenderness. To education of wound care, discharge today and outpatient department follow up was arrange.'
        }]
    }
