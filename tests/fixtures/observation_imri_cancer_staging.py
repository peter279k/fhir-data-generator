import pytest
from fhir_data_generator import ObservationIclaimC1 as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='ObservationCancerStaging-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/observation-cancerstaging-imri'
    ]

@pytest.fixture
def status():
    return 'final'

@pytest.fixture
def category_coding():
    return [{
        'system' : 'http://loinc.org',
        'code' : '22037-6',
        'display' : 'Staging Cancer Narrative'
    }]

@pytest.fixture
def code_coding():
    return [{
        'system' : 'http://snomed.info/sct',
        'code' : '399537006',
        'display' : 'Clinical TNM stage grouping'
    }]

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/Patient-min',
    }

@pytest.fixture
def effective_datetime():
    return '2024-04-01'

@pytest.fixture
def performer():
    return [{
        'reference' : 'Practitioner/Practitioner-min'
    }]

@pytest.fixture
def value_codeable_concept():
    return {
        'coding' : [{
            'system' : 'http://snomed.info/sct',
            'code' : '1222806003',
            'display' : 'American Joint Committee on Cancer stage IIIC (qualifier value)'
        }]
    }

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Observation',
        'id' : 'ObservationCancerStaging-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/observation-cancerstaging-imri']
        },
        'status' : 'final',
        'category' : [{
            'coding' : [{
                'system' : 'http://loinc.org',
                'code' : '22037-6',
                'display' : 'Staging Cancer Narrative'
            }]
        }],
        'code' : {
            'coding' : [{
                'system' : 'http://snomed.info/sct',
                'code' : '399537006',
                'display' : 'Clinical TNM stage grouping'
            }]
        },
        'subject' : {
            'reference' : 'Patient/Patient-min'
        },
        'effectiveDateTime' : '2024-04-01',
        'performer' : [{
            'reference' : 'Practitioner/Practitioner-min'
        }],
        'valueCodeableConcept' : {
            'coding' : [{
                'system' : 'http://snomed.info/sct',
                'code' : '1222806003',
                'display' : 'American Joint Committee on Cancer stage IIIC (qualifier value)'
            }]
        }
    }
