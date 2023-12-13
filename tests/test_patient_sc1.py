from fixtures.patient_sc1_info import *


def test_create(patient_class, profile_urls, identifiers, inactive, managing_organization, names, gender, birth_date, addresses, telecoms, patient_sc1_payload):
    expected = patient_sc1_payload
    scenario = 1

    patient_class.set_profile_url(profile_urls[0])

    patient_class.set_identifier(identifiers[0])
    patient_class.set_identifier(identifiers[1])

    patient_class.set_active(inactive)

    patient_class.set_managing_organization(managing_organization)

    patient_class.set_name(names[0])

    patient_class.set_gender(gender)

    patient_class.set_birth_date(birth_date)

    patient_class.set_address(addresses[0])
    patient_class.set_address(addresses[1])

    patient_class.set_telecom(telecoms[0])

    patient_class.create(scenario)

    assert patient_class.payload_template == expected
