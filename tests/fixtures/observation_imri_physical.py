import pytest
from fhir_data_generator import ObservationIclaimC1 as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='ObservationPhysicalExamination-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/observation-physical-examination-imri'
    ]

@pytest.fixture
def status():
    return 'final'

@pytest.fixture
def category_coding():
    return [{
        'system' : 'http://terminology.hl7.org/CodeSystem/observation-category',
        'code' : 'exam'
    }]

@pytest.fixture
def code_coding():
    return [{
        'system' : 'http://snomed.info/sct',
        'code' : '39868003',
        'display' : 'Inspection of mouth'
    }]

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/Patient-min',
    }

@pytest.fixture
def effective_datetime():
    return '2023-09-07'

@pytest.fixture
def value_string():
    return 'oral lesion: No'

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Observation',
        'id' : 'ObservationPhysicalExamination-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/observation-physical-examination-imri']
        },
        'status' : 'final',
        'category' : [{
            'coding' : [{
                'system' : 'http://terminology.hl7.org/CodeSystem/observation-category',
                'code' : 'exam'
            }]
        }],
        'code' : {
            'coding' : [{
                'system' : 'http://snomed.info/sct',
                'code' : '39868003',
                'display' : 'Inspection of mouth'
            }]
        },
        'subject' : {
            'reference' : 'Patient/Patient-min'
        },
        'effectiveDateTime' : '2023-09-07',
        'valueString' : 'oral lesion: No'
    }
