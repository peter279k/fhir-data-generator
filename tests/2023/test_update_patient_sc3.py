from fixtures.patient_sc3_info import *


def test_create(patient_class, profile_urls, identifiers, names, active, managing_organization, contacts, gender, birth_date, addresses, telecoms, update_patient_sc3_payload):
    expected = update_patient_sc3_payload
    scenario = 3

    patient_class.set_profile_url(profile_urls[0])

    patient_class.set_identifier(identifiers[0])
    patient_class.set_identifier(identifiers[1])

    patient_class.set_name(names[0])

    patient_class.set_gender(gender)

    patient_class.set_birth_date(birth_date)

    patient_class.set_address(addresses[0])

    patient_class.set_telecom(telecoms[0])
    patient_class.set_telecom(telecoms[1])
    patient_class.set_telecom(telecoms[2])

    patient_class.set_contact(contacts[0])

    patient_class.set_patient_id('22526')

    patient_class.set_active(active)

    patient_class.set_managing_organization(managing_organization)

    patient_class.create(scenario, update=True)

    assert patient_class.payload_template == expected
