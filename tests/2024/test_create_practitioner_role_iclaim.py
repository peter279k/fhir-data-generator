from fixtures.practitioner_role_iclaim_2024 import *


def test_create(practitioner_role_class, profile_urls, practitioner, code, expected_payload):
    expected = expected_payload

    practitioner_role_class.set_profile_urls(profile_urls)

    practitioner_role_class.set_practitioner(practitioner)

    practitioner_role_class.set_code(code)

    practitioner_role_class.create()

    assert practitioner_role_class.payload_template == expected
