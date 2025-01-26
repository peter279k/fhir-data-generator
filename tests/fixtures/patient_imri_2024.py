import pytest
from fhir_data_generator import PatientIclaimC1 as Patient


@pytest.fixture
def patient_class():
    return Patient('Patient-min')

@pytest.fixture
def profile_urls():
    return [
        'https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/patient-imri',
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
    return [{
        'use' : 'official',
        'type' : {
            'coding' : [{
                'system' : 'http://terminology.hl7.org/CodeSystem/v2-0203',
                'code' : 'NNxxx',
                '_code' : {
                    'extension' : [{
                        'extension' : [{
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
        'value' : 'A123456789'
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
        'value' : '70892114'
    }]

@pytest.fixture
def name_use():
    return 'usual'

@pytest.fixture
def name_text():
    return '安格斯'

@pytest.fixture
def gender():
    return 'male'

@pytest.fixture
def birth_date():
    return '2000-02-02'

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Patient',
        'id' : 'Patient-min',
        'meta' : {
            'profile' : ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/patient-imri']
        },
        'identifier' : [{
            'use' : 'official',
            'type' : {
                'coding' : [{
                    'system' : 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code' : 'NNxxx',
                    '_code' : {
                        'extension' : [{
                            'extension' : [{
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
            'value' : 'A123456789'
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
            'value' : '70892114'
        }],
        'name' : [{
            'use' : 'usual',
            'text' : '安格斯'
        }],
        'gender' : 'male',
        'birthDate' : '2000-02-02'
    }
