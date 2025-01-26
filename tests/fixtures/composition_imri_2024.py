import pytest
from fhir_data_generator import CompositionImri as Composition


@pytest.fixture
def composition_class():
    return Composition('CompositionDischargeSummary-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/composition-dischargesummary-imri',
    ]

@pytest.fixture
def status():
    return 'final'

@pytest.fixture
def type_coding():
    return [{
        'system' : 'http://loinc.org',
        'code' : '18842-5',
        'display' : 'Discharge summary'
    }]

@pytest.fixture
def subject():
    return {
        'reference' : 'Patient/Patient-min'
    }

@pytest.fixture
def encounter():
    return {
        'reference' : 'Encounter/Encounter-min'
    }

@pytest.fixture
def date():
    return '2024-05-12T14:30:00+08:00'

@pytest.fixture
def author():
    return [
        {
            'reference' : 'Organization/OrganizationHosp-min'
        },
        {
            'reference' : 'Practitioner/Practitioner-min'
        }
    ]

@pytest.fixture
def title():
    return '出院病歷摘要'

@pytest.fixture
def section():
    return [{
            'title' : '住院臆斷',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '46241-6',
                    'display' : 'Hospital admission diagnosis Narrative - Reported'
                }]
            },
            'entry' : [{
                'reference' : 'Observation/ObservationImpression-min'
            }]
        },
        {
            'title' : '出院診斷',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '11535-2',
                    'display' : 'Hospital discharge Dx Narrative'
                }]
            },
            'entry' : [{
                'reference' : 'Condition/ConditionDischargeDiagnosis-min'
            }]
        },
        {
            'title' : '癌症期別',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '22037-6',
                    'display' : 'Staging Cancer Narrative'
                }]
            },
            'entry' : [{
                'reference' : 'Observation/ObservationCancerStaging-min'
            }]
        },
        {
            'title' : '主訴',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '10154-3',
                    'display' : 'Chief complaint Narrative - Reported'
                }]
            },
            'entry' : [{
                'reference' : 'Condition/ConditionChiefComplaint-min'
            }]
        },
        {
            'title' : '病史',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '10164-2',
                    'display' : 'History of Present illness Narrative'
                }]
            },
            'entry' : [{
                'reference' : 'Condition/ConditionPresentIllness-min'
            }]
        },
        {
            'title' : '理學檢查發現',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '29545-1',
                    'display' : 'Physical findings Narrative'
                }]
            },
            'entry' : [{
                'reference' : 'Observation/ObservationPhysicalExamination-min'
            }]
        },
        {
            'title' : '檢驗與特殊檢查',
                'code' : {
                    'coding' : [{
                        'system' : 'http://loinc.org',
                        'code' : '30954-2',
                        'display' : 'Relevant diagnostic tests/laboratory data Narrative'
                    }]
                },
            'entry' : [{
                    'reference' : 'Observation/ObservationLaboratory-min'
                },
                {
                    'reference' : 'Observation/ObservationLaboratory-lab'
                }]
        },
        {
            'title' : '醫療影像檢查',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '18748-4',
                    'display' : 'Diagnostic imaging study'
                }]
            },
            'entry' : [{
                'reference' : 'ImagingStudy/ImagingStudy-min'
            }]
        },
        {
            'title' : '病理報告',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '22034-3',
                    'display' : 'Pathology report Cancer Narrative'
                }]
            },
            'entry' : [{
                'reference' : 'Observation/ObservationPathologyReport-min'
            }]
        },
        {
            'title' : '手術日期及方法',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '8724-7',
                    'display' : 'Surgical operation note description Narrative'
                }]
            },
            'entry' : [{
                'reference' : 'Procedure/Procedure-min'
            }]
        },
        {
            'title' : '住院治療經過',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '8648-8',
                    'display' : 'Hospital course Narrative'
                }]
            },
            'entry' : [{
                'reference' : 'Procedure/ProcedureHospitalCourse-min'
            },
            {
                'reference' : 'Location/Location-min'
            }]
        },
        {
            'title' : '合併症與併發症',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '55109-3',
                    'display' : 'Complications Document'
                }]
            },
            'entry' : [{
                'reference' : 'Condition/ConditionComorbiditiesandComplications-min'
            }]
        },
        {
            'title' : '出院指示',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '8653-8',
                    'display' : 'Hospital Discharge instructions'
                }]
            },
            'entry' : [{
                'reference' : 'CarePlan/CarePlan-min'
            },
            {
                'reference' : 'MedicationRequest/MedicationRequest-min'
            }]
        }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Composition',
        'id' : 'CompositionDischargeSummary-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/composition-dischargesummary-imri']
        },
        'status' : 'final',
        'type' : {
            'coding' : [{
                'system' : 'http://loinc.org',
                'code' : '18842-5',
                'display' : 'Discharge summary'
            }]
        },
        'subject' : {
            'reference' : 'Patient/Patient-min'
        },
        'encounter' : {
            'reference' : 'Encounter/Encounter-min'
        },
        'date' : '2024-05-12T14:30:00+08:00',
        'author' : [{
            'reference' : 'Organization/OrganizationHosp-min'
            },
            {
                'reference' : 'Practitioner/Practitioner-min'
        }],
        'title' : '出院病歷摘要',
        'section' : [{
            'title' : '住院臆斷',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '46241-6',
                    'display' : 'Hospital admission diagnosis Narrative - Reported'
                }]
            },
            'entry' : [{
                'reference' : 'Observation/ObservationImpression-min'
            }]
        },
        {
            'title' : '出院診斷',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '11535-2',
                    'display' : 'Hospital discharge Dx Narrative'
                }]
            },
            'entry' : [{
                'reference' : 'Condition/ConditionDischargeDiagnosis-min'
            }]
        },
        {
            'title' : '癌症期別',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '22037-6',
                    'display' : 'Staging Cancer Narrative'
                }]
            },
            'entry' : [{
                'reference' : 'Observation/ObservationCancerStaging-min'
            }]
        },
        {
            'title' : '主訴',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '10154-3',
                    'display' : 'Chief complaint Narrative - Reported'
                }]
            },
            'entry' : [{
                'reference' : 'Condition/ConditionChiefComplaint-min'
            }]
        },
        {
            'title' : '病史',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '10164-2',
                    'display' : 'History of Present illness Narrative'
                }]
            },
            'entry' : [{
                'reference' : 'Condition/ConditionPresentIllness-min'
            }]
        },
        {
            'title' : '理學檢查發現',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '29545-1',
                    'display' : 'Physical findings Narrative'
                }]
            },
            'entry' : [{
                'reference' : 'Observation/ObservationPhysicalExamination-min'
            }]
        },
        {
            'title' : '檢驗與特殊檢查',
                'code' : {
                    'coding' : [{
                        'system' : 'http://loinc.org',
                        'code' : '30954-2',
                        'display' : 'Relevant diagnostic tests/laboratory data Narrative'
                    }]
                },
            'entry' : [{
                    'reference' : 'Observation/ObservationLaboratory-min'
                },
                {
                    'reference' : 'Observation/ObservationLaboratory-lab'
                }]
        },
        {
            'title' : '醫療影像檢查',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '18748-4',
                    'display' : 'Diagnostic imaging study'
                }]
            },
            'entry' : [{
                'reference' : 'ImagingStudy/ImagingStudy-min'
            }]
        },
        {
            'title' : '病理報告',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '22034-3',
                    'display' : 'Pathology report Cancer Narrative'
                }]
            },
            'entry' : [{
                'reference' : 'Observation/ObservationPathologyReport-min'
            }]
        },
        {
            'title' : '手術日期及方法',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '8724-7',
                    'display' : 'Surgical operation note description Narrative'
                }]
            },
            'entry' : [{
                'reference' : 'Procedure/Procedure-min'
            }]
        },
        {
            'title' : '住院治療經過',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '8648-8',
                    'display' : 'Hospital course Narrative'
                }]
            },
            'entry' : [{
                'reference' : 'Procedure/ProcedureHospitalCourse-min'
            },
            {
                'reference' : 'Location/Location-min'
            }]
        },
        {
            'title' : '合併症與併發症',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '55109-3',
                    'display' : 'Complications Document'
                }]
            },
            'entry' : [{
                'reference' : 'Condition/ConditionComorbiditiesandComplications-min'
            }]
        },
        {
            'title' : '出院指示',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '8653-8',
                    'display' : 'Hospital Discharge instructions'
                }]
            },
            'entry' : [{
                'reference' : 'CarePlan/CarePlan-min'
            },
            {
                'reference' : 'MedicationRequest/MedicationRequest-min'
            }]
        }]
    }
