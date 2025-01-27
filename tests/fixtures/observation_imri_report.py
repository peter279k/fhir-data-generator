import pytest
from fhir_data_generator import ObservationIclaimC1 as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='ObservationPathologyReport-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/observation-pathology-report-imri'
    ]

@pytest.fixture
def status():
    return 'final'

@pytest.fixture
def category_coding():
    return [{
        'system' : 'http://loinc.org',
        'code' : '22034-3',
        'display' : 'Pathology report Cancer Narrative'
    }]

@pytest.fixture
def code_text():
    return 'Anus, hemorrhoidectomy, hemorrhoid.'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/Patient-min',
    }

@pytest.fixture
def effective_datetime():
    return '2023-09-08'

@pytest.fixture
def performer():
    return [{
        'reference' : 'Practitioner/Practitioner-min'
    }]

@pytest.fixture
def value_string():
    return 'The specimen submitted consists of 2 pieces of anal tissue measuring 1.4 cm in greatest dimension.\r\n                Al1 for section. Microscopically, the section shows a picture of hemorrhoid, composed of dilated,\r\n                tortuous and congested veins in the stroma of the anal mucosa'

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Observation',
        'id' : 'ObservationPathologyReport-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/observation-pathology-report-imri']
        },
        'status' : 'final',
        'category' : [{
            'coding' : [{
                'system' : 'http://loinc.org',
                'code' : '22034-3',
                'display' : 'Pathology report Cancer Narrative'
            }]
        }],
        'code' : {
            'text' : 'Anus, hemorrhoidectomy, hemorrhoid.'
        },
        'subject' : {
            'reference' : 'Patient/Patient-min'
        },
        'effectiveDateTime' : '2023-09-08',
        'performer' : [{
            'reference' : 'Practitioner/Practitioner-min'
        }],
        'valueString' : 'The specimen submitted consists of 2 pieces of anal tissue measuring 1.4 cm in greatest dimension.\r\n                Al1 for section. Microscopically, the section shows a picture of hemorrhoid, composed of dilated,\r\n                tortuous and congested veins in the stroma of the anal mucosa'
    }
