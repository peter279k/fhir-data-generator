import pytest
from fhir_data_generator import PhysicalActivityServiceRequest


@pytest.fixture
def service_request_class():
    return PhysicalActivityServiceRequest('servicerequest-example')

@pytest.fixture
def profile_urls():
    return [
        'https://hapi.fhir.tw/fhir/StructureDefinition/ServiceRequest-sport',
    ]

@pytest.fixture
def identifiers():
    return [{
        'system': 'https://www.health.ntpc.gov.tw/',
        'value': 's141526',
    }]

@pytest.fixture
def status():
    return 'completed'

@pytest.fixture
def intent():
    return 'order'

@pytest.fixture
def category_coding():
    return [{
        'system': 'https://hapi.fhir.tw/fhir/CodeSystem/tempcode',
        'code': 'PhysicalActivity',
        'display': 'Physical Activity'
    }]

@pytest.fixture
def code_coding():
    return [{
        'system': 'http://snomed.info/sct',
        'code': '229065009',
        'display': 'Exercise therapy',
    }]

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/patient-tw-example'
    }

@pytest.fixture
def authored_on():
    return '2024-07-01'

@pytest.fixture
def requester():
    return {
        'reference': 'Practitioner/practitioner-d-example'
    }

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'ServiceRequest',
        'id': 'servicerequest-example',
        'meta': {
            'profile': ['https://hapi.fhir.tw/fhir/StructureDefinition/ServiceRequest-sport']
        },
        'identifier': [{
            'system': 'https://www.health.ntpc.gov.tw/',
            'value': 's141526'
        }],
        'status': 'completed',
        'intent': 'order',
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
                'code': '229065009',
                'display': 'Exercise therapy'
            }]
        },
        'subject': {
            'reference': 'Patient/patient-tw-example'
        },
        'authoredOn': '2024-07-01',
        'requester': {
            'reference': 'Practitioner/practitioner-d-example'
        }
    }
