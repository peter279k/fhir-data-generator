import pytest
from fhir_data_generator import CompositionImri as Composition


@pytest.fixture
def composition_class():
    return Composition('CompositionOperationNote-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/composition-operationnote-imri',
    ]

@pytest.fixture
def status():
    return 'final'

@pytest.fixture
def type_coding():
    return [{
        'system' : 'http://loinc.org',
        'code' : '11504-8',
        'display' : 'Surgical operation note'
    }]

@pytest.fixture
def subject():
    return {
        'reference' : 'Patient/Patient-min'
    }

@pytest.fixture
def date():
    return '2024-05-12T14:30:00+08:00'

@pytest.fixture
def author():
    return [
        {
            'reference' : 'Organization/OrganizationHosp-min'
        }
    ]

@pytest.fixture
def title():
    return '手術紀錄'

@pytest.fixture
def section():
    return [{
            'title' : '病人資訊',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '52460-3',
                    'display' : 'Patient Information'
                }]
            },
            'section' : [{
                'code' : {
                    'coding' : [{
                        'system' : 'http://loinc.org',
                        'code' : '882-1',
                        'display' : 'ABO and Rh group [Type] in Blood'
                    }]
                },
                'entry' : [{
                    'reference' : 'Observation/ObservationBloodType-min'
                }]
            }]
        },
        {
            'title' : '手術資訊',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '11504-8',
                    'display' : 'Surgical operation note'
                }]
            },
            'entry' : [{
                'reference' : 'Procedure/Procedure-pro'
            }],
            'section' : [{
                'code' : {
                    'coding' : [{
                        'system' : 'http://loinc.org',
                        'code' : '10218-6',
                        'display' : 'Surgical operation note postoperative diagnosis Narrative'
                    }]
                },
                'entry' : [{
                    'reference' : 'Condition/Condition-postope'
                }]
            },
            {
                'code' : {
                    'coding' : [{
                        'system' : 'http://loinc.org',
                        'code' : '59770-8',
                        'display' : 'Procedure estimated blood loss Narrative'
                    }]
                },
                'entry' : [{
                    'reference' : 'Observation/ObservationBloodLoss-min'
                }]
            },
            {
                'code' : {
                    'coding' : [{
                        'system' : 'http://loinc.org',
                        'code' : '59774-0',
                        'display' : 'Procedure anesthesia Narrative'
                    }]
                },
                'entry' : [{
                    'reference' : 'Procedure/ProcedureAnesthesiaMode-min'
                }]
            }]
        }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Composition',
        'id' : 'CompositionOperationNote-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/composition-operationnote-imri']
        },
        'status' : 'final',
        'type' : {
            'coding' : [{
                'system' : 'http://loinc.org',
                'code' : '11504-8',
                'display' : 'Surgical operation note'
            }]
        },
        'subject' : {
            'reference' : 'Patient/Patient-min'
        },
        'date' : '2024-05-12T14:30:00+08:00',
        'author' : [{
            'reference' : 'Organization/OrganizationHosp-min'
        }],
        'title' : '手術紀錄',
        'section' : [{
            'title' : '病人資訊',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '52460-3',
                    'display' : 'Patient Information'
                }]
            },
            'section' : [{
                'code' : {
                    'coding' : [{
                        'system' : 'http://loinc.org',
                        'code' : '882-1',
                        'display' : 'ABO and Rh group [Type] in Blood'
                    }]
                },
                'entry' : [{
                    'reference' : 'Observation/ObservationBloodType-min'
                }]
            }]
        },
        {
            'title' : '手術資訊',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '11504-8',
                    'display' : 'Surgical operation note'
                }]
            },
            'entry' : [{
                'reference' : 'Procedure/Procedure-pro'
            }],
            'section' : [{
                'code' : {
                    'coding' : [{
                        'system' : 'http://loinc.org',
                        'code' : '10218-6',
                        'display' : 'Surgical operation note postoperative diagnosis Narrative'
                    }]
                },
                'entry' : [{
                    'reference' : 'Condition/Condition-postope'
                }]
            },
            {
                'code' : {
                    'coding' : [{
                        'system' : 'http://loinc.org',
                        'code' : '59770-8',
                        'display' : 'Procedure estimated blood loss Narrative'
                    }]
                },
                'entry' : [{
                    'reference' : 'Observation/ObservationBloodLoss-min'
                }]
            },
            {
                'code' : {
                    'coding' : [{
                        'system' : 'http://loinc.org',
                        'code' : '59774-0',
                        'display' : 'Procedure anesthesia Narrative'
                    }]
                },
                'entry' : [{
                    'reference' : 'Procedure/ProcedureAnesthesiaMode-min'
                }]
            }]
        }]
    }
