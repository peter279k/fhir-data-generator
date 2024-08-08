import pytest
from fhir_data_generator import TWCoreLocation as Location


@pytest.fixture
def location_class():
    return Location('loc-ent-example')

@pytest.fixture
def profile_urls():
    return [
        'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Location-twcore',
    ]

@pytest.fixture
def status():
    return 'active'

@pytest.fixture
def name():
    return '衛生福利部臺北醫院耳鼻喉科'

@pytest.fixture
def description():
    return '診治各種耳、鼻、咽、喉等上呼吸道疾病及頭頸部腫瘤 , 包括 : 感冒、咳嗽、頭痛、喉嚨痛、聲音沙啞、吞嚥困難、呼吸不順、鼻塞、鼻竇炎、鼻過敏、鼻息肉、扁桃腺肥大、耳鳴、耳痛、中耳炎、顏面神經麻痺、顎顳關節痛、口乾舌燥、打鼾、語言障礙、食道異物取出、頭頸部腫瘤、舌及口咽腫瘤手術'

@pytest.fixture
def mode():
    return 'kind'

@pytest.fixture
def type_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/v3-RoleCode',
        'code': 'ENT',
        'display': 'Otorhinolaryngology clinic'
    }]

@pytest.fixture
def telecom():
    return [{
        'system': 'phone',
        'value': '02-2276-5566',
        'use': 'work'
    }]

@pytest.fixture
def address():
    return {
        'use': 'work',
        'type': 'both',
        'text': '242新北市新莊區思源路127號',
        'line': ['思源路127號'],
        'city': '新莊區',
        'district': '新北市',
        'postalCode': '242'
    }

@pytest.fixture
def position():
    return {
        'longitude': 25.043085494729105,
        'latitude': 121.45941895179722
    }

@pytest.fixture
def managing_organization():
    return {
        'reference': 'Organization/org-hosp-example'
    }

@pytest.fixture
def hours_of_operation_days_of_week():
    return ['mon', 'tue', 'wed', 'thu', 'fri']

@pytest.fixture
def hours_of_operation_all_day():
    return True

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Location',
        'id': 'loc-ent-example',
        'meta': {
            'profile': [
                'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Location-twcore'
            ]
        },
        'status': 'active',
        'name': '衛生福利部臺北醫院耳鼻喉科',
        'description': '診治各種耳、鼻、咽、喉等上呼吸道疾病及頭頸部腫瘤 , 包括 : 感冒、咳嗽、頭痛、喉嚨痛、聲音沙啞、吞嚥困難、呼吸不順、鼻塞、鼻竇炎、鼻過敏、鼻息肉、扁桃腺肥大、耳鳴、耳痛、中耳炎、顏面神經麻痺、顎顳關節痛、口乾舌燥、打鼾、語言障礙、食道異物取出、頭頸部腫瘤、舌及口咽腫瘤手術',
        'mode': 'kind',
        'type': [{
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/v3-RoleCode',
                'code': 'ENT',
                'display': 'Otorhinolaryngology clinic'
            }]
        }],
        'telecom': [{
            'system': 'phone',
            'value': '02-2276-5566',
            'use': 'work'
        }],
        'address': {
            'use': 'work',
            'type': 'both',
            'text': '242新北市新莊區思源路127號',
            'line': ['思源路127號'],
            'city': '新莊區',
            'district': '新北市',
            'postalCode': '242'
        },
        'position': {
            'longitude': 25.043085494729105,
            'latitude': 121.45941895179722
        },
        'managingOrganization': {
            'reference': 'Organization/org-hosp-example'
        },
        'hoursOfOperation': [{
            'daysOfWeek': ['mon', 'tue', 'wed', 'thu', 'fri'],
            'allDay': True
        }]
    }
