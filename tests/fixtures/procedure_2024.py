import pytest
from fhir_data_generator import TWCoreProcedure as Procedure


@pytest.fixture
def procedure_class():
    return Procedure(procedure_id='pro-example')

@pytest.fixture
def profile_urls():
    return [
        'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Procedure-twcore'
    ]

@pytest.fixture
def status():
    return 'completed'

@pytest.fixture
def code_coding():
    return [{
        'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-10-pcs-2021-tw',
        'code': 'BU46ZZZ'
    }]

@pytest.fixture
def code_text():
    return '子宮超音波'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/pat-example'
    }

@pytest.fixture
def performed_date_time():
    return '2022-08-12'

@pytest.fixture
def asserter():
    return {
        'reference': 'Practitioner/pra-dr-example'
    }

@pytest.fixture
def performer():
    return [{
        'actor': {
            'reference': 'Practitioner/pra-dr-example'
        },
        'onBehalfOf': {
            'reference': 'Organization/org-hosp-example'
        }
    }]

@pytest.fixture
def body_site_coding():
    return [{
        'system': 'http://snomed.info/sct',
        'code': '9258009'
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Procedure',
        'id': 'pro-example',
        'meta': {
            'profile': [
                'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Procedure-twcore'
            ]
        },
        'status': 'completed',
        'code': {
            'coding': [{
                'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-10-pcs-2021-tw',
                'code': 'BU46ZZZ'
            }],
            'text': '子宮超音波'
        },
        'subject': {
            'reference': 'Patient/pat-example'
        },
        'performedDateTime': '2022-08-12',
        'asserter': {
            'reference': 'Practitioner/pra-dr-example'
        },
        'performer': [{
            'actor': {
                'reference': 'Practitioner/pra-dr-example'
            },
            'onBehalfOf': {
                'reference': 'Organization/org-hosp-example'
            }
        }],
        'bodySite': [{
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '9258009'
            }]
        }]
    }
