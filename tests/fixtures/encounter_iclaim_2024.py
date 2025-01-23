import pytest
from fhir_data_generator import TWCoreEncounter as Encounter


@pytest.fixture
def encounter_class():
    return Encounter('Encounter-C1')

@pytest.fixture
def profile_urls():
    return [
        'https://claim.cgh.org.tw/iclaim/StructureDefinition/encounter-iclaim'
    ]

@pytest.fixture
def extension():
    return [{
        'url' : 'https://claim.cgh.org.tw/iclaim/StructureDefinition/cathay-medicalidentity',
        'valueCodeableConcept' : {
            'coding' : [{
                'system' : 'http://terminology.hl7.org/CodeSystem/coverage-selfpay',
                'code' : 'pay'
            }]
        }
    }]

@pytest.fixture
def identifier():
    return [{
        'system' : 'https://www.cgh.org.tw',
        'value' : '1286481'
    }]

@pytest.fixture
def status():
    return 'finished'

@pytest.fixture
def fixture_class():
    return {
        'system' : 'http://terminology.hl7.org/CodeSystem/v3-ActCode',
        'code' : 'AMB'
    }

@pytest.fixture
def service_type_coding():
    return [{
        'system' : 'https://claim.cgh.org.tw/iclaim/CodeSystem/nhi-department-values',
        'code' : '06',
        'display' : '骨科'
    }]

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/Patient-C1'
    }

@pytest.fixture
def participant_individual():
    return {
        'reference' : 'PractitionerRole/PractitionerRole-rec'
    }

@pytest.fixture
def period():
    return {
        'start' : '2023-08-07T17:00:14-05:00',
        'end' : '2023-08-07T18:00:14-05:00'
    }

@pytest.fixture
def length():
    return {
        'value' : 1,
        'unit' : 'days',
        'system' : 'http://unitsofmeasure.org',
        'code' : 'd'
    }

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Encounter',
        'id' : 'Encounter-C1',
        'meta' : {
            'profile' : ['https://claim.cgh.org.tw/iclaim/StructureDefinition/encounter-iclaim']
        },
        'extension' : [{
            'url' : 'https://claim.cgh.org.tw/iclaim/StructureDefinition/cathay-medicalidentity',
            'valueCodeableConcept' : {
                'coding' : [{
                    'system' : 'http://terminology.hl7.org/CodeSystem/coverage-selfpay',
                    'code' : 'pay'
                }]
            }
        }],
        'identifier' : [{
            'system' : 'https://www.cgh.org.tw',
            'value' : '1286481'
        }],
        'status' : 'finished',
        'class' : {
            'system' : 'http://terminology.hl7.org/CodeSystem/v3-ActCode',
            'code' : 'AMB'
        },
        'serviceType' : {
            'coding' : [{
                'system' : 'https://claim.cgh.org.tw/iclaim/CodeSystem/nhi-department-values',
                'code' : '06',
                'display' : '骨科'
            }]
        },
        'subject' : {
            'reference' : 'Patient/Patient-C1'
        },
        'participant' : [{
            'individual' : {
                'reference' : 'PractitionerRole/PractitionerRole-rec'
            }
        }],
        'period' : {
            'start' : '2023-08-07T17:00:14-05:00',
            'end' : '2023-08-07T18:00:14-05:00'
        },
        'length' : {
            'value' : 1,
            'unit' : 'days',
            'system' : 'http://unitsofmeasure.org',
            'code' : 'd'
        }
    }
