from fixtures.observation_ltc_glucose import *


def test_create_glucose_blood(observation_class, profile_urls, status, category_coding, code_codings, subject, effective_datetime, performer, value_quantity, expected_payload):
    expected = expected_payload
    expected['code']['coding'] = code_codings[0]

    observation_class.set_profile_urls(profile_urls)

    observation_class.set_status(status)

    observation_class.set_category_coding(category_coding)

    observation_class.set_code_coding(code_codings[0])

    observation_class.set_subject(subject)

    observation_class.set_effective_datetime(effective_datetime)

    observation_class.set_performer(performer)

    observation_class.set_value_quantity(value_quantity)

    observation_class.create()

    assert observation_class.payload_template == expected

def test_create_glucose_blood_post_meal(observation_class, profile_urls, status, category_coding, code_codings, subject, effective_datetime, performer, value_quantity, expected_payload):
    expected = expected_payload
    expected['code']['coding'] = code_codings[1]

    observation_class.set_profile_urls(profile_urls)

    observation_class.set_status(status)

    observation_class.set_category_coding(category_coding)

    observation_class.set_code_coding(code_codings[1])

    observation_class.set_subject(subject)

    observation_class.set_effective_datetime(effective_datetime)

    observation_class.set_performer(performer)

    observation_class.set_value_quantity(value_quantity)

    observation_class.create()

    assert observation_class.payload_template == expected

def test_create_glucose_blood_pre_meal(observation_class, profile_urls, status, category_coding, code_codings, subject, effective_datetime, performer, value_quantity, expected_payload):
    expected = expected_payload
    expected['code']['coding'] = code_codings[2]

    observation_class.set_profile_urls(profile_urls)

    observation_class.set_status(status)

    observation_class.set_category_coding(category_coding)

    observation_class.set_code_coding(code_codings[2])

    observation_class.set_subject(subject)

    observation_class.set_effective_datetime(effective_datetime)

    observation_class.set_performer(performer)

    observation_class.set_value_quantity(value_quantity)

    observation_class.create()

    assert observation_class.payload_template == expected
