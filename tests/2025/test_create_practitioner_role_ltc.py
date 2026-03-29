from fixtures.practitioner_role_ltc import *


def test_create(practitioner_role_class, profile_urls, active, practitioner, organization, code, specialty, telecom, available_time, expected_payload):
    expected = expected_payload

    practitioner_role_class.set_profile_urls(profile_urls)

    practitioner_role_class.set_active(active)

    practitioner_role_class.set_practitioner(practitioner)

    practitioner_role_class.set_organization(organization)

    practitioner_role_class.set_code(code)

    practitioner_role_class.set_specialty(specialty)

    practitioner_role_class.set_telecom(telecom)

    practitioner_role_class.set_available_time(available_time)

    practitioner_role_class.create()

    assert practitioner_role_class.payload_template == expected
