import json
import uuid
from fhir_data_generator import Patient


patient = Patient(str(uuid.uuid4()))
patient.set_profile_url('https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition-TWPatient.json')

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
    'value': '262344368',
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
managing_organization = 'Organization/MITW.ForIdentifier'
name = {
    'use': 'official',
    'text': '李小明',
    'family': '李',
    'given': ['小明'],
}
gender = 'male'
birth_date = '2023-12-23'
addresses = [
    {
        'use': 'home',
        'text': '105台北市松山區民生東路四段133號',
    },
    {
        'country': 'TW',
    },
]
scenario = 1
telecom = {
    'use': 'home',
    'system': 'phone',
    'value': '0905285349',
}

patient.set_identifier(identifier1)
patient.set_identifier(identifier2)
patient.set_active(True)
patient.set_managing_organization(managing_organization)
patient.set_name(name)
patient.set_gender(gender)
patient.set_birth_date(birth_date)
patient.set_address(addresses[0])
patient.set_address(addresses[1])
patient.set_telecom(telecom)

# Retrieving the Patient resource dict
patient_json_dict = patient.create(1)
print(patient_json_dict)

# Retrieve the Patient resource JSON string
print(json.dumps(patient_json_dict))
