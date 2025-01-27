from fixtures.observation_imri_lab_min import *


def test_create(observation_class, profile_urls, status, category_coding, category_text, code_text, subject, effective_datetime, value_string, expected_payload):
    expected = expected_payload

    observation_class.set_profile_urls(profile_urls)

    observation_class.set_status(status)

    observation_class.set_category_coding(category_coding)
    observation_class.set_category_text(category_text)

    observation_class.set_code_text(code_text)

    observation_class.set_subject(subject)

    observation_class.set_effective_datetime(effective_datetime)

    observation_class.set_value_string(value_string)

    observation_class.create()

    assert observation_class.payload_template == expected
