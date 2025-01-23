import pytest
from fhir_data_generator import CoverageC1 as Coverage


@pytest.fixture
def coverage_class():
    return Coverage('Coverage-C1')

@pytest.fixture
def profile_urls():
    return [
        'https://claim.cgh.org.tw/iclaim/StructureDefinition/coverage-iclaim'
    ]

@pytest.fixture
def status():
    return 'active'

@pytest.fixture
def beneficiary():
    return {
        'reference' : 'Patient/Patient-C1'
    }

@pytest.fixture
def payor():
    return [{
        'reference' : 'Organization/Organization-cathay'
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Coverage',
        'id' : 'Coverage-C1',
        'meta' : {
            'profile' : ['https://claim.cgh.org.tw/iclaim/StructureDefinition/coverage-iclaim']
        },
        'status' : 'active',
        'beneficiary' : {
            'reference' : 'Patient/Patient-C1'
        },
        'payor' : [{
            'reference' : 'Organization/Organization-cathay'
        }]
    }
