from fixtures.patient_imri_2024 import *


def test_create(patient_class, profile_urls, identifiers, name_use, name_text, gender, birth_date, expected_payload):
    expected = expected_payload

    patient_class.set_profile_urls(profile_urls)

    patient_class.set_identifiers(identifiers)

    patient_class.set_name_use(name_use)
    patient_class.set_name_text(name_text)

    patient_class.set_gender(gender)

    patient_class.set_birth_date(birth_date)

    patient_class.create()

    assert patient_class.payload_template == expected
