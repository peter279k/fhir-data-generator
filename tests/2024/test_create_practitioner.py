from fixtures.practitioner_2024 import *


def test_create(practitioner_class, profile_urls, identifiers, active, name_text, expected_payload):
    expected = expected_payload

    practitioner_class.set_profile_urls(profile_urls)

    practitioner_class.set_identifiers(identifiers)

    practitioner_class.set_active(active)

    practitioner_class.set_name_text(name_text)

    practitioner_class.create()

    assert practitioner_class.payload_template == expected
