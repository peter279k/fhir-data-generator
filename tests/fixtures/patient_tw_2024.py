import pytest
from fhir_data_generator import PatientTW


@pytest.fixture
def patient_class():
    return PatientTW('patient-tw-example')

@pytest.fixture
def profile_urls():
    return [
        'https://hapi.fhir.tw/fhir/StructureDefinition/TWCorePatient',
    ]


@pytest.fixture
def extension_url():
    return 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/person-age'

@pytest.fixture
def extension_value_age():
    return {
        'value': 32,
        'system': 'http://unitsofmeasure.org',
        'code': 'a',
    }

@pytest.fixture
def extension_extension_coding():
    return [{
        'system': 'urn:iso:std:iso:3166',
        'code': 'TW',
    }]

@pytest.fixture
def extension_extension_url():
    return 'http://hl7.org/fhir/StructureDefinition/patient-nationality'

@pytest.fixture
def identifiers():
    return [{
        'use': 'official',
        'type': {
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                'code': 'NNxxx',
                '_code': {
                    'extension': [{
                        'extension': [
                            {
                                'url': 'suffix',
                                'valueString': 'TWN'
                            },
                            {
                                'url': 'valueSet',
                                'valueCanonical': 'http://hl7.org/fhir/ValueSet/iso3166-1-3'
                            }
                        ],
                        'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/identifier-suffix'
                    }]
                }
            }]
        },
        'system': 'http://www.moi.gov.tw',
        'value': 'A123456789'
    }]

@pytest.fixture
def active():
    return True

@pytest.fixture
def name_use():
    return 'official'

@pytest.fixture
def name_text():
    return '連小妹'

@pytest.fixture
def gender():
    return 'female'

@pytest.fixture
def birth_date():
    return '1990-01-01'

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Patient',
        'id': 'patient-tw-example',
        'meta': {
            'profile': ['https://hapi.fhir.tw/fhir/StructureDefinition/TWCorePatient']
        },
        'extension': [
            {
                'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/person-age',
                'valueAge': {
                    'value': 32,
                    'system': 'http://unitsofmeasure.org',
                    'code': 'a'
                }
            },
            {
                'extension': [{
                    'url': 'code',
                    'valueCodeableConcept': {
                        'coding': [{
                            'system': 'urn:iso:std:iso:3166',
                            'code': 'TW'
                        }]
                    }
                }],
                'url': 'http://hl7.org/fhir/StructureDefinition/patient-nationality'
            }
        ],
        'identifier': [{
            'use': 'official',
            'type': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code': 'NNxxx',
                    '_code': {
                        'extension': [{
                            'extension': [
                                {
                                    'url': 'suffix',
                                    'valueString': 'TWN'
                                },
                                {
                                    'url': 'valueSet',
                                    'valueCanonical': 'http://hl7.org/fhir/ValueSet/iso3166-1-3'
                                }
                            ],
                            'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/identifier-suffix'
                        }]
                    }
                }]
            },
            'system': 'http://www.moi.gov.tw',
            'value': 'A123456789'
        }],
        'active': True,
        'name': [{
            'use': 'official',
            'text': '連小妹'
        }],
        'gender': 'female',
        'birthDate': '1990-01-01'
    }
