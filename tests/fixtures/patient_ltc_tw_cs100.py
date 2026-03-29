import pytest
from fhir_data_generator import PatientLtc


@pytest.fixture
def patient_class():
    return PatientLtc('ltc-patient-cs100-example')

@pytest.fixture
def identifiers():
    return [{
        'system': 'https://example.org/mrn',
        'value': 'A0001'
    }]

@pytest.fixture
def names():
    return [{
        'text': '王小明'
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Patient',
        'id': 'ltc-patient-cs100-example',
        'identifier': [{
            'system': 'https://example.org/mrn',
            'value': 'A0001'
        }],
        'name': [{
            'text': '王小明'
        }]
    }
