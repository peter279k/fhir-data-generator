from fixtures.organization_ltc import *


def test_create(organization_class, profile_urls, identifiers, active, types, name, telecom, address, contact, expected_payload):
    expected = expected_payload

    organization_class.set_profile_urls(profile_urls)

    organization_class.set_identifiers(identifiers)

    organization_class.set_active(active)

    organization_class.set_type(types)

    organization_class.set_name(name)

    organization_class.set_telecom(telecom)

    organization_class.set_address(address)

    organization_class.set_contact(contact)

    organization_class.create()

    assert organization_class.payload_template == expected
