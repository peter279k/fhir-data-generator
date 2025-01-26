from fixtures.practitioner_imri_2024 import *


def test_create(practitioner_class, profile_urls, name, expected_payload):
    expected = expected_payload

    practitioner_class.set_profile_urls(profile_urls)

    practitioner_class.set_name(name)

    practitioner_class.create()

    assert practitioner_class.payload_template == expected
