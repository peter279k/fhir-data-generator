import pytest
from fhir_data_generator import TWCoreDocumentReference as DocumentReference


@pytest.fixture
def document_reference_class():
    return DocumentReference('doc-outpatient-example')

@pytest.fixture
def profile_urls():
    return [
        'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/DocumentReference-twcore'
    ]

@pytest.fixture
def status():
    return 'current'

@pytest.fixture
def type_coding():
    return [{
        'system': 'http://loinc.org',
        'code': '34108-1',
        'display':
        'Outpatient Note'
    }]

@pytest.fixture
def type_text():
    return '門診紀錄'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/pat-example'
    }

@pytest.fixture
def date():
    return '2024-01-23T12:34:56Z'

@pytest.fixture
def author():
    return [{
        'reference': 'Practitioner/pra-dr-example'
    }]

@pytest.fixture
def custodian():
    return {
        'reference': 'Organization/org-hosp-example'
    }

@pytest.fixture
def content():
    return [{
        'attachment': {
            'contentType': 'application/pdf',
            'url': 'ConsultationReport.pdf',
            'title': 'Consultation Report'
        }
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'DocumentReference',
        'id': 'doc-outpatient-example',
        'meta': {
            'profile': [
                'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/DocumentReference-twcore'
            ]
        },
        'status': 'current',
        'type': {
            'coding': [{
                'system': 'http://loinc.org',
                'code': '34108-1',
                'display': 'Outpatient Note'
            }],
            'text': '門診紀錄'
        },
        'subject': {
            'reference': 'Patient/pat-example'
        },
        'date': '2024-01-23T12:34:56Z',
        'author': [{
            'reference': 'Practitioner/pra-dr-example'
        }],
        'custodian': {
            'reference': 'Organization/org-hosp-example'
        },
        'content': [{
            'attachment': {
                'contentType': 'application/pdf',
                'url': 'ConsultationReport.pdf',
                'title': 'Consultation Report'
            }
        }]
    }
