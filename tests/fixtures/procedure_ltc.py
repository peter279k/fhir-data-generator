import pytest
from fhir_data_generator import ProcedureLtc as Procedure


@pytest.fixture
def procedure_class():
    return Procedure(procedure_id='ltc-procedure-bathing-example')

@pytest.fixture
def profile_urls():
    return [
        'http://ltc-ig.fhir.tw/StructureDefinition/LTCProcedureCareActivity'
    ]

@pytest.fixture
def status():
    return 'completed'

@pytest.fixture
def code_codings():
    return [
        [{
            'system': 'http://snomed.info/sct',
            'code': '226010006',
            'display': 'Assisting with eating and drinking'
        }],
        [{
            'system': 'http://snomed.info/sct',
            'code': '60369001',
            'display': 'Bathing patient'
        }],
        [{
            'system': 'http://snomed.info/sct',
            'code': '225964003',
            'display': 'Assisting with personal hygiene'
        }],
        [{
            'system': 'http://snomed.info/sct',
            'code': '313332003',
            'display': 'Dressing patient'
        }],
        [{
            'system': 'http://snomed.info/sct',
            'code': '313420001',
            'display': 'Assisting with toileting'
        }],
        [{
            'system': 'http://snomed.info/sct',
            'code': '223454002',
            'display': 'Escorting subject to toilet'
        }],
        [{
            'system': 'http://snomed.info/sct',
            'code': '710803000',
            'display': 'Assistance with mobility'
        }],
        [{
            'system': 'http://snomed.info/sct',
            'code': '713138001',
            'display': 'Assistance with mobility in bed'
        }],
        [{
            'system': 'http://snomed.info/sct',
            'code': '733923007',
            'display': 'Change of diaper'
        }],
    ]

@pytest.fixture
def code_texts():
    return [
        '進食協助',
        '沐浴/擦澡',
        '個人衛生協助',
        '穿衣',
        '如廁協助',
        '陪同到廁所',
        '移位/移動協助',
        '床上移動協助',
        '更換尿布',
    ]

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/ltc-patient-chen-ming-hui'
    }

@pytest.fixture
def performed_date_time():
    return '2024-01-15T14:30:00+08:00'

@pytest.fixture
def performer():
    return [{
        'actor': {
            'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'
        }
    }]

@pytest.fixture
def note():
    return [{
        'time': '2024-01-15T14:30:00+08:00',
        'text': '住民配合度良好，無特殊狀況'
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Procedure',
        'id': 'ltc-procedure-bathing-example',
        'meta': {
            'profile': ['http://ltc-ig.fhir.tw/StructureDefinition/LTCProcedureCareActivity']
        },
        'status': 'completed',
        'code': {
            'coding': [],
            'text': ''
        },
        'subject': {
            'reference': 'Patient/ltc-patient-chen-ming-hui'
        },
        'performedDateTime': '2024-01-15T14:30:00+08:00',
        'performer': [{
            'actor': {
                'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'
            }
        }],
        'note': [{
            'time': '2024-01-15T14:30:00+08:00',
            'text': '住民配合度良好，無特殊狀況'
        }]
    }
