from fixtures.diagnostic_report_iclaim_2024 import *


def test_create(diagnostic_report_class, profile_urls, status, code_coding, subject, result, expected_payload):
    expected = expected_payload

    diagnostic_report_class.set_profile_urls(profile_urls)

    diagnostic_report_class.set_status(status)

    diagnostic_report_class.set_code_coding(code_coding)

    diagnostic_report_class.set_subject(subject)

    diagnostic_report_class.set_result(result)

    diagnostic_report_class.create()

    assert diagnostic_report_class.payload_template == expected
