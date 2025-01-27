from fixtures.procedure_imri_pro_2024 import *


def test_create(procedure_class, profile_urls, status, category, code_coding, subject, performed_date_time, performer, reason_reference, body_site_coding, report, note, used_code, expected_payload):
    expected = expected_payload

    procedure_class.set_profile_urls(profile_urls)

    procedure_class.set_status(status)

    procedure_class.set_category(category)

    procedure_class.set_code_coding(code_coding)

    procedure_class.set_subject(subject)

    procedure_class.set_performed_date_time(performed_date_time)

    procedure_class.set_performer(performer)

    procedure_class.set_reason_reference(reason_reference)

    procedure_class.set_body_site_coding(body_site_coding)

    procedure_class.set_report(report)

    procedure_class.set_note(note)

    procedure_class.set_used_code(used_code)

    procedure_class.create()

    assert procedure_class.payload_template == expected
