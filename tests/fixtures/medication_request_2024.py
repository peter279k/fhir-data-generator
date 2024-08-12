import pytest
from fhir_data_generator import TWCoreMedicationRequest as MedicationRequest


@pytest.fixture
def medication_request_class():
    return MedicationRequest('med-req-ref-example')

@pytest.fixture
def profile_urls():
    return [
        'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/MedicationRequest-twcore',
    ]

@pytest.fixture
def identifier():
    return [{
        'system': 'http://www.moi.gov.tw',
        'value': '7077',
    }]

@pytest.fixture
def status():
    return 'active'

@pytest.fixture
def status_reason_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/medicationrequest-status-reason',
        'code': 'clarif'
    }]

@pytest.fixture
def intent():
    return 'order'

@pytest.fixture
def category_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/medicationrequest-category',
        'code': 'discharge'
    }]

@pytest.fixture
def medication_reference():
    return {
        'reference': 'Medication/med-example'
    }

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/pat-example'
    }

@pytest.fixture
def encounter():
    return {
        'reference': 'Encounter/enc-example'
    }

@pytest.fixture
def authored_on():
    return '2022-08-01T18:00:14+08:00'

@pytest.fixture
def requester():
    return {
        'reference': 'Practitioner/pra-dr-example'
    }

@pytest.fixture
def reason_reference():
    return [{
        'reference': 'Observation/obs-lab-example'
    }]

@pytest.fixture
def dosage_instruction_text():
    return '三餐飯後，口服'

@pytest.fixture
def dosage_instruction_timing_coding():
    return [{
        'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medication-frequency-nhi-tw',
        'code': 'PC'
    }]

@pytest.fixture
def dosage_instruction_timing_text():
    return '三餐飯後'

@pytest.fixture
def dosage_instruction_route_coding():
    return [{
        'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medication-path-tw',
        'code': 'PO'
    }]

@pytest.fixture
def dosage_instruction_dose_rate_type_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/dose-rate-type',
        'code': 'ordered'
    }]

@pytest.fixture
def dispense_request_validity_period_start():
    return '2022-08-01T18:00:14+08:00'

@pytest.fixture
def dispense_request_validity_period_end():
    return '2022-08-08T18:00:14+08:00'

@pytest.fixture
def expected_payload():

    return {
        'resourceType': 'MedicationRequest',
        'id': 'med-req-ref-example',
        'meta': {
            'profile': [
                'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/MedicationRequest-twcore'
            ]
        },
        'identifier': [{
            'system': 'http://www.moi.gov.tw', 'value': '7077'
        }],
        'status': 'active',
        'statusReason': {
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/medicationrequest-status-reason',
                'code': 'clarif'
            }]
        },
        'intent': 'order',
        'category': [{
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/medicationrequest-category',
                'code': 'discharge'
            }]
        }],
        'medicationReference': {
            'reference': 'Medication/med-example'
        },
        'subject': {
            'reference': 'Patient/pat-example'
        },
        'encounter': {
            'reference': 'Encounter/enc-example'
        },
        'authoredOn': '2022-08-01T18:00:14+08:00',
        'requester': {
            'reference': 'Practitioner/pra-dr-example'
        },
        'reasonReference': [{
            'reference': 'Observation/obs-lab-example'
        }],
        'dosageInstruction': [{
            'text': '三餐飯後，口服',
            'timing': {
                'code': {
                    'coding': [{
                        'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medication-frequency-nhi-tw',
                        'code': 'PC'
                    }],
                    'text': '三餐飯後'
                }},
                'route': {
                    'coding': [{
                        'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medication-path-tw',
                        'code': 'PO'
                    }]
                },
                'doseAndRate': [{
                    'type': {
                        'coding': [{
                            'system': 'http://terminology.hl7.org/CodeSystem/dose-rate-type',
                            'code': 'ordered'
                        }]
                    }
                }]
            }],
        'dispenseRequest': {
            'validityPeriod': {
                'start': '2022-08-01T18:00:14+08:00',
                'end': '2022-08-08T18:00:14+08:00'
            }
        }
    }
