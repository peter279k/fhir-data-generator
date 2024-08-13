from fixtures.procedure_2024 import *


def test_create(procedure_class, profile_urls, status, code_coding, code_text, subject, performed_date_time, asserter, performer, body_site_coding, expected_payload):
    expected = expected_payload

    procedure_class.set_profile_urls(profile_urls)

    procedure_class.set_status(status)

    procedure_class.set_code_coding(code_coding)
    procedure_class.set_code_text(code_text)

    procedure_class.set_subject(subject)

    procedure_class.set_performed_date_time(performed_date_time)

    procedure_class.set_asserter(asserter)

    procedure_class.set_performer(performer)

    procedure_class.set_body_site_coding(body_site_coding)

    procedure_class.create()

    assert procedure_class.payload_template == expected
