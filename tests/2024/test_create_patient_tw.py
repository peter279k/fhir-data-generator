from fixtures.patient_tw_2024 import *


def test_create(patient_class, profile_urls, extension_url, extension_value_age, extension_extension_coding, extension_extension_url, identifiers, active, name_use, name_text, gender, birth_date, expected_payload):
    expected = expected_payload

    patient_class.set_profile_urls(profile_urls)

    patient_class.set_extension_url(extension_url)
    patient_class.set_extension_value_age(extension_value_age)
    patient_class.set_extension_extension_coding(extension_extension_coding)
    patient_class.set_extension_extension_url(extension_extension_url)

    patient_class.set_identifiers(identifiers)

    patient_class.set_active(active)

    patient_class.set_name_use(name_use)
    patient_class.set_name_text(name_text)

    patient_class.set_gender(gender)

    patient_class.set_birth_date(birth_date)

    patient_class.create()

    assert patient_class.payload_template == expected
