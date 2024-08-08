import pytest
from fhir_data_generator import Condition


@pytest.fixture
def condition_class():
    return Condition('con-example')

@pytest.fixture
def profile_urls():
    return [
        'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Condition-twcore'
    ]

@pytest.fixture
def clinical_status_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/condition-clinical',
        'code': 'remission'
    }]

@pytest.fixture
def verification_status_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/condition-ver-status',
        'code': 'confirmed'
    }]

@pytest.fixture
def category_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/condition-category',
        'code': 'encounter-diagnosis'
    }]

@pytest.fixture
def severity_coding():
    return [{
        'system': 'http://loinc.org',
        'code': 'LA6752-5'
    }]

@pytest.fixture
def code_coding():
    return [{
        'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-10-cm-2021-tw',
        'code': 'E08.649'
    }]

@pytest.fixture
def code_text():
    return '起因於潛在病的糖尿病，伴有低血糖，未伴有昏迷'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/pat-example'
    }

@pytest.fixture
def onset_datetime():
    return '2022-08-01T17:00:14+08:00'

@pytest.fixture
def abatement_datetime():
    return '2022-08-01T18:00:14+08:00'

@pytest.fixture
def asserter():
    return {
        'reference': 'Practitioner/pra-dr-example'
    }

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Condition',
        'id': 'con-example',
        'meta': {
            'profile': [
                'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Condition-twcore'
            ]
        },
        'clinicalStatus': {
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/condition-clinical',
                'code': 'remission'
            }]
        },
        'verificationStatus': {
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/condition-ver-status',
                'code': 'confirmed'
            }]
        },
        'category': [{
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/condition-category',
                'code': 'encounter-diagnosis'
            }]
        }],
        'severity': {
            'coding': [{
                'system': 'http://loinc.org',
                'code': 'LA6752-5'
            }]
        },
        'code': {
            'coding': [{
                'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-10-cm-2021-tw',
                'code': 'E08.649'
            }],
            'text': '起因於潛在病的糖尿病，伴有低血糖，未伴有昏迷'
        },
        'subject': {
            'reference': 'Patient/pat-example'
        },
        'onsetDateTime': '2022-08-01T17:00:14+08:00',
        'abatementDateTime': '2022-08-01T18:00:14+08:00',
        'asserter': {
            'reference': 'Practitioner/pra-dr-example'
        }
    }
