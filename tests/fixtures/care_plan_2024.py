import pytest
from fhir_data_generator import CarePlan


@pytest.fixture
def care_plan_class():
    return CarePlan('careplan-example')

@pytest.fixture
def profile_urls():
    return [
        'https://hapi.fhir.tw/fhir/StructureDefinition/Careplan-sport',
    ]

@pytest.fixture
def status():
    return 'active'

@pytest.fixture
def intent():
    return 'plan'

@pytest.fixture
def category_coding():
    return [
        {
            'system': 'https://hapi.fhir.tw/fhir/CodeSystem/tempcode',
            'code': 'PhysicalActivity',
            'display': 'Physical Activity'
        }
    ]

@pytest.fixture
def description():
    return '椎間盤間隔小/退化擠壓狀況 核心訓練以髖部(臀部)和腹部訓練為主'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/patient-tw-example',
    }

@pytest.fixture
def author():
    return {
        'reference': 'Practitioner/practitioner-c-example'
    }

@pytest.fixture
def goal():
    return [{
        'reference': 'Goal/goal-example',
    }]

@pytest.fixture
def activity_progress():
    return [
        {
            'time': '2024-07-03',
            'text': '滾筒放鬆：1.胸椎伸展 8趟 2.上背滾動 10趟 3.胸椎旋轉 左右各8次 核心：1.死蟲 後腳跟點地板 單邊各六下 兩組 2.橋式+彈力圈 20下 1組 3.徒手弓箭步 單側負重6公斤10下一組,前腳墊高10下一組',
        },
    ]

@pytest.fixture
def activity_detail():
    return {
        'status': 'completed',
        'description': '機械臀推/彈力箱臀推 感受度不佳 暫時不做',
    }

@pytest.fixture
def note():
    return [{
        'time': '2024-07-04',
        'text': '肚臍對應後方腰椎摸會痛，活動筋骨及輕微推拿後有好一點',
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'CarePlan',
        'id': 'careplan-example',
        'meta': {
            'profile': [
                'https://hapi.fhir.tw/fhir/StructureDefinition/Careplan-sport'
            ]
        },
        'status': 'active',
        'intent': 'plan',
        'category': [
            {
                'coding': [
                    {
                        'system': 'https://hapi.fhir.tw/fhir/CodeSystem/tempcode',
                        'code': 'PhysicalActivity',
                        'display': 'Physical Activity'
                    }
                ]
            }
        ],
        'description': '椎間盤間隔小/退化擠壓狀況 核心訓練以髖部(臀部)和腹部訓練為主',
        'subject': {
            'reference': 'Patient/patient-tw-example',
        },
        'author': {
            'reference': 'Practitioner/practitioner-c-example'
        },
        'goal': [
            {
                'reference': 'Goal/goal-example',
            }
        ],
        'activity': [
            {
                'progress': [
                    {
                        'time': '2024-07-03',
                        'text': '滾筒放鬆：1.胸椎伸展 8趟 2.上背滾動 10趟 3.胸椎旋轉 左右各8次 核心：1.死蟲 後腳跟點地板 單邊各六下 兩組 2.橋式+彈力圈 20下 1組 3.徒手弓箭步 單側負重6公斤10下一組,前腳墊高10下一組',
                    },
                ],
                'detail': {
                    'status': 'completed',
                    'description': '機械臀推/彈力箱臀推 感受度不佳 暫時不做',
                },
            },
        ],
        'note': [
            {
                'time': '2024-07-04',
                'text': '肚臍對應後方腰椎摸會痛，活動筋骨及輕微推拿後有好一點',
            }
        ],
    }
