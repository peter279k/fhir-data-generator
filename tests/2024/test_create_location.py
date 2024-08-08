from fixtures.location_2024 import *


def test_create(location_class, profile_urls, status, name, description, mode, type_coding, telecom, address, position, managing_organization, hours_of_operation_days_of_week, hours_of_operation_all_day, expected_payload):
    expected = expected_payload

    location_class.set_profile_urls(profile_urls)

    location_class.set_status(status)

    location_class.set_name(name)

    location_class.set_description(description)

    location_class.set_mode(mode)

    location_class.set_type_coding(type_coding)

    location_class.set_telecom(telecom)

    location_class.set_address(address)

    location_class.set_position(position)

    location_class.set_managing_organization(managing_organization)

    location_class.set_hours_of_operation_days_of_week(hours_of_operation_days_of_week)
    location_class.set_hours_of_operation_all_day(hours_of_operation_all_day)

    location_class.create()

    assert location_class.payload_template == expected
