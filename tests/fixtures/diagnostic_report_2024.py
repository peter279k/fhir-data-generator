import pytest
from fhir_data_generator import TWCoreDiagnosticReport as DiagnosticReport


@pytest.fixture
def diagnostic_report_class():
    return DiagnosticReport('dia-example')

@pytest.fixture
def profile_urls():
    return [
        'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/DiagnosticReport-twcore'
    ]

@pytest.fixture
def status():
    return 'registered'

@pytest.fixture
def category_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/v2-0074',
        'code': 'LAB',
        'display': 'Laboratory'
    }]

@pytest.fixture
def category_text():
    return 'Laboratory'

@pytest.fixture
def code_coding():
    return [{
        'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medical-service-payment-tw',
        'code': '09002C',
        'display': '血中尿素氮'
    }]

@pytest.fixture
def code_text():
    return '血中尿素氮'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/pat-example'
    }

@pytest.fixture
def effective_datetime():
    return '2022-08-01T17:00:14+08:00'

@pytest.fixture
def issued():
    return '2022-08-01T18:00:14+08:00'

@pytest.fixture
def performer():
    return [{
        'reference': 'Practitioner/pra-dr-example'
    }]

@pytest.fixture
def result():
    return [{
        'reference': 'Observation/obs-lab-example'
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'DiagnosticReport',
        'id': 'dia-example',
        'meta': {
            'profile': [
                'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/DiagnosticReport-twcore'
            ]
        },
        'status': 'registered',
        'category': [{
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/v2-0074',
                'code': 'LAB',
                'display': 'Laboratory'
            }],
            'text': 'Laboratory'
        }],
        'code': {
            'coding': [{
                'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medical-service-payment-tw',
                'code': '09002C',
                'display': '血中尿素氮'
            }],
            'text': '血中尿素氮'
        },
        'subject': {
            'reference': 'Patient/pat-example'
        },
        'effectiveDateTime': '2022-08-01T17:00:14+08:00',
        'issued': '2022-08-01T18:00:14+08:00',
        'performer': [{
            'reference': 'Practitioner/pra-dr-example'
        }],
        'result': [{
            'reference': 'Observation/obs-lab-example'
        }]
    }
