import pytest
from fhir_data_generator import PatientIclaimC1 as Patient


@pytest.fixture
def patient_class():
    return Patient('Patient-C1')

@pytest.fixture
def profile_urls():
    return [
        'https://claim.cgh.org.tw/iclaim/StructureDefinition/patient-iclaim',
    ]

@pytest.fixture
def extension():
    return [{
        'url' : 'https://claim.cgh.org.tw/iclaim/StructureDefinition/cathay-occupation',
        'valueCodeableConcept' : {
        'coding' : [
          {
            'system' : 'https://claim.cgh.org.tw/iclaim/CodeSystem/lia-roc-occupation-values',
            'code' : '00010010'
          }
        ]
      }
    }]

@pytest.fixture
def identifiers():
    return [
        {
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
            'value': 'C251401029'
        },
        {
            'use': 'official',
            'type': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code': 'MR'
                }]
            },
            'system' : 'https://www.cgh.org.tw',
            'value': 'ADCM9487'
        }
    ]

@pytest.fixture
def name_use():
    return 'usual'

@pytest.fixture
def name_text():
    return '郝美麗'

@pytest.fixture
def gender():
    return 'female'

@pytest.fixture
def birth_date():
    return '1990-04-22'

@pytest.fixture
def address_extension():
    return [
        {
            'url' : 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-number',
            'valueString' : '365號'
        }
    ]

@pytest.fixture
def address():
    return   [{
      'extension' : [
        {
          'url' : 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-number',
          'valueString' : '365號'
        }
      ],
      'text' : '台北市北投區明德路365號',
      'line' : [
        '明德路'
      ],
      'city' : '北投區',
      'district' : '台北市',
      'country' : 'TW'
    }]

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'Patient',
        'id': 'Patient-C1',
        'meta' : {
            'profile' : ['https://claim.cgh.org.tw/iclaim/StructureDefinition/patient-iclaim']
        },
        'extension' : [{
            'url' : 'https://claim.cgh.org.tw/iclaim/StructureDefinition/cathay-occupation',
            'valueCodeableConcept' : {
                'coding' : [{
                    'system' : 'https://claim.cgh.org.tw/iclaim/CodeSystem/lia-roc-occupation-values',
                    'code' : '00010010'
                }]
            }
        }],
        'identifier' : [{
            'use' : 'official',
            'type' : {
                'coding' : [{
                    'system' : 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code' : 'NNxxx',
                    '_code' : {
                        'extension' : [{
                            'extension' : [
                                {
                                    'url' : 'suffix',
                                    'valueString' : 'TWN'
                                },
                                {
                                    'url' : 'valueSet',
                                    'valueCanonical' : 'http://hl7.org/fhir/ValueSet/iso3166-1-3'
                                }
                            ],
                            'url' : 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/identifier-suffix'
                        }]
                    }
                }]
            },
            'system' : 'http://www.moi.gov.tw',
            'value' : 'C251401029'
        },
        {
            'use' : 'official',
            'type' : {
                'coding' : [{
                    'system' : 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code' : 'MR'
                }]
            },
            'system' : 'https://www.cgh.org.tw',
            'value' : 'ADCM9487'
        }],
        'name' : [{
            'use' : 'usual',
            'text' : '郝美麗'
        }],
        'gender' : 'female',
        'birthDate' : '1990-04-22',
        'address' : [{
            'extension' : [{
                'url' : 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-number',
                'valueString' : '365號'
            }],
            'text' : '台北市北投區明德路365號',
            'line' : ['明德路'],
            'city' : '北投區',
            'district' : '台北市',
            'country' : 'TW'
        }]
    }
