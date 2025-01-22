import pytest
from fhir_data_generator import TWCorePractitioner as Practitioner


@pytest.fixture
def practitioner_class():
    return Practitioner(practitioner_id='Practitioner-Chen')

@pytest.fixture
def profile_urls():
    return ['https://claim.cgh.org.tw/iclaim/StructureDefinition/practitioner-iclaim']

@pytest.fixture
def identifiers():
    return [
        {
            'use' : 'official',
            'type' : {
                'coding' : [
                    {
                        'system' : 'http://terminology.hl7.org/CodeSystem/v2-0203',
                        'code' : 'MD'
                    }
                ]
            },
            'system' : 'https://www.cgh.org.tw',
            'value' : '031932'
        }
    ]

@pytest.fixture
def name():
    return [{
        'use': 'official',
        'text': '陳健骨',
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Practitioner',
        'id' : 'Practitioner-Chen',
        'meta' : {
            'profile' : ['https://claim.cgh.org.tw/iclaim/StructureDefinition/practitioner-iclaim']
        },
        'identifier' : [{
            'use' : 'official',
            'type' : {
                'coding' : [{
                    'system' : 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code' : 'MD'
                }]
            },
            'system' : 'https://www.cgh.org.tw',
            'value' : '031932'
        }],
        'name' : [{
            'use' : 'official',
            'text' : '陳健骨'
        }]
    }
