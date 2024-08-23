from fixtures.condition_m_2024 import *


def test_create(condition_m_class, profile_urls, clinical_status_coding, category_coding, code_coding, subject, asserter, expected_payload):
    expected = expected_payload

    condition_m_class.set_profile_urls(profile_urls)

    condition_m_class.set_clinical_status_coding(clinical_status_coding)

    condition_m_class.set_category_coding(category_coding)

    condition_m_class.set_code_coding(code_coding)

    condition_m_class.set_subject(subject)

    condition_m_class.set_asserter(asserter)

    payload_template = condition_m_class.create()

    assert condition_m_class.payload_template == expected
