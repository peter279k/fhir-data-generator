import requests
from fixtures.patient_sc3_info import *


def test_create(patient_class, profile_urls, identifiers, active, managing_organization, gender, birth_date, addresses, contacts, patient_sc3_payload):
    expected = patient_sc3_payload
    scenario = 3

    patient_class.set_profile_url(profile_urls[0])

    patient_class.set_identifier(identifiers[0])
    patient_class.set_identifier(identifiers[1])

    patient_class.set_gender(gender)

    patient_class.set_birth_date(birth_date)

    patient_class.set_contact(contacts[0])

    patient_class.set_address(addresses[0])
    patient_class.set_address(addresses[1])

    patient_class.set_active(active)

    patient_class.set_managing_organization(managing_organization)

    patient_class.create(scenario)

    assert patient_class.payload_template == expected

def test_create_on_fhir_server(patient_class, patient_sc3_payload):
    headers = {
        'Accept': 'application/fhir+json',
        'Content-Type': 'application/fhir+json',
    }
    patient_sc3_payload['id'] = patient_class.patient_id
    response = requests.post('https://hapi.fhir.tw/fhir/Patient', json=patient_sc3_payload, headers=headers)
    with open('sc3_response.text', 'w') as f:
        f.write(response.text)
