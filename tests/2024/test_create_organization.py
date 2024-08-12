from fixtures.organization_2024 import *


def test_create(organization_class, profile_urls, identifiers, type_coding, name, telecom, expected_payload):
    expected = expected_payload

    organization_class.set_profile_urls(profile_urls)

    organization_class.set_identifiers(identifiers)

    organization_class.set_type_coding(type_coding)

    organization_class.set_name(name)

    organization_class.set_telecom(telecom)

    organization_class.create()

    assert organization_class.payload_template == expected
