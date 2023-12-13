from fixtures.patient_sc2_info import *


def test_set_contact(patient_class, contacts):
    expected = contacts
    expected_len = 1

    patient_class.set_contact(contacts[0])

    assert patient_class.contacts == expected
    assert len(patient_class.contacts) == expected_len

def test_remove_contact(patient_class, contacts):
    expected = []
    expected_len = 0

    patient_class.set_contact(contacts[0])

    patient_class.remove_contact(contacts[0])

    assert patient_class.contacts == expected
    assert len(patient_class.contacts) == expected_len

def test_create(patient_class, profile_urls, identifiers, inactive, managing_organization, names, gender, birth_date, addresses, telecoms, contacts, patient_sc2_payload):
    expected = patient_sc2_payload
    scenario = 2

    patient_class.set_profile_url(profile_urls[0])

    patient_class.set_identifier(identifiers[0])
    patient_class.set_identifier(identifiers[1])

    patient_class.set_active(inactive)

    patient_class.set_managing_organization(managing_organization)

    patient_class.set_name(names[0])

    patient_class.set_gender(gender)

    patient_class.set_birth_date(birth_date)

    patient_class.set_address(addresses[0])

    patient_class.set_telecom(telecoms[0])
    patient_class.set_telecom(telecoms[1])
    patient_class.set_telecom(telecoms[2])

    patient_class.set_contact(contacts[0])

    patient_class.create(scenario)

    assert patient_class.payload_template == expected
