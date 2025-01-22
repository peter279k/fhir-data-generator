import pytest
from fhir_data_generator import ObservationIclaimC1 as Observation


@pytest.fixture
def observation_class():
    return Observation(observation_id='Observation-C1')

@pytest.fixture
def profile_urls():
    return [
        'https://claim.cgh.org.tw/iclaim/StructureDefinition/observation-iclaim'
    ]

@pytest.fixture
def identifier():
    return [{
        'system' : 'https://www.cgh.org.tw',
        'value' : '096H004'
    }]

@pytest.fixture
def status():
    return 'final'

@pytest.fixture
def category_coding():
    return [{
        'system' : 'http://terminology.hl7.org/CodeSystem/observation-category',
        'code' : 'laboratory'
    }]

@pytest.fixture
def code_coding():
    return [{
        'system' : 'http://loinc.org',
        'code' : '100856-4',
        'display' : 'CD3+CD4+ (T4 helper) cells/100 cells in Blood mononuclear cells'
    }]

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/Patient-C1',
    }

@pytest.fixture
def effective_datetime():
    return '2023-08-07'

@pytest.fixture
def issued():
    return '2023-08-07T17:00:14+08:00'

@pytest.fixture
def performer():
    return [
        {
            'reference' : 'PractitionerRole/PractitionerRole-tech'
        },
        {
            'reference' : 'PractitionerRole/PractitionerRole-rep'
        },
    ]

@pytest.fixture
def value_quantity():
    return {
        'value' : 4000,
        'unit' : '/uL',
        'system' : 'http://unitsofmeasure.org'
    }

@pytest.fixture
def note():
    return [{
        'text' : '無'
    }]

@pytest.fixture
def interpretation():
    return [{
        'coding' : [{
            'system' : 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation',
            'code' : '<'
        }]
    }]

@pytest.fixture
def body_site_coding():
    return [{
        'system' : 'http://snomed.info/sct',
        'code' : '9736006'
    }]

@pytest.fixture
def reference_range():
    return [{
        'low' : {
            'value' : 4500
        },
        'high' : {
            'value' : 10000
        }
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Observation',
        'id' : 'Observation-C1',
        'meta' : {
            'profile' : ['https://claim.cgh.org.tw/iclaim/StructureDefinition/observation-iclaim']
        },
        'identifier' : [{
            'system' : 'https://www.cgh.org.tw',
            'value' : '096H004'
        }],
        'status' : 'final',
        'category' : [{
            'coding' : [{
                'system' : 'http://terminology.hl7.org/CodeSystem/observation-category',
                'code' : 'laboratory'
            }]
        }],
        'code' : {
            'coding' : [{
                'system' : 'http://loinc.org',
                'code' : '100856-4',
                'display' : 'CD3+CD4+ (T4 helper) cells/100 cells in Blood mononuclear cells'
            }]
        },
        'subject' : {
            'reference' : 'Patient/Patient-C1'
        },
        'effectiveDateTime' : '2023-08-07',
        'issued' : '2023-08-07T17:00:14+08:00',
        'performer' : [
            {
                'reference' : 'PractitionerRole/PractitionerRole-tech'
            },
            {
                'reference' : 'PractitionerRole/PractitionerRole-rep'
            }
        ],
        'valueQuantity' : {
            'value' : 4000,
            'unit' : '/uL',
            'system' : 'http://unitsofmeasure.org'
        },
        'interpretation' : [{
            'coding' : [{
                'system' : 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation',
                'code' : '<'
            }]
        }],
        'note' : [{
            'text' : '無'
        }],
        'bodySite' : {
            'coding' : [{
                'system' : 'http://snomed.info/sct',
                'code' : '9736006'
            }]
        },
        'referenceRange' : [{
            'low' : {
                'value' : 4500
            },
            'high' : {
                'value' : 10000
            }
        }]
    }
