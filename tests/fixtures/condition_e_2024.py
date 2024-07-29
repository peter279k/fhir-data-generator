import pytest
from fhir_data_generator import ConditionE


@pytest.fixture
def condition_e_class():
    return ConditionE('condition-e-example')

@pytest.fixture
def profile_urls():
    return [
        'https://hapi.fhir.tw/fhir/StructureDefinition/Condition-excercise-history',
    ]

@pytest.fixture
def clinical_status_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/condition-clinical',
        'code': 'active',
    }]

@pytest.fixture
def category_coding():
    return [{
        'system': 'https://hapi.fhir.tw/fhir/CodeSystem/tempcode',
        'code': 'PhysicalActivity',
        'display': 'Physical Activity',
    }]

@pytest.fixture
def code_coding():
    return [{
        'system': 'http://snomed.info/sct',
        'code': '229072005',
        'display': 'Aerobic exercises',
    }]

@pytest.fixture
def code_text():
    return '一週2次有氧運動 每次30分鐘'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/patient-tw-example',
    }

@pytest.fixture
def asserter():
    return {
        'reference': 'Practitioner/practitioner-d-example',
    }

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Condition',
        'id': 'condition-e-example',
        'meta': {
            'profile': ['https://hapi.fhir.tw/fhir/StructureDefinition/Condition-excercise-history'],
        },
        'clinicalStatus': {
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/condition-clinical',
                'code': 'active'
            }],
        },
        'category': [{
            'coding': [{
                'system': 'https://hapi.fhir.tw/fhir/CodeSystem/tempcode',
                'code': 'PhysicalActivity',
                'display': 'Physical Activity'
            }]
        }],
        'code': {
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '229072005',
                'display': 'Aerobic exercises'
            }],
            'text': '一週2次有氧運動 每次30分鐘'
        },
        'subject': {
            'reference': 'Patient/patient-tw-example',
        },
        'asserter': {
            'reference': 'Practitioner/practitioner-d-example',
        },
    }
