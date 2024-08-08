import pytest
from fhir_data_generator import TWCoreEncounter as Encounter


@pytest.fixture
def encounter_class():
    return Encounter('enc-example')

@pytest.fixture
def profile_urls():
    return [
        'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Encounter-twcore'
    ]

@pytest.fixture
def identifier():
    return [{
        'system': 'http://healthcare.example.org/identifiers/enocunter',
        'value': 'E22081702'
    }]

@pytest.fixture
def status():
    return 'finished'

@pytest.fixture
def fixture_class():
    return {
        'system': 'http://terminology.hl7.org/CodeSystem/v3-ActCode',
        'code': 'PRENC'
    }

@pytest.fixture
def type_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/encounter-type',
        'code': 'ADMS'
    }]

@pytest.fixture
def service_type_coding():
    return [{
        'system': 'http://snomed.info/sct',
        'code': '394589003',
        'display': 'Nephrology'
    }]

@pytest.fixture
def service_type_text():
    return '腎臟內科'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/pat-example'
    }

@pytest.fixture
def participant_type_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/v3-ParticipationType',
        'code': 'PPRF'
    }]

@pytest.fixture
def participant_period():
    return {
        'start': '2022-08-01T17:00:14+08:00',
        'end': '2022-08-01T18:00:14+08:00'
    }

@pytest.fixture
def participant_individual():
    return {
        'reference': 'Practitioner/pra-dr-example'
    }

@pytest.fixture
def period():
    return {
        'start': '2022-08-01T17:00:14+08:00',
        'end': '2022-08-01T18:00:14+08:00'
    }

@pytest.fixture
def reason_code_coding():
    return [{
        'system': 'http://snomed.info/sct',
        'code': '160303001',
        'display': 'FH: Diabetes mellitus'
    }]

@pytest.fixture
def hospitalization_discharge_disposition_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/discharge-disposition',
        'code': 'home'
    }]

@pytest.fixture
def location():
    return {
        'reference': 'Location/loc-ent-example'
    }

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Encounter',
        'id': 'enc-example',
        'meta': {
            'profile': [
                'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Encounter-twcore'
            ]
        },
        'identifier': [{
            'system': 'http://healthcare.example.org/identifiers/enocunter',
            'value': 'E22081702'
        }],
        'status': 'finished',
        'class': {
            'system': 'http://terminology.hl7.org/CodeSystem/v3-ActCode',
            'code': 'PRENC'
        },
        'type': [{
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/encounter-type',
                'code': 'ADMS'
            }]
        }],
        'serviceType': {
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '394589003',
                'display': 'Nephrology'
            }],
            'text': '腎臟內科'
        },
        'subject': {
            'reference': 'Patient/pat-example'
        },
        'participant': [{
            'type': [{
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v3-ParticipationType',
                    'code': 'PPRF'
                }]
            }],
            'period': {
                'start': '2022-08-01T17:00:14+08:00',
                'end': '2022-08-01T18:00:14+08:00'
            },
            'individual': {
                'reference': 'Practitioner/pra-dr-example'
            }
        }],
        'period': {
            'start': '2022-08-01T17:00:14+08:00',
            'end': '2022-08-01T18:00:14+08:00'
        },
        'reasonCode': [{
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '160303001',
                'display': 'FH: Diabetes mellitus'
            }]
        }],
        'hospitalization': {
            'dischargeDisposition': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/discharge-disposition',
                    'code': 'home'
                }]
            }
        },
        'location': [{
            'location': {
                'reference': 'Location/loc-ent-example'
            }
        }]
    }
