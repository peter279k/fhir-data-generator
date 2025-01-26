import pytest
from fhir_data_generator import ImagingStudyImri as ImagingStudy


@pytest.fixture
def imaging_study_class():
    return ImagingStudy('ImagingStudy-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/imagingstudy-imri',
    ]

@pytest.fixture
def status():
    return 'available'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/Patient-min'
    }

@pytest.fixture
def encounter():
    return {
        'reference': 'Encounter/Encounter-min'
    }

@pytest.fixture
def started():
    return '2023-09-07T11:01:20+03:00'

@pytest.fixture
def interpreter():
    return [{
        'reference' : 'Practitioner/Practitioner-min'
    }]

@pytest.fixture
def description():
    return 'No significant roentgenological abnormality is observed.'

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'ImagingStudy',
        'id' : 'ImagingStudy-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/imagingstudy-imri']
        },
        'status' : 'available',
        'subject' : {
            'reference' : 'Patient/Patient-min'
        },
        'encounter' : {
            'reference' : 'Encounter/Encounter-min'
        },
        'started' : '2023-09-07T11:01:20+03:00',
        'interpreter' : [{
            'reference' : 'Practitioner/Practitioner-min'
        }],
        'description' : 'No significant roentgenological abnormality is observed.'
    }
