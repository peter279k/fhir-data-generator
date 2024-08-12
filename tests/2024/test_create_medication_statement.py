from fixtures.medication_statement_2024 import *


def test_create(medication_statement_class, profile_urls, status, category_coding, category_text, medication_codeable_concept_coding, medication_codeable_concept_text, subject, effective_date_time, date_asserted, reason_code_coding, reason_code_text, note, dosage_text, dosage_timing_repeat, dosage_route_coding, dosage_route_text, expected_payload):
    expected = expected_payload

    medication_statement_class.set_profile_urls(profile_urls)

    medication_statement_class.set_status(status)

    medication_statement_class.set_category_coding(category_coding)
    medication_statement_class.set_category_text(category_text)

    medication_statement_class.set_medication_codeable_concept_coding(medication_codeable_concept_coding)
    medication_statement_class.set_medication_codeable_concept_text(medication_codeable_concept_text)

    medication_statement_class.set_subject(subject)

    medication_statement_class.set_effective_date_time(effective_date_time)

    medication_statement_class.set_date_asserted(date_asserted)

    medication_statement_class.set_reason_code_coding(reason_code_coding)
    medication_statement_class.set_reason_code_text(reason_code_text)

    medication_statement_class.set_note(note)

    medication_statement_class.set_dosage_text(dosage_text)
    medication_statement_class.set_dosage_timing_repeat(dosage_timing_repeat)
    medication_statement_class.set_dosage_route_coding(dosage_route_coding)
    medication_statement_class.set_dosage_route_text(dosage_route_text)

    medication_statement_class.create()

    assert medication_statement_class.payload_template == expected
