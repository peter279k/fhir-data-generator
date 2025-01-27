from fixtures.observation_imri_blood_type import *


def test_create(observation_class, profile_urls, status, code_coding, code_text, subject, effective_datetime, value_codeable_concept, expected_payload):
    expected = expected_payload

    observation_class.set_profile_urls(profile_urls)

    observation_class.set_status(status)

    observation_class.set_code_coding(code_coding)
    observation_class.set_code_text(code_text)

    observation_class.set_subject(subject)

    observation_class.set_effective_datetime(effective_datetime)

    observation_class.set_value_codeable_concept(value_codeable_concept)

    observation_class.create()

    assert observation_class.payload_template == expected
