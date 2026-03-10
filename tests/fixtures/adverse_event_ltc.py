import pytest
from fhir_data_generator import AdverseEventLtc as AdverseEvent


@pytest.fixture
def adverse_event_classes():
    return [
        AdverseEvent(event_id='ltc-adverseevent-cs100-example'),
        AdverseEvent(event_id='ltc-adverse-event-example'),
    ]

@pytest.fixture
def profile_urls():
    return [
        'http://ltc-ig.fhir.tw/StructureDefinition/AdverseEvent-twltc',
    ]

@pytest.fixture
def extension():
    return [{
        'extension': [{
            'url': 'textType',
            'valueCodeableConcept': {
                'coding': [{
                    'system': 'http://ltc-ig.fhir.tw/CodeSystem/cs-tw-ltc-incident-texttype',
                    'code': 'desc',
                    'display': '事件描述'
                }]
            }
        },
        {
            'url': 'text',
            'valueString': '巡視時發現個案暈眩跌坐於地，已聯繫家屬與機構。'
        }],
        'url': 'http://ltc-ig.fhir.tw/StructureDefinition/Ext-TW-LTC-AdverseEvent-Description'
    }]

@pytest.fixture
def identifiers():
    return [
        {
            'use': 'official',
            'system': 'http://ltc-ig.fhir.tw/adverse-event',
            'value': 'AE-CS100-2025-001'
        },
        {
            'use': 'official',
            'system': 'http://ltc-ig.fhir.tw/adverse-event',
            'value': 'AE-2024-001'
        },
    ]

@pytest.fixture
def actuality():
    return 'actual'

@pytest.fixture
def events():
    return [
        {
            'coding': [{
                'system': 'http://ltc-ig.fhir.tw/CodeSystem/cs-tw-ltc-incident-category',
                'code': 'careacc',
                'display': '照顧意外事件'
            }]
        },
        {
            'text': '離開安全區域',
        },
  ]

@pytest.fixture
def subjects():
    return [
        {
            'reference': 'Patient/ltc-patient-cs100-example'
        },
        {
            'reference': 'Patient/ltc-patient-chen-ming-hui'
        },
    ]

@pytest.fixture
def dates():
    return ['2025-11-05T10:20:00+08:00', '2024-01-15T14:30:00+08:00']

@pytest.fixture
def detected():
    return '2024-01-15T14:32:00+08:00'

@pytest.fixture
def recorded_dates():
    return ['2025-11-05T10:30:00+08:00', '2024-01-15T14:35:00+08:00']

@pytest.fixture
def location():
    return {
        'reference': 'Location/ltc-location-example'
    }

@pytest.fixture
def seriousness():
    return {
        'coding': [{
            'system': 'http://terminology.hl7.org/CodeSystem/adverse-event-seriousness',
            'code': 'serious',
            'display': 'Serious'
        }]
    }

@pytest.fixture
def severity():
    return {
        'coding': [{
            'system': 'http://terminology.hl7.org/CodeSystem/adverse-event-severity',
            'code': 'moderate',
            'display': 'Moderate'
        }]
    }

@pytest.fixture
def outcome():
    return {
        'coding': [{
            'system': 'http://terminology.hl7.org/CodeSystem/adverse-event-outcome',
            'code': 'recovering',
            'display': 'Recovering'
        }]
    }

@pytest.fixture
def recorder():
    return {
        'reference': 'Practitioner/ltc-practitioner-example'
    }

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'AdverseEvent',
        'id': '',
        'meta': {
            'profile': ['http://ltc-ig.fhir.tw/StructureDefinition/AdverseEvent-twltc']
        },
        'extension': [],
        'identifier': {},
        'actuality': 'actual',
        'event': {},
        'subject': {},
        'date': '',
        'detected': '',
        'recordedDate': '',
        'location': {},
        'seriousness': {},
        'severity': {},
        'outcome': {},
        'recorder': {},
    }
