from fixtures.ltc_location import *


def test_create(location_class, profile_urls, status, name, description, mode, types, address, position, expected_payload):
    expected = expected_payload

    location_class.set_profile_urls(profile_urls)

    location_class.set_status(status)

    location_class.set_name(name)

    location_class.set_description(description)

    location_class.set_mode(mode)

    location_class.set_type(types)

    location_class.set_address(address)

    location_class.set_position(position)

    location_class.create()

    assert location_class.payload_template == expected
