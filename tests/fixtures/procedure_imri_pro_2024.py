import pytest
from fhir_data_generator import TWCoreProcedure as Procedure


@pytest.fixture
def procedure_class():
    return Procedure(procedure_id='Procedure-pro')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/procedureoperation-imri'
    ]

@pytest.fixture
def status():
    return 'completed'

@pytest.fixture
def category():
    return {
        'coding' : [{
            'system' : 'http://loinc.org',
            'code' : '8724-7',
            'display' : 'Surgical operation note description Narrative'
        }]
    }

@pytest.fixture
def code_coding():
    return [{
        'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medical-service-payment-tw',
        'code' : '75607C',
        'display' : '鼠蹊疝氣修補術-無腸切除'
    }]

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/Patient-min'
    }

@pytest.fixture
def performed_date_time():
    return '2023-10-20'

@pytest.fixture
def performer():
    return [{
        'actor' : {
            'reference' : 'PractitionerRole/PractitionerRole-min',
            'display' : '劉伊詩'
        }
    }]

@pytest.fixture
def reason_reference():
    return [{
        'reference' : 'Condition/Condition-preope'
    }]

@pytest.fixture
def body_site_coding():
    return [{
        'system' : 'http://snomed.info/sct',
        'code' : '4312008',
        'display' : 'Anterior midline of abdomen'
    }]

@pytest.fixture
def report():
    return [{
        'reference' : 'DocumentReference/DocumentReference-min'
    }]

@pytest.fixture
def note():
    return [
        {
            'text' : '1. indication: (gall bladder polyp) 2. gall bladder: normal; gallbladder wall thickening: (-), _1_mm 3.gall stone (no), sludge (no), spiliage (no), cystic duct impaction(no) 4. cystic duct closed with (hemolock) 5. cystic artery closed with (hemolock) 6. intraoperative bile spillage(yes), stone spillage (no) 7. drainage left (no) 8. wound closure: (primary closure) 9.previous abdominal surgery: (no) 10.port site (3 ports in single incision) 11. way of cholecystectomy (Calot\'s triangle first) 12.estimated blood loss:_1_ ml 13.Other intra-operation operation findings :'
        },
        {
            'text' : '1. Under general anesthesia, patient was put in supine position 2. Sterlized and draped the abdomen as usual 3. 2.5cm incision wound created at umbilicus, glove port was set, 3 ports were inserted via glove port 4. approach Calot\'s trangle, dissect the serosa 5. dissect cystic duct and cystic artery, present critical view of safty 6. closed cystic artery with hemolock 7. dissect gallbladder from gallbladder fossa 8. closed cystic duct with hemolock 9. After hemostasis, retract specimen with endo-bag, close the wound in layers'
        }
    ]

@pytest.fixture
def used_code():
    return [{
        'coding' : [{
            'system' : 'http://snomed.info/sct',
            'code' : '256641009',
            'display' : 'Ribbon gauze'
        }]
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Procedure',
        'id' : 'Procedure-pro',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/procedureoperation-imri']
        },
        'status' : 'completed',
        'category' : {
            'coding' : [{
                'system' : 'http://loinc.org',
                'code' : '8724-7',
                'display' : 'Surgical operation note description Narrative'
            }]
        },
        'code' : {
            'coding' : [{
                'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medical-service-payment-tw',
                'code' : '75607C',
                'display' : '鼠蹊疝氣修補術-無腸切除'
            }]
        },
        'subject' : {
            'reference' : 'Patient/Patient-min'
        },
        'performedDateTime' : '2023-10-20',
        'performer' : [{
            'actor' : {
                'reference' : 'PractitionerRole/PractitionerRole-min',
                'display' : '劉伊詩'
            }
        }],
        'reasonReference' : [{
            'reference' : 'Condition/Condition-preope'
        }],
        'bodySite' : [{
            'coding' : [{
                'system' : 'http://snomed.info/sct',
                'code' : '4312008',
                'display' : 'Anterior midline of abdomen'
            }]
        }],
        'report' : [{
            'reference' : 'DocumentReference/DocumentReference-min'
        }],
        'note' : [{
            'text' : '1. indication: (gall bladder polyp) 2. gall bladder: normal; gallbladder wall thickening: (-), _1_mm 3.gall stone (no), sludge (no), spiliage (no), cystic duct impaction(no) 4. cystic duct closed with (hemolock) 5. cystic artery closed with (hemolock) 6. intraoperative bile spillage(yes), stone spillage (no) 7. drainage left (no) 8. wound closure: (primary closure) 9.previous abdominal surgery: (no) 10.port site (3 ports in single incision) 11. way of cholecystectomy (Calot\'s triangle first) 12.estimated blood loss:_1_ ml 13.Other intra-operation operation findings :'
        },
        {
            'text' : '1. Under general anesthesia, patient was put in supine position 2. Sterlized and draped the abdomen as usual 3. 2.5cm incision wound created at umbilicus, glove port was set, 3 ports were inserted via glove port 4. approach Calot\'s trangle, dissect the serosa 5. dissect cystic duct and cystic artery, present critical view of safty 6. closed cystic artery with hemolock 7. dissect gallbladder from gallbladder fossa 8. closed cystic duct with hemolock 9. After hemostasis, retract specimen with endo-bag, close the wound in layers'
        }],
        'usedCode' : [{
            'coding' : [{
                'system' : 'http://snomed.info/sct',
                'code' : '256641009',
                'display' : 'Ribbon gauze'
            }]
        }]
    }
