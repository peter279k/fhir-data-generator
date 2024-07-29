import pytest
from fhir_data_generator import PatientEX


@pytest.fixture
def patient_class():
    return PatientEX('patient-ex-example')

@pytest.fixture
def profile_urls():
    return [
        'https://hapi.fhir.tw/fhir/StructureDefinition/Patient-sport',
    ]

@pytest.fixture
def extension_url():
    return 'https://hapi.fhir.tw/fhir/StructureDefinition/person-age'

@pytest.fixture
def extension_value_age():
    return {
        'value': 32,
        'unit': '32',
        'system': 'http://unitsofmeasure.org',
        'code': 'a',
    }

@pytest.fixture
def identifiers():
    return [{
        'system': 'https://www.morefit.com.tw',
        'value': '0938110330',
    }]

@pytest.fixture
def name_text():
    return '連小妹'

@pytest.fixture
def gender():
    return 'female'

@pytest.fixture
def birth_date():
    return '1990-01-01'

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Patient',
        'id': 'patient-ex-example',
        'meta': {
            'profile': ['https://hapi.fhir.tw/fhir/StructureDefinition/Patient-sport']
        },
        'extension': [{
            'url': 'https://hapi.fhir.tw/fhir/StructureDefinition/person-age',
            'valueAge': {
                'value': 32,
                'unit': '32',
                'system': 'http://unitsofmeasure.org',
                'code': 'a'
            }
        }],
        'identifier': [{
            'system': 'https://www.morefit.com.tw', 'value': '0938110330'
        }],
        'name': [{
            'text': '連小妹'
        }],
        'gender': 'female',
        'birthDate': '1990-01-01'
    }
