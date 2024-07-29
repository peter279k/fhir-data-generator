from fixtures.condition_e_2024 import *


def test_create(condition_e_class, profile_urls, clinical_status_coding, category_coding, code_coding, code_text, subject, asserter, expected_payload):
    expected = expected_payload

    condition_e_class.set_profile_urls(profile_urls)

    condition_e_class.set_clinical_status_coding(clinical_status_coding)

    condition_e_class.set_category_coding(category_coding)

    condition_e_class.set_code_coding(code_coding)
    condition_e_class.set_code_text(code_text)

    condition_e_class.set_subject(subject)

    condition_e_class.set_asserter(asserter)

    condition_e_class.create()

    assert condition_e_class.payload_template == expected
