from fixtures.condition_2024 import *


def test_create(condition_class, profile_urls, clinical_status_coding, verification_status_coding, category_coding, severity_coding, code_coding, code_text, subject, onset_datetime, abatement_datetime, asserter, expected_payload):
    expected = expected_payload

    condition_class.set_profile_urls(profile_urls)

    condition_class.set_clinical_status_coding(clinical_status_coding)

    condition_class.set_verification_status_coding(verification_status_coding)

    condition_class.set_category_coding(category_coding)

    condition_class.set_severity_coding(severity_coding)

    condition_class.set_code_coding(code_coding)
    condition_class.set_code_text(code_text)

    condition_class.set_subject(subject)

    condition_class.set_onset_datetime(onset_datetime)

    condition_class.set_abatement_datetime(abatement_datetime)

    condition_class.set_asserter(asserter)

    condition_class.create()

    assert condition_class.payload_template == expected
