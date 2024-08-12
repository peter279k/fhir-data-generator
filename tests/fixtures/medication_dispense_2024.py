import pytest
from fhir_data_generator import TWCoreMedicationDispense as MedicationDispense


@pytest.fixture
def medication_dispense_class():
    return MedicationDispense('med-dis-ref-example')

@pytest.fixture
def profile_urls():
    return [
        'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/MedicationDispense-twcore'
    ]

@pytest.fixture
def status():
    return 'completed'

@pytest.fixture
def category_coding():
    return [{
        'system': 'http://terminology.hl7.org/fhir/CodeSystem/medicationdispense-category',
        'code': 'inpatient'
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
def context():
    return {
        'reference': 'Encounter/enc-example'
    }

@pytest.fixture
def performer_actor():
    return {
        'reference': 'Practitioner/pra-phc-example'
    }

@pytest.fixture
def type_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/v3-ActCode',
        'code': 'DF',
        'display': 'Daily Fill'
    }]

@pytest.fixture
def quantity():
    return {
        'value': 30,
        'unit': 'TAB',
        'system': 'http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm',
        'code': 'TAB'
    }

@pytest.fixture
def days_supply():
    return {
        'value': 30,
        'unit': 'days'
    }

@pytest.fixture
def when_prepared():
    return '2022-08-01T07:00:14+08:00'

@pytest.fixture
def when_handed_over():
    return '2022-08-01T08:15:14+08:00'

@pytest.fixture
def dosage_instruction():
    return [{
        'text': '每天早上口服一次',
        'timing': {
            'repeat': {
                'frequency': 1,
                'period': 1,
                'periodUnit': 'd'
            }
        }
    }]

@pytest.fixture
def substitution_was_substituted():
    return False

@pytest.fixture
def substitution_type_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/v3-substanceAdminSubstitution',
        'code': 'N',
        'display': 'none'
    }]

@pytest.fixture
def substitution_reason_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/v3-ActReason',
        'code': 'FP',
        'display': 'formulary policy'
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'MedicationDispense',
        'id': 'med-dis-ref-example',
        'meta': {
            'profile': [
                'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/MedicationDispense-twcore'
            ]
        },
        'status': 'completed',
        'category': {
            'coding': [{
                'system': 'http://terminology.hl7.org/fhir/CodeSystem/medicationdispense-category',
                'code': 'inpatient'
            }]
        },
        'medicationReference': {
            'reference': 'Medication/med-example'
        },
        'subject': {
            'reference': 'Patient/pat-example'
        },
        'context': {
            'reference': 'Encounter/enc-example'
        },
        'performer': [{
            'actor': {
                'reference': 'Practitioner/pra-phc-example'
            }
        }],
        'type': {
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/v3-ActCode',
                'code': 'DF',
                'display': 'Daily Fill'
            }]
        },
        'quantity': {
            'value': 30,
            'unit': 'TAB',
            'system': 'http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm',
            'code': 'TAB'
        },
        'daysSupply': {
            'value': 30,
            'unit': 'days'
        },
        'whenPrepared': '2022-08-01T07:00:14+08:00',
        'whenHandedOver': '2022-08-01T08:15:14+08:00',
        'dosageInstruction': [{
            'text': '每天早上口服一次',
            'timing': {
                'repeat': {
                    'frequency': 1,
                    'period': 1,
                    'periodUnit': 'd'
                }
            }
        }],
        'substitution': {
            'wasSubstituted': False,
            'type': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v3-substanceAdminSubstitution',
                    'code': 'N',
                    'display': 'none'
                }]
            },
            'reason': [{
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v3-ActReason',
                    'code': 'FP',
                    'display': 'formulary policy'
                }]
            }]
        }
    }
