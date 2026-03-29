from fixtures.practitioner_nurse_ltc import *


def test_create(practitioner_class, profile_urls, identifiers, active, name, telecom, gender, qualification, expected_payload):
    expected = expected_payload

    practitioner_class.set_profile_urls(profile_urls)

    practitioner_class.set_identifiers(identifiers)

    practitioner_class.set_active(active)

    practitioner_class.set_name(name)

    practitioner_class.set_telecom(telecom)

    practitioner_class.set_gender(gender)

    practitioner_class.set_qualification(qualification)

    practitioner_class.create()

    assert practitioner_class.payload_template == expected
