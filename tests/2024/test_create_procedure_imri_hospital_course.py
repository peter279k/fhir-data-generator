from fixtures.procedure_imri_hospital_course_2024 import *


def test_create(procedure_class, profile_urls, status, code_coding, subject, encounter, note, expected_payload):
    expected = expected_payload

    procedure_class.set_profile_urls(profile_urls)

    procedure_class.set_status(status)

    procedure_class.set_code_coding(code_coding)

    procedure_class.set_subject(subject)

    procedure_class.set_encounter(encounter)

    procedure_class.set_note(note)

    procedure_class.create()

    assert procedure_class.payload_template == expected
