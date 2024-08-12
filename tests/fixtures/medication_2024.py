import pytest
from fhir_data_generator import TWCoreMedication as Medication


@pytest.fixture
def medication_class():
    return Medication('med-example')

@pytest.fixture
def profile_urls():
    return [
        'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Medication-twcore',
    ]

@pytest.fixture
def code_coding():
    return [
        {
            'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medication-fda-tw',
            'code': '衛署藥輸字第025485號',
            'display': '阿立批挫'
        }
    ]

@pytest.fixture
def code_text():
    return '阿立批挫'

@pytest.fixture
def form_coding():
    return [
        {
            'system': 'http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm',
            'code': 'POWD'
        }
    ]

@pytest.fixture
def form_text():
    return '粉'

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Medication',
        'id': 'med-example',
        'meta': {
            'profile': [
                'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Medication-twcore'
            ]
        },
        'code': {
            'coding': [
                {
                    'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medication-fda-tw',
                    'code': '衛署藥輸字第025485號',
                    'display': '阿立批挫'
                }
            ],
            'text': '阿立批挫'
        },
        'form': {
            'coding': [
                {
                    'system': 'http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm',
                    'code': 'POWD'
                }
            ],
            'text': '粉'
        }
    }
