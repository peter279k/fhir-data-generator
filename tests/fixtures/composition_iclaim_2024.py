import pytest
from fhir_data_generator import TWCoreComposition as Composition


@pytest.fixture
def composition_class():
    return Composition('Composition-C1')

@pytest.fixture
def profile_urls():
    return [
        'https://claim.cgh.org.tw/iclaim/StructureDefinition/composition-iclaim',
    ]

@pytest.fixture
def identifier():
    return {
        'system' : 'https://www.cgh.org.tw',
        'value' : 'A0001'
    }

@pytest.fixture
def status():
    return 'final'

@pytest.fixture
def type_coding():
    return [{
        'system' : 'http://loinc.org',
        'code' : '64291-8'
    }]

@pytest.fixture
def subject():
    return {
        'reference' : 'Patient/Patient-C1'
    }

@pytest.fixture
def date():
    return '2023-08-21T14:30:00+08:00'

@pytest.fixture
def author():
    return [{
        'reference' : 'Organization/Organization-min'
    }]

@pytest.fixture
def title():
    return '理賠用收據-診斷證明-檢驗紀錄'

@pytest.fixture
def section_title():
    return '理賠用收據-診斷證明-檢驗紀錄'

@pytest.fixture
def section_code():
    return {
        'coding' : [{
            'system' : 'http://loinc.org',
            'code' : '64291-8'
        }]
    }

@pytest.fixture
def section_entry():
    return [
        {
            'reference' : 'Claim/Claim-C1'
        },
        {
            'reference' : 'Coverage/Coverage-C1'
        },
        {
            'reference' : 'Organization/Organization-cathay'
        },
        {
            'reference' : 'Condition/Condition-C1'
        },
        {
            'reference' : 'DiagnosticReport/DiagnosticReport-C1'
        },
        {
            'reference' : 'Encounter/Encounter-C1'
        },
        {
            'reference' : 'Practitioner/Practitioner-Chen'
        },
        {
            'reference' : 'Practitioner/Practitioner-Ciou'
        },
        {
            'reference' : 'Practitioner/Practitioner-Wang1'
        },
        {
            'reference' : 'Observation/Observation-C1'
        }
    ]

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Composition',
        'id' : 'Composition-C1',
        'meta' : {
            'profile' : ['https://claim.cgh.org.tw/iclaim/StructureDefinition/composition-iclaim']
        },
        'identifier' : {
            'system' : 'https://www.cgh.org.tw',
            'value' : 'A0001'
        },
        'status' : 'final',
        'type' : {
            'coding' : [{
                'system' : 'http://loinc.org',
                'code' : '64291-8'
            }]
        },
        'subject' : {
            'reference' : 'Patient/Patient-C1'
        },
        'date' : '2023-08-21T14:30:00+08:00',
        'author' : [{
            'reference' : 'Organization/Organization-min'
        }],
        'title' : '理賠用收據-診斷證明-檢驗紀錄',
        'section' : [{
            'title' : '理賠用收據-診斷證明-檢驗紀錄',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '64291-8'
                }]
            },
            'entry' : [
                {
                    'reference' : 'Claim/Claim-C1'
                },
                {
                    'reference' : 'Coverage/Coverage-C1'
                },
                {
                    'reference' : 'Organization/Organization-cathay'
                },
                {
                    'reference' : 'Condition/Condition-C1'
                },
                {
                    'reference' : 'DiagnosticReport/DiagnosticReport-C1'
                },
                {
                    'reference' : 'Encounter/Encounter-C1'
                },
                {
                    'reference' : 'Practitioner/Practitioner-Chen'
                },
                {
                    'reference' : 'Practitioner/Practitioner-Ciou'
                },
                {
                    'reference' : 'Practitioner/Practitioner-Wang1'
                },
                {
                    'reference' : 'Observation/Observation-C1'
                }
            ]
        }]
    }
