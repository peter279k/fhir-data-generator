import pytest
from fhir_data_generator import DocumentReferenceImri as DocumentReference


@pytest.fixture
def document_reference_class():
    return DocumentReference('DocumentReference-min')

@pytest.fixture
def profile_urls():
    return [
        'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/DocumentReference-twcore'
    ]

@pytest.fixture
def status():
    return 'current'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/Patient-min'
    }

@pytest.fixture
def content():
    return [{
        'attachment' : {
            'contentType' : 'image/png',
            'url' : 'https://telegraph-image-55i.pages.dev/file/3830a304a2eb70419c80a.png',
            'title' : 'gallbladder polyp'
        }
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'DocumentReference',
        'id' : 'DocumentReference-min',
        'meta' : {
            'profile' : ['https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/DocumentReference-twcore']
        },
        'status' : 'current',
        'subject' : {
            'reference' : 'Patient/Patient-min'
        },
        'content' : [{
            'attachment' : {
                'contentType' : 'image/png',
                'url' : 'https://telegraph-image-55i.pages.dev/file/3830a304a2eb70419c80a.png',
                'title' : 'gallbladder polyp'
            }
        }]
    }
