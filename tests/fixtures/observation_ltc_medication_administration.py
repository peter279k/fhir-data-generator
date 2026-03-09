import pytest
from fhir_data_generator import MedicationAdministration


@pytest.fixture
def medication_administration_class():
    return MedicationAdministration('ltc-medication-administration-metformin-example')

@pytest.fixture
def profile_urls():
    return [
        'http://ltc-ig.fhir.tw/StructureDefinition/LTCMedicationAdministration'
    ]

@pytest.fixture
def status():
    return 'completed'

@pytest.fixture
def medication_codeable_concept_coding():
    return [{
        'system': 'http://snomed.info/sct',
        'code': '323402006',
        'display': 'Product containing benethamine penicillin (medicinal product)'
    }]

@pytest.fixture
def medication_codeable_concept_text():
    return 'Product containing benethamine penicillin (medicinal product)'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/ltc-patient-chen-ming-hui'
    }

@pytest.fixture
def effective_date_time():
    return '2024-01-15T08:00:00+08:00'

@pytest.fixture
def performer():
    return [{
        'actor': {
            'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'
        }
    }]

@pytest.fixture
def note():
    return [{
        'time': '2024-01-15T08:00:00+08:00',
        'text': '住民按時服藥，無不良反應'
    }]

@pytest.fixture
def dosage():
    return {
        'route': {
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '26643006',
                'display': 'Oral route'
            }],
            'text': '口服'
        },
        'dose': {
            'value': 500,
            'unit': 'mg',
            'system': 'http://unitsofmeasure.org',
            'code': 'mg'
        }
    }

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'MedicationAdministration',
        'id': 'ltc-medication-administration-metformin-example',
        'meta': {
            'profile': ['http://ltc-ig.fhir.tw/StructureDefinition/LTCMedicationAdministration']
        },
        'status': 'completed',
        'medicationCodeableConcept': {
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '323402006',
                'display': 'Product containing benethamine penicillin (medicinal product)'
            }],
            'text': 'Product containing benethamine penicillin (medicinal product)'
        },
        'subject': {
            'reference': 'Patient/ltc-patient-chen-ming-hui'
        },
        'effectiveDateTime': '2024-01-15T08:00:00+08:00',
        'performer': [{
            'actor': {
                'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'
            }
        }],
        'note': [{
            'time': '2024-01-15T08:00:00+08:00',
            'text': '住民按時服藥，無不良反應'
        }],
        'dosage': {
            'route': {
                'coding': [{
                    'system': 'http://snomed.info/sct',
                    'code': '26643006',
                    'display': 'Oral route'
                }],
                'text': '口服'
            },
            'dose': {
                'value': 500,
                'unit': 'mg',
                'system': 'http://unitsofmeasure.org',
                'code': 'mg'
            }
        }
    }

