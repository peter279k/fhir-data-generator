import pytest
from fhir_data_generator import ConditionE


@pytest.fixture
def condition_m_class():
    return ConditionE('condition-m-example')

@pytest.fixture
def profile_urls():
    return [
        'https://hapi.fhir.tw/fhir/StructureDefinition/Condition-medical-history',
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
        'system': 'http://loinc.org',
        'code': '10164-2',
        'display': 'History of Present illness Narrative'
    }]

@pytest.fixture
def code_coding():
    return [{
        'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-10-cm-2021-tw',
        'code': 'E08.649'
    }]

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
        'id': 'condition-m-example',
        'meta': {
            'profile': ['https://hapi.fhir.tw/fhir/StructureDefinition/Condition-medical-history']
        },
        'clinicalStatus': {
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/condition-clinical',
                'code': 'active'
            }]
        },
        'category': [{
            'coding': [{
                'system': 'http://loinc.org',
                'code': '10164-2',
                'display': 'History of Present illness Narrative'
            }]
        }],
        'code': {
            'coding': [{
                'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-10-cm-2021-tw',
                'code': 'E08.649'
            }]
        },
        'subject': {
            'reference': 'Patient/patient-tw-example'
        },
        'asserter': {
            'reference': 'Practitioner/practitioner-d-example'
        },
    }
