from fixtures.location_imri_2024 import *


def test_create(location_class, profile_urls, identifier, name, expected_payload):
    expected = expected_payload

    location_class.set_profile_urls(profile_urls)

    location_class.set_identifier(identifier)

    location_class.set_name(name)

    location_class.create()

    assert location_class.payload_template == expected
