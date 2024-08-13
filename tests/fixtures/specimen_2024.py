import pytest
from fhir_data_generator import TWCoreSpecimen as Specimen


@pytest.fixture
def specimen_class():
    return Specimen(specimen_id='spe-blood-example')

@pytest.fixture
def profile_urls():
    return [
        'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Specimen-twcore',
    ]

@pytest.fixture
def identifier():
    return [{
        'system': 'https://www.tph.mohw.gov.tw',
        'value': '1a3f5b7d-9e2c-4f6a-8c1e-0b2d4e6f8a9c'
    }]

@pytest.fixture
def accession_identifier():
    return {
        'value': '20150816-0001'
    }

@pytest.fixture
def status():
    return 'available'

@pytest.fixture
def type_coding():
    return [{
        'system': 'http://snomed.info/sct',
        'code': '119297000',
        'display': 'Blood specimen'
    }]

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/pat-example',
        'display': '陳加玲'
    }

@pytest.fixture
def received_time():
    return '2023-11-04T09:00:00.000Z'

@pytest.fixture
def collection_collector():
    return {
        'reference': 'Practitioner/pra-dr-example',
        'display': '王依昇'
    }

@pytest.fixture
def collection_collected_date_time():
    return '2023-11-03T08:30:08.000Z'

@pytest.fixture
def collection_quantity():
    return {
        'value': 4,
        'unit': 'mL',
        'system': 'http://unitsofmeasure.org',
        'code': 'mL'
    }

@pytest.fixture
def collection_method_coding():
    return [{
        'system': 'http://snomed.info/sct',
        'code': '278450005',
        'display': 'Finger-prick sampling'
    }]

@pytest.fixture
def collection_method_text():
    return 'Phlebotomy'

@pytest.fixture
def collection_body_site_coding():
    return [{
        'system': 'http://snomed.info/sct',
        'code': '53130003',
        'display': 'Venous Blood'
    }]

@pytest.fixture
def collection_body_site_text():
    return 'Venous Blood'

@pytest.fixture
def collection_fasting_status_codeable_concept_coding():
    return [{
        'system': 'http://terminology.hl7.org/CodeSystem/v2-0916',
        'code': 'F',
        'display': 'Patient was fasting prior to the procedure.'
    }]

@pytest.fixture
def processing():
    return [
        {
            'description': 'Centrifugation',
            'procedure': {
                'coding': [{
                    'system': 'http://snomed.info/sct',
                    'code': '85457002',
                    'display': 'Centrifugation'
                }],
                'text': 'Centrifugation'
            },
            'timeDateTime': '2023-11-04T09:30:00.000Z'
        },
        {
            'description': 'Freezing',
            'procedure': {
                'coding': [{
                    'system': 'http://snomed.info/sct',
                    'code': '48103003',
                    'display': 'Freezing'
                }],
                'text': 'Freezing'
            },
            'timeDateTime': '2023-11-04T10:00:00.000Z'
        }
    ]

@pytest.fixture
def container():
    return [{
        'description': '真空採血管',
        'type': {
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '701516009',
                'display': 'Evacuated blood collection tube transport container'
            }]
        },
        'capacity': {
            'value': 6,
            'unit': 'mL',
            'system': 'http://unitsofmeasure.org',
            'code': 'mL'
        },
        'specimenQuantity': {
            'value': 4,
            'unit': 'mL',
            'system': 'http://unitsofmeasure.org',
            'code': 'mL'
        }
    }]

@pytest.fixture
def note():
    return [{
        'text': '此血液檢體來自患者的最後一次例行檢查'
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Specimen',
        'id': 'spe-blood-example',
        'meta': {
            'profile': [
                'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Specimen-twcore'
            ]
        },
        'identifier': [{
            'system': 'https://www.tph.mohw.gov.tw',
            'value': '1a3f5b7d-9e2c-4f6a-8c1e-0b2d4e6f8a9c'
        }],
        'accessionIdentifier': {
            'value': '20150816-0001'
        },
        'status': 'available',
        'type': {
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '119297000',
                'display': 'Blood specimen'
            }]
        },
        'subject': {
            'reference': 'Patient/pat-example',
            'display': '陳加玲'
        },
        'receivedTime': '2023-11-04T09:00:00.000Z',
        'collection': {
            'collector': {
                'reference': 'Practitioner/pra-dr-example',
                'display': '王依昇'
            },
            'collectedDateTime': '2023-11-03T08:30:08.000Z',
            'quantity': {
                'value': 4,
                'unit': 'mL',
                'system': 'http://unitsofmeasure.org',
                'code': 'mL'
            },
            'method': {
                'coding': [{
                    'system': 'http://snomed.info/sct',
                    'code': '278450005',
                    'display': 'Finger-prick sampling'
                }],
                'text': 'Phlebotomy'
            },
            'bodySite': {
                'coding': [{
                    'system': 'http://snomed.info/sct',
                    'code': '53130003',
                    'display': 'Venous Blood'
                }],
                'text': 'Venous Blood'
            },
            'fastingStatusCodeableConcept': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0916',
                    'code': 'F',
                    'display': 'Patient was fasting prior to the procedure.'
                }]
            }
        },
        'processing': [
            {
                'description': 'Centrifugation',
                'procedure': {
                    'coding': [{
                        'system': 'http://snomed.info/sct',
                        'code': '85457002',
                        'display': 'Centrifugation'
                    }],
                    'text': 'Centrifugation'
                },
                'timeDateTime': '2023-11-04T09:30:00.000Z'
            },
            {
                'description': 'Freezing',
                'procedure': {
                    'coding': [{
                        'system': 'http://snomed.info/sct',
                        'code': '48103003',
                        'display': 'Freezing'
                    }],
                    'text': 'Freezing'
                },
                'timeDateTime': '2023-11-04T10:00:00.000Z'
            }
        ],
        'container': [{
            'description': '真空採血管',
            'type': {
                'coding': [{
                    'system': 'http://snomed.info/sct',
                    'code': '701516009',
                    'display': 'Evacuated blood collection tube transport container'
                }]
            },
            'capacity': {
                'value': 6,
                'unit': 'mL',
                'system': 'http://unitsofmeasure.org',
                'code': 'mL'
            },
            'specimenQuantity': {
                'value': 4,
                'unit': 'mL',
                'system': 'http://unitsofmeasure.org',
                'code': 'mL'
            }
        }],
        'note': [{
            'text': '此血液檢體來自患者的最後一次例行檢查'
        }]
    }
