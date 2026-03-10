import pytest
from fhir_data_generator import LocationLtc as Location


@pytest.fixture
def location_class():
    return Location(location_id='ltc-location-example')

@pytest.fixture
def profile_urls():
    return [
        'http://ltc-ig.fhir.tw/StructureDefinition/Location-twltc'
    ]

@pytest.fixture
def status():
    return 'active'

@pytest.fixture
def name():
    return '新北市私立安康老人長期照顧中心（養護型）'

@pytest.fixture
def description():
    return '失智症個案陳明輝目前所在的日照中心'

@pytest.fixture
def mode():
    return 'instance'

@pytest.fixture
def types():
    return [{
        'coding': [{
            'system': 'http://terminology.hl7.org/CodeSystem/v3-RoleCode',
            'code': 'PTRES',
            'display': 'Patient\'s Residence'
        }]
    }]

@pytest.fixture
def address():
    return {
        'use': 'work',
        'type': 'physical',
        'text': '新北市中和區安康路二段123號'
    }

@pytest.fixture
def position():
    return {
        'longitude': 121.5089,
        'latitude': 24.9936,
        'altitude': 25.5
    }

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Location',
        'id': 'ltc-location-example',
        'meta': {
            'profile': ['http://ltc-ig.fhir.tw/StructureDefinition/Location-twltc']
        },
        'status': 'active',
        'name': '新北市私立安康老人長期照顧中心（養護型）',
        'description': '失智症個案陳明輝目前所在的日照中心',
        'mode': 'instance',
        'type': [{
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/v3-RoleCode',
                'code': 'PTRES',
                'display': 'Patient\'s Residence',
            }]
        }],
        'address': {
            'use': 'work',
            'type': 'physical',
            'text': '新北市中和區安康路二段123號'
        },
        'position': {
            'longitude': 121.5089,
            'latitude': 24.9936,
            'altitude': 25.5
        }
    }
