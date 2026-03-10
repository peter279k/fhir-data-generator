import pytest
from fhir_data_generator import QuestionnaireResponse


@pytest.fixture
def questionnaire_response_classes():
    return [
        QuestionnaireResponse(response_id='ltc-questionnaire-response-cdr-moderate-example'),
        QuestionnaireResponse(response_id='ltc-questionnaire-response-cdr-example'),
        QuestionnaireResponse(response_id='ltc-questionnaire-response-cdr-complete-example'),
    ]

@pytest.fixture
def profile_urls():
    return [
        'http://ltc-ig.fhir.tw/StructureDefinition/LTCQuestionnaireResponseCDR'
    ]

@pytest.fixture
def extensions():
    return [
        [{
            'url': 'http://ltc-ig.fhir.tw/StructureDefinition/cdr-total-score',
            'valueInteger': 2
        }],
        [{
            'url': 'http://ltc-ig.fhir.tw/StructureDefinition/cdr-total-score',
            'valueInteger': 1
        }],
        [{
            'url': 'http://ltc-ig.fhir.tw/StructureDefinition/cdr-total-score',
            'valueInteger': 1
        }],
    ]

@pytest.fixture
def questionnaire():
    return 'http://ltc-ig.fhir.tw/Questionnaire/ltc-questionnaire-cdr'

@pytest.fixture
def status():
    return 'completed'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/ltc-patient-chen-ming-hui',
    }

@pytest.fixture
def authored_lists():
    return [
        '2024-01-15T10:30:00+08:00',
        '2024-01-15T10:30:00+08:00',
        '2024-01-15T10:30:00+08:00',
    ]

@pytest.fixture
def author():
    return {
        'reference': 'Practitioner/ltc-practitioner-physician-aa12-example',
    }

@pytest.fixture
def source():
    return {
        'reference': 'Patient/ltc-patient-chen-ming-hui',
    }

@pytest.fixture
def items():
    return [
        [{
            'linkId': 'CDR-1',
            'text': '記憶力',
            'answer': [{
                'valueInteger': 3
            }]
        },
        {
            'linkId': 'CDR-2',
            'text': '定向感',
            'answer': [{
                'valueInteger': 3
            }]
        },
        {
            'linkId': 'CDR-3',
            'text': '解決問題能力',
            'answer': [{
                'valueInteger': 3
            }]
        },
        {
            'linkId': 'CDR-4',
            'text': '社區活動能力',
            'answer': [{
                'valueInteger': 3
            }]
        },
        {
            'linkId': 'CDR-5',
            'text': '家居嗜好',
            'answer': [{
                'valueInteger': 3
            }]
        },
        {
            'linkId': 'CDR-6',
            'text': '自我照料',
            'answer': [{
                'valueInteger': 2
            }]
        },
        {
            'linkId': 'CDR-Total',
            'text': '目前的失智期',
            'answer': [{
                'valueInteger': 2
            }]
        }],
        [{
            'linkId': 'CDR-1',
            'text': '記憶力',
            'answer': [{
                'valueInteger': 1
            }]
        },
        {
            'linkId': 'CDR-2',
            'text': '定向感',
            'answer': [{
                'valueInteger': 1
            }]
        },
        {
            'linkId': 'CDR-3',
            'text': '解決問題能力',
            'answer': [{
                'valueInteger': 1
            }]
        },
        {
            'linkId': 'CDR-4',
            'text': '社區活動能力',
            'answer': [{
                'valueInteger': 1
            }]
        },
        {
            'linkId': 'CDR-5',
            'text': '家居嗜好',
            'answer': [{
                'valueInteger': 1
            }]
        },
        {
            'linkId': 'CDR-6',
            'text': '自我照料',
            'answer': [{
                'valueInteger': 0
            }]
        },
        {
            'linkId': 'CDR-Total',
            'text': '目前的失智期',
            'answer': [{
                'valueInteger': 1
            }]
        }],
        [{
            'linkId': 'CDR-1',
            'text': '記憶力',
            'answer': [{
                'valueInteger': 1
            }]
        },
        {
            'linkId': 'CDR-2',
            'text': '定向感',
            'answer': [{
                'valueInteger': 1
            }]
        },
        {
            'linkId': 'CDR-3',
            'text': '解決問題能力',
            'answer': [{
                'valueInteger': 1
            }]
        },
        {
            'linkId': 'CDR-4',
            'text': '社區活動能力',
            'answer': [{
                'valueInteger': 1
            }]
        },
        {
            'linkId': 'CDR-5',
            'text': '家居嗜好',
            'answer': [{
                'valueInteger': 1
            }]
        },
        {
            'linkId': 'CDR-6',
            'text': '自我照料',
            'answer': [{
                'valueInteger': 0
            }]
        },
        {
            'linkId': 'CDR-Total',
            'text': '目前的失智期',
            'answer': [{
                'valueInteger': 1
            }]
        }]
    ]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'QuestionnaireResponse',
        'id': '',
        'meta': {
            'profile': ['http://ltc-ig.fhir.tw/StructureDefinition/LTCQuestionnaireResponseCDR']
        },
        'extension': [],
        'questionnaire': 'http://ltc-ig.fhir.tw/Questionnaire/ltc-questionnaire-cdr',
        'status': 'completed',
        'subject': {
            'reference': 'Patient/ltc-patient-chen-ming-hui'
        },
        'authored': '',
        'author': {
            'reference': 'Practitioner/ltc-practitioner-physician-aa12-example'
        },
        'source': {
            'reference': 'Patient/ltc-patient-chen-ming-hui'
        },
        'item': [],
    }
