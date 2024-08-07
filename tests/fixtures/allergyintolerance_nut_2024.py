import pytest
from fhir_data_generator import AllergyIntoleranceNut


@pytest.fixture
def allergy_intolerance_class():
    return AllergyIntoleranceNut('all-nut-example')

@pytest.fixture
def profile_urls():
    return [
        'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/AllergyIntolerance-twcore',
    ]

@pytest.fixture
def clinical_status_coding():
    return [{
        'system' : 'http://terminology.hl7.org/CodeSystem/allergyintolerance-clinical',
        'code' : 'active',
        'display' : 'Active',
    }]

@pytest.fixture
def clinical_status_text():
    return 'Active'

@pytest.fixture
def verification_status_coding():
    return [{
        'system' : 'http://terminology.hl7.org/CodeSystem/allergyintolerance-verification',
        'code' : 'confirmed',
        'display' : 'Confirmed',
    }]

@pytest.fixture
def verification_status_text():
    return 'Confirmed'

@pytest.fixture
def category():
    return ['food']

@pytest.fixture
def criticality():
    return 'high'

@pytest.fixture
def code_coding():
    return [{
        'system' : 'http://snomed.info/sct',
        'code' : '91934008',
        'display' : 'Nut allergy'
    }]

@pytest.fixture
def code_text():
    return '堅果過敏'

@pytest.fixture
def patient():
    return {
        'reference' : 'Patient/pat-example',
        'display' : '陳加玲',
    }

@pytest.fixture
def onset_datetime():
    return '2023-09-03T10:15:00Z'

@pytest.fixture
def recorded_date():
    return '2023-09-03T14:30:00Z'

@pytest.fixture
def recorder():
    return {
        'reference' : 'Practitioner/pra-dr-example',
        'display' : '王依昇',
    }

@pytest.fixture
def asserter():
    return {
        'reference' : 'Practitioner/pra-nurse-example',
        'display' : '陳莉',
    }

@pytest.fixture
def last_occurrence():
    return '2023-09-03T14:30:00Z'

@pytest.fixture
def note():
    return [{
        'text' : '患者對堅果與添加堅果的食品過敏，可能導致皮膚發癢、紅腫',
    }]

@pytest.fixture
def reaction_description():
    return '皮膚發癢、紅腫'

@pytest.fixture
def reaction_severity():
    return 'severe'

@pytest.fixture
def reaction_exposure_route_text():
    return '口服'

@pytest.fixture
def reaction_note():
    return [{
      'text' : '患者在食用堅果後出現皮膚發癢和紅腫，症狀於2023年9月3日下午2:30發作'
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'AllergyIntolerance',
        'id': 'all-nut-example',
        'meta': {
            'profile': [
                'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/AllergyIntolerance-twcore'
            ]
        },
        'clinicalStatus': {
            'coding': [
                {
                    'system': 'http://terminology.hl7.org/CodeSystem/allergyintolerance-clinical',
                    'code': 'active', 'display': 'Active'
                }
            ],
            'text': 'Active'
        },
        'verificationStatus': {
            'coding': [
                {
                    'system': 'http://terminology.hl7.org/CodeSystem/allergyintolerance-verification',
                    'code': 'confirmed', 'display': 'Confirmed'
                }
            ],
            'text': 'Confirmed'
        },
        'type': 'allergy',
        'category': ['food'],
        'criticality': 'high',
        'code': {
            'coding': [
                {
                    'system': 'http://snomed.info/sct',
                    'code': '91934008',
                    'display': 'Nut allergy'
                }
            ],
            'text': '堅果過敏'
        },
        'patient': {
            'reference': 'Patient/pat-example',
            'display': '陳加玲'
        },
        'onsetDateTime': '2023-09-03T10:15:00Z',
        'recordedDate': '2023-09-03T14:30:00Z',
        'recorder': {
            'reference': 'Practitioner/pra-dr-example',
            'display': '王依昇'
        },
        'asserter': {
            'reference': 'Practitioner/pra-nurse-example',
            'display': '陳莉'
        },
        'lastOccurrence': '2023-09-03T14:30:00Z',
        'note': [
            {
                'text': '患者對堅果與添加堅果的食品過敏，可能導致皮膚發癢、紅腫'
            }
        ],
        'reaction': [
            {
                'substance': {
                    'coding': [
                        {
                            'system': 'http://snomed.info/sct',
                            'code': '3193000',
                            'display': 'alpha-1,4-Glucan-protein synthase (uridine diphosphate-forming)'
                        }
                    ],
                    'text': 'alpha-1,4-Glucan-protein synthase (uridine diphosphate-forming)'
                },
                'manifestation': [
                    {
                        'coding': [
                            {
                                'system': 'http://snomed.info/sct',
                                'code': '39579001',
                                'display': 'Anaphylaxis (disorder)'
                            }
                        ]
                    }
                ],
                'description': '皮膚發癢、紅腫',
                'severity': 'severe',
                'exposureRoute': {
                    'coding': [
                        {
                            'system': 'http://snomed.info/sct',
                            'code': '26643006',
                            'display': 'Oral use'
                        }
                    ],
                    'text': '口服'
                },
                'note': [
                    {
                        'text': '患者在食用堅果後出現皮膚發癢和紅腫，症狀於2023年9月3日下午2:30發作'
                    }
                ]
            }
        ]
    }
