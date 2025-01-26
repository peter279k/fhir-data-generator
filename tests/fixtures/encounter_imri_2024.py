import pytest
from fhir_data_generator import EncounterImri as Encounter


@pytest.fixture
def encounter_class():
    return Encounter('Encounter-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/encounter-imri'
    ]

@pytest.fixture
def status():
    return 'finished'

@pytest.fixture
def fixture_class():
    return {
        'system' : 'http://terminology.hl7.org/CodeSystem/v3-ActCode',
        'code' : 'PRENC'
    }

@pytest.fixture
def service_type_coding():
    return [{
        'system' : 'http://snomed.info/sct',
        'code' : '408464004',
        'display' : 'Colorectal Surgery'
    }]

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/Patient-min'
    }

@pytest.fixture
def participant_individual():
    return {
        'reference' : 'Practitioner/Practitioner-min'
    }

@pytest.fixture
def period():
    return {
        'start' : '2023-09-06T17:00:14+08:00',
        'end' : '2023-09-12T18:00:14+08:00'
    }

@pytest.fixture
def hospitalization():
    return {
        'destination' : {
            'reference' : 'Location/Location-min'
        },
        'dischargeDisposition' : {
            'text' : '改門診治療'
        }
    }

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Encounter',
        'id' : 'Encounter-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/encounter-imri']
        },
        'status' : 'finished',
        'class' : {
            'system' : 'http://terminology.hl7.org/CodeSystem/v3-ActCode',
            'code' : 'PRENC'
        },
        'serviceType' : {
            'coding' : [{
                'system' : 'http://snomed.info/sct',
                'code' : '408464004',
                'display' : 'Colorectal Surgery'
            }]
        },
        'subject' : {
            'reference' : 'Patient/Patient-min'
        },
        'participant' : [{
            'individual' : {
                'reference' : 'Practitioner/Practitioner-min'
            }
        }],
        'period' : {
            'start' : '2023-09-06T17:00:14+08:00',
            'end' : '2023-09-12T18:00:14+08:00'
        },
        'hospitalization' : {
            'destination' : {
                'reference' : 'Location/Location-min'
            },
            'dischargeDisposition' : {
                'text' : '改門診治療'
            }
        }
    }
