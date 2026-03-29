import pytest
from fhir_data_generator import PatientLtc


@pytest.fixture
def patient_class():
    return PatientLtc('ltc-patient-chen-ming-hui')

@pytest.fixture
def profile_urls():
    return [
        'http://ltc-ig.fhir.tw/StructureDefinition/LTCPatient',
    ]

@pytest.fixture
def identifiers():
    return [{
        'use': 'official',
        'type': {
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                'code': 'PRN',
                'display': 'Provider Number'
            }]
        },
        'system': 'http://www.ankang-ltc.tw',
        'value': 'R2024001'
    },
    {
        'use': 'official',
        'type': {
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                'code': 'NNxxx',
                'display': 'National Person Identifier where the xxx is the ISO table 3166 3-character (alphabetic) country code'
            }],
            'text': 'National Person Identifier (TWN)'
        },
        'system': 'http://www.moi.gov.tw',
        'value': 'A123456789'
    }]

@pytest.fixture
def active():
    return True

@pytest.fixture
def names():
    return [{
        'use': 'official',
        'text': 'Chen Ming Hui'
    },
    {
        'use': 'usual',
        'text': '陳明慧'
    }]

@pytest.fixture
def telecom():
    return [{
        'system': 'phone',
        'value': '0912345678',
        'use': 'mobile'
    }]

@pytest.fixture
def gender():
    return 'female'

@pytest.fixture
def birth_date():
    return '1945-03-15'

@pytest.fixture
def address():
    return [{
        'use': 'home',
        'text': '新北市中和區安康路二段123號3樓301室',
        'line': ['安康路二段123號3樓301室'],
        'city': '中和區',
        'state': '新北市',
        'postalCode': '23511',
        'country': 'TW'
    },
    {
        'use': 'billing',
        'text': '台北市大安區和平東路二段76號2樓',
        'line': ['和平東路二段76號2樓'],
        'city': '大安區',
        'state': '台北市',
        'postalCode': '10663',
        'country': 'TW'
    }]

@pytest.fixture
def contact():
    return [{
        'relationship': [{
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/v2-0131',
                'code': 'N',
                'display': 'Next-of-Kin'
            }]
        }],
        'name': {
            'use': 'usual',
            'text': '陳志強'
        },
        'telecom': [{
            'system': 'phone',
            'value': '0987654321',
            'use': 'mobile'
        },
        {
            'system': 'phone',
            'value': '02-27031234',
            'use': 'home'
        }]
    }]

@pytest.fixture
def managing_organization():
    return {
        'reference': 'Organization/ltc-organization-example',
    }

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Patient',
        'id': 'ltc-patient-chen-ming-hui',
        'meta': {
            'profile': ['http://ltc-ig.fhir.tw/StructureDefinition/LTCPatient']
        },
        'identifier': [{
            'use': 'official',
            'type': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code': 'PRN',
                    'display': 'Provider Number'
                }]
            },
            'system': 'http://www.ankang-ltc.tw',
            'value': 'R2024001'
        },
        {
            'use': 'official',
            'type': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code': 'NNxxx',
                    'display': 'National Person Identifier where the xxx is the ISO table 3166 3-character (alphabetic) country code'
                }],
                'text': 'National Person Identifier (TWN)'
            },
            'system': 'http://www.moi.gov.tw',
            'value': 'A123456789'
        }],
        'active': True,
        'name': [{
            'use': 'official',
            'text': 'Chen Ming Hui'
        },
        {
            'use': 'usual',
            'text': '陳明慧'
        }],
        'telecom': [{
            'system': 'phone',
            'value': '0912345678',
            'use': 'mobile'
        }],
        'gender': 'female',
        'birthDate': '1945-03-15',
        'address': [{
            'use': 'home',
            'text': '新北市中和區安康路二段123號3樓301室',
            'line': ['安康路二段123號3樓301室'],
            'city': '中和區',
            'state': '新北市',
            'postalCode': '23511',
            'country': 'TW'
        },
        {
            'use': 'billing',
            'text': '台北市大安區和平東路二段76號2樓',
            'line': ['和平東路二段76號2樓'],
            'city': '大安區',
            'state': '台北市',
            'postalCode': '10663',
            'country': 'TW'
        }],
        'contact': [{
            'relationship': [{
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0131',
                    'code': 'N',
                    'display': 'Next-of-Kin'
                }]
            }],
            'name': {
                'use': 'usual',
                'text': '陳志強'
            },
            'telecom': [{
                'system': 'phone',
                'value': '0987654321',
                'use': 'mobile'
            },
            {
                'system': 'phone',
                'value': '02-27031234',
                'use': 'home'
            }]
        }],
        'managingOrganization': {
            'reference': 'Organization/ltc-organization-example'
        }
    }
