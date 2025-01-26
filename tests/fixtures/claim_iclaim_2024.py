import pytest
from fhir_data_generator import Claim


@pytest.fixture
def claim_class():
    return Claim('Claim-C1')

@pytest.fixture
def profile_urls():
    return [
        'https://claim.cgh.org.tw/iclaim/StructureDefinition/claim-iclaim'
    ]

@pytest.fixture
def identifier():
    return [{
        'system' : 'https://www.cgh.org.tw',
        'value' : 'A0001'
    }]

@pytest.fixture
def status():
    return 'active'

@pytest.fixture
def type_coding():
    return [{
        'system' : 'http://terminology.hl7.org/CodeSystem/claim-type',
        'code' : 'institutional'
    }]

@pytest.fixture
def patient():
    return {
        'reference' : 'Patient/Patient-C1'
    }

@pytest.fixture
def created():
    return '2023-08-07'

@pytest.fixture
def provider():
    return {
        'reference' : 'Organization/Organization-min'
    }

@pytest.fixture
def priority_coding():
    return [{
        'system' : 'http://terminology.hl7.org/CodeSystem/processpriority',
        'code' : 'stat'
    }]

@pytest.fixture
def diagnosis():
    return [{
        'sequence' : 1,
        'diagnosisReference' : {
            'reference' : 'Condition/Condition-C1'
        }
    }]

@pytest.fixture
def insurance():
    return [{
        'sequence' : 1,
        'focal' : True,
        'coverage' : {
            'reference' : 'Coverage/Coverage-C1'
        }
    }]

@pytest.fixture
def item():
    return [{
        'sequence' : 1,
        'category' : {
            'coding' : [{
                'system' : 'http://hl7.org/fhir/invoice-priceComponentType',
                'code' : 'base'
            }]
        },
        'productOrService' : {
            'coding' : [{
                'system' : 'https://claim.cgh.org.tw/iclaim/CodeSystem/cathay-chargeitemcode-values',
                'code' : 'REGISTRATION'
            }]
        },
        'modifier' : [{
            'coding' : [{
                'system' : 'http://terminology.hl7.org/CodeSystem/coverage-selfpay',
                'code' : 'pay'
            }]
        }],
        'servicedDate' : '2023-08-07',
        'net' : {
            'value' : 150
        }
    },
    {
        'sequence' : 2,
        'productOrService' : {
            'coding' : [{
                'system' : 'https://claim.cgh.org.tw/iclaim/CodeSystem/cathay-chargeitemcode-values',
                'code' : 'REGISTRATION'
            }]
        },
        'modifier' : [{
            'coding' : [{
                'system' : 'http://terminology.hl7.org/CodeSystem/v3-ActCode',
                'code' : 'PUBLICPOL'
            }]
        }],
        'servicedDate' : '2023-08-07',
        'net' : {
            'value' : 580
        }
    }]

@pytest.fixture
def total():
    return {
        'value' : 150
    }

@pytest.fixture
def expected_payload():
    return {
        'resourceType' : 'Claim',
        'id' : 'Claim-C1',
        'meta' : {
            'profile' : ['https://claim.cgh.org.tw/iclaim/StructureDefinition/claim-iclaim']
        },
        'identifier' : [{
            'system' : 'https://www.cgh.org.tw',
            'value' : 'A0001'
        }],
        'status' : 'active',
        'type' : {
            'coding' : [{
                'system' : 'http://terminology.hl7.org/CodeSystem/claim-type',
                'code' : 'institutional'
            }]
        },
        'use' : 'claim',
        'patient' : {
            'reference' : 'Patient/Patient-C1'
        },
        'created' : '2023-08-07',
        'provider' : {
            'reference' : 'Organization/Organization-min'
        },
        'priority' : {
            'coding' : [{
                'system' : 'http://terminology.hl7.org/CodeSystem/processpriority',
                'code' : 'stat'
            }]
        },
        'diagnosis' : [{
            'sequence' : 1,
            'diagnosisReference' : {
                'reference' : 'Condition/Condition-C1'
            }
        }],
        'insurance' : [{
            'sequence' : 1,
            'focal' : True,
            'coverage' : {
                'reference' : 'Coverage/Coverage-C1'
            }
        }],
        'item' : [{
            'sequence' : 1,
            'category' : {
                'coding' : [{
                    'system' : 'http://hl7.org/fhir/invoice-priceComponentType',
                    'code' : 'base'
                }]
            },
            'productOrService' : {
                'coding' : [{
                    'system' : 'https://claim.cgh.org.tw/iclaim/CodeSystem/cathay-chargeitemcode-values',
                    'code' : 'REGISTRATION'
                }]
            },
            'modifier' : [{
                'coding' : [{
                    'system' : 'http://terminology.hl7.org/CodeSystem/coverage-selfpay',
                    'code' : 'pay'
                }]
            }],
            'servicedDate' : '2023-08-07',
            'net' : {
                'value' : 150
            }
        },
        {
            'sequence' : 2,
            'productOrService' : {
                'coding' : [{
                    'system' : 'https://claim.cgh.org.tw/iclaim/CodeSystem/cathay-chargeitemcode-values',
                    'code' : 'REGISTRATION'
                }]
            },
            'modifier' : [{
                'coding' : [{
                    'system' : 'http://terminology.hl7.org/CodeSystem/v3-ActCode',
                    'code' : 'PUBLICPOL'
                }]
            }],
            'servicedDate' : '2023-08-07',
            'net' : {
                'value' : 580
            }
        }],
        'total' : {
            'value' : 150
        }
    }
