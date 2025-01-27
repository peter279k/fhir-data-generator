from fixtures.condition_imri_present_illness import *


def test_create(condition_class, profile_urls, clinical_status_coding, category_coding, code_coding, subject, encounter, expected_payload):
    expected = expected_payload

    condition_class.set_profile_urls(profile_urls)

    condition_class.set_clinical_status_coding(clinical_status_coding)

    condition_class.set_category_coding(category_coding)

    condition_class.set_code_coding(code_coding)

    condition_class.set_subject(subject)

    condition_class.set_encounter(encounter)

    condition_class.create()

    assert condition_class.payload_template == expected
