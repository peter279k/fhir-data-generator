from fixtures.tw_core_practitioner_2024 import *


def test_create(practitioner_class, profile_urls, identifiers, active, name, telecom, photo, birth_date, gender, address, qualification, expected_payload):
    expected = expected_payload

    practitioner_class.set_profile_urls(profile_urls)

    practitioner_class.set_identifiers(identifiers)

    practitioner_class.set_active(active)

    practitioner_class.set_name(name)

    practitioner_class.set_telecom(telecom)

    practitioner_class.set_photo(photo)

    practitioner_class.set_gender(gender)

    practitioner_class.set_birth_date(birth_date)

    practitioner_class.set_address(address)

    practitioner_class.set_qualification(qualification)

    practitioner_class.create()

    assert practitioner_class.payload_template == expected
