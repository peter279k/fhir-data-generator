from fixtures.diagnostic_report_2024 import *


def test_create(diagnostic_report_class, profile_urls, status, category_coding, category_text, code_coding, code_text, subject, effective_datetime, issued, performer, result, expected_payload):
    expected = expected_payload

    diagnostic_report_class.set_profile_urls(profile_urls)

    diagnostic_report_class.set_status(status)

    diagnostic_report_class.set_category_coding(category_coding)
    diagnostic_report_class.set_category_text(category_text)

    diagnostic_report_class.set_code_coding(code_coding)
    diagnostic_report_class.set_code_text(code_text)

    diagnostic_report_class.set_subject(subject)

    diagnostic_report_class.set_effective_datetime(effective_datetime)

    diagnostic_report_class.set_issued(issued)

    diagnostic_report_class.set_performer(performer)

    diagnostic_report_class.set_result(result)

    diagnostic_report_class.create()

    assert diagnostic_report_class.payload_template == expected
