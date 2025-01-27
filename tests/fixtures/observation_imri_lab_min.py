import pytest
from fhir_data_generator import ObservationIclaimC1 as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='ObservationLaboratory-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/observation-laboratory-imri'
    ]

@pytest.fixture
def status():
    return 'final'

@pytest.fixture
def category_coding():
    return [{
        'system' : 'http://loinc.org',
        'code' : '30954-2'
    }]

@pytest.fixture
def category_text():
    return '特殊檢查'

@pytest.fixture
def code_text():
    return '心電圖(EKG)'

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
    return 'Normal sinus rhythmwith sinus arrhythmia Voltage criteria for left ventricular hypertrophy Early repolarization'

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Observation',
        'id' : 'ObservationLaboratory-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/observation-laboratory-imri']
        },
        'status' : 'final',
        'category' : [{
            'coding' : [{
                'system' : 'http://loinc.org',
                'code' : '30954-2'
            }],
            'text' : '特殊檢查'
        }],
        'code' : {
            'text' : '心電圖(EKG)'
        },
        'subject' : {
            'reference' : 'Patient/Patient-min'
        },
        'effectiveDateTime' : '2023-09-07',
        'valueString' : 'Normal sinus rhythmwith sinus arrhythmia Voltage criteria for left ventricular hypertrophy Early repolarization'
    }
