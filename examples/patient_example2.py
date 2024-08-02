import json
import uuid
from fhir_data_generator import Patient


patient = Patient(str(uuid.uuid4()))

patient.set_profile_url('https://fhir.server/path/to/profile/path')

identifier1 = {
    'use': 'official',
    'system': 'http://www.boca.gov.tw',
    'type': {
        'coding': [
            {
                'system': 'http://www.boca.gov.tw',
                'code': 'PPN',
                'display': 'Passport number',
            },
        ],
    },
    'value': 'E262344368'[2:],
}
identifier2 = {
    'use': 'official',
    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
    'type': {
        'coding': [
            {
                'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                'code': 'MR',
                'display': 'Medical record number',
            },
        ]
    },
    'value': '123456789',
}

patient.set_identifier(identifier1)
patient.set_identifier(identifier2)

patient.set_active(True)

managing_organization = 'Organization/MITW.ForIdentifier'
patient.set_managing_organization(managing_organization)

names = [
    {
        'use': 'official',
        'family': 'Li',
        'given': [
            'Peter'
        ],
        'text': 'Peter Li',
    },
]

patient.set_name(names[0])

gender = 'male'
patient.set_gender(gender)

birth_date = '2023-12-23'
patient.set_birth_date(birth_date)

addresses = [
    {
        'use': 'home',
        'text': '105台北市松山區民生東路四段133號',
    },
    {
        'country': 'TW',
    },
]

patient.set_address(addresses[0])
patient.set_address(addresses[1])

telecom = {
    'use': 'home',
    'system': 'phone',
    'value': '0905285349',
}
patient.set_telecom(telecom)

communications = [
    {
        'language': {
            'coding': [
                {
                    'system': 'http://terminology.hl7.org/CodeSystem/v3-ietf3066',
                    'code': 'en-US',
                },
            ],
            'text': 'English (US)',
        },
    },
]

patient.set_communication(communications[0])

scenario = 2

# Retrieving the Patient resource dict
patient_json_dict = patient.create(scenario)
print(patient_json_dict)

# Retrieve the Patient resource JSON string
print(json.dumps(patient_json_dict))
