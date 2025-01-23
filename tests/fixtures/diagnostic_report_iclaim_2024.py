import pytest
from fhir_data_generator import TWCoreDiagnosticReport as DiagnosticReport


@pytest.fixture
def diagnostic_report_class():
    return DiagnosticReport('DiagnosticReport-C1')

@pytest.fixture
def profile_urls():
    return [
        'https://claim.cgh.org.tw/iclaim/StructureDefinition/diagnosticreport-iclaim'
    ]

@pytest.fixture
def status():
    return 'final'

@pytest.fixture
def code_coding():
    return [{
        'system' : 'http://loinc.org',
        'code' : '100537-0'
    }]

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/Patient-C1'
    }

@pytest.fixture
def result():
    return [{
        'reference': 'Observation/Observation-C1'
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'DiagnosticReport',
        'id' : 'DiagnosticReport-C1',
        'meta' : {
            'profile' : ['https://claim.cgh.org.tw/iclaim/StructureDefinition/diagnosticreport-iclaim']
        },
        'status' : 'final',
        'code' : {
            'coding' : [{
                'system' : 'http://loinc.org',
                'code' : '100537-0'
            }]
        },
        'subject' : {
            'reference' : 'Patient/Patient-C1'
        },
        'result' : [{
            'reference' : 'Observation/Observation-C1'
        }]
    }
