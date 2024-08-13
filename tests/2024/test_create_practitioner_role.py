from fixtures.practitioner_role_2024 import *


def test_create(practitioner_role_class, profile_urls, identifiers, active, period, practitioner, specialty_coding, code, location, telecom, available_time, not_available, availability_exceptions, expected_payload):
    expected = expected_payload

    practitioner_role_class.set_profile_urls(profile_urls)

    practitioner_role_class.set_identifiers(identifiers)

    practitioner_role_class.set_active(active)

    practitioner_role_class.set_period(period)

    practitioner_role_class.set_practitioner(practitioner)

    practitioner_role_class.set_specialty_coding(specialty_coding)

    practitioner_role_class.set_code(code)

    practitioner_role_class.set_location(location)

    practitioner_role_class.set_telecom(telecom)

    practitioner_role_class.set_available_time(available_time)

    practitioner_role_class.set_not_available(not_available)

    practitioner_role_class.set_availability_exceptions(availability_exceptions)

    practitioner_role_class.create()

    assert practitioner_role_class.payload_template == expected
