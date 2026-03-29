from fixtures.patient_ltc_tw import *


def test_create(patient_class, profile_urls, identifiers, active, names, telecom, gender, birth_date, address, contact, managing_organization, expected_payload):
    expected = expected_payload

    patient_class.set_profile_urls(profile_urls)

    patient_class.set_active(active)

    patient_class.set_names(names)

    patient_class.set_identifiers(identifiers)

    patient_class.set_telecom(telecom)

    patient_class.set_gender(gender)

    patient_class.set_birth_date(birth_date)

    patient_class.set_address(address)

    patient_class.set_contact(contact)

    patient_class.set_managing_organization(managing_organization)

    patient_class.create()

    assert patient_class.payload_template == expected
