import pytest
from fhir_data_generator import TWCoreMedicationStatement as MedicationStatement


@pytest.fixture
def medication_statement_class():
    return MedicationStatement('med-sta-example')

@pytest.fixture
def profile_urls():
    return [
        'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/MedicationStatement-twcore'
    ]

@pytest.fixture
def status():
    return 'active'

@pytest.fixture
def category_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/medication-statement-category',
        'code': 'outpatient',
        'display': 'outpatient'
    }]

@pytest.fixture
def category_text():
    return '門診'

@pytest.fixture
def medication_codeable_concept_coding():
    return [{
        'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medication-nhi-tw',
        'code': 'A003092100',
        'display': 'ASPIRIN TABLETS 500MG "S.Y."'
    }]

@pytest.fixture
def medication_codeable_concept_text():
    return '阿司匹林'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/pat-example'
    }

@pytest.fixture
def effective_date_time():
    return '2023-11-05T08:00:00+08:00'

@pytest.fixture
def date_asserted():
    return '2023-11-05T10:00:00+08:00'

@pytest.fixture
def reason_code_coding():
    return [{
        'system': 'http://snomed.info/sct',
        'code': '303002',
        'display':'Apoplectic pancreatitis'
    }]

@pytest.fixture
def reason_code_text():
    return '胰臟炎'

@pytest.fixture
def note():
    return [{
        'text': '每日早晚各一次'
    }]

@pytest.fixture
def dosage_text():
    return '每次一片'

@pytest.fixture
def dosage_timing_repeat():
    return {
        'frequency': 2, 'period': 1, 'periodUnit': 'd'
    }

@pytest.fixture
def dosage_route_coding():
    return [{
        'system': 'http://snomed.info/sct',
        'code': '26643006',
        'display': 'Oral route'
    }]

@pytest.fixture
def dosage_route_text():
    return '口服'

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'MedicationStatement',
        'id': 'med-sta-example',
        'meta': {
            'profile': [
                'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/MedicationStatement-twcore'
            ]
        },
        'status': 'active',
        'category': {
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/medication-statement-category',
                'code': 'outpatient',
                'display': 'outpatient'
            }],
            'text': '門診'
        },
        'medicationCodeableConcept': {
            'coding': [{
                'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medication-nhi-tw',
                'code': 'A003092100',
                'display': 'ASPIRIN TABLETS 500MG "S.Y."'
            }],
            'text': '阿司匹林'
        },
        'subject': {
            'reference': 'Patient/pat-example'
        },
        'effectiveDateTime': '2023-11-05T08:00:00+08:00',
        'dateAsserted': '2023-11-05T10:00:00+08:00',
        'reasonCode': [{
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '303002',
                'display':'Apoplectic pancreatitis'
            }],
            'text': '胰臟炎'
        }],
        'note': [{
            'text': '每日早晚各一次'
        }],
        'dosage': [{
            'text': '每次一片',
            'timing': {
                'repeat': {
                    'frequency': 2, 'period': 1, 'periodUnit': 'd'
                }
            },
            'route': {
                'coding': [{
                    'system': 'http://snomed.info/sct',
                    'code': '26643006',
                    'display': 'Oral route'
                }],
                'text': '口服'
            }
        }]
    }
