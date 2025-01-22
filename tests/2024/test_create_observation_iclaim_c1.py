from fixtures.observation_iclaim_c1 import *


def test_create(observation_class, profile_urls, status, identifier, category_coding, code_coding, subject, effective_datetime, issued, performer, value_quantity, note, interpretation, body_site_coding, reference_range, expected_payload):
    expected = expected_payload

    observation_class.set_profile_urls(profile_urls)

    observation_class.set_status(status)

    observation_class.set_identifier(identifier)

    observation_class.set_category_coding(category_coding)

    observation_class.set_code_coding(code_coding)

    observation_class.set_subject(subject)

    observation_class.set_effective_datetime(effective_datetime)

    observation_class.set_issued(issued)

    observation_class.set_performer(performer)

    observation_class.set_value_quantity(value_quantity)

    observation_class.set_note(note)

    observation_class.set_interpretation(interpretation)

    observation_class.set_body_site_coding(body_site_coding)

    observation_class.set_reference_range(reference_range)

    observation_class.create()

    assert observation_class.payload_template == expected
