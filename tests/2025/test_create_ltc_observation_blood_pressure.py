from fixtures.observation_ltc_pasport_blood_pressure import *


def test_create(observation_class, profile_urls, status, category_coding, code_coding, subject, effective_datetime, performer, interpretation, note, body_site_coding, method_coding, component, expected_payload):
    expected = expected_payload

    observation_class.set_profile_urls(profile_urls)

    observation_class.set_status(status)

    observation_class.set_category_coding(category_coding)

    observation_class.set_code_coding(code_coding)

    observation_class.set_subject(subject)

    observation_class.set_effective_datetime(effective_datetime)

    observation_class.set_performer(performer)

    observation_class.set_interpretation(interpretation)

    observation_class.set_note(note)

    observation_class.set_body_site_coding(body_site_coding)

    observation_class.set_method_coding(method_coding)

    observation_class.set_component(component)

    observation_class.create()

    assert observation_class.payload_template == expected
