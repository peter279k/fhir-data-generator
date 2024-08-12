from fixtures.medication_request_2024 import *


def test_create(medication_request_class, profile_urls, identifier, status, status_reason_coding, intent, category_coding, medication_reference, subject, encounter, authored_on, requester, reason_reference, dosage_instruction_text, dosage_instruction_timing_coding, dosage_instruction_timing_text, dosage_instruction_route_coding, dosage_instruction_dose_rate_type_coding, dispense_request_validity_period_start, dispense_request_validity_period_end, expected_payload):
    expected = expected_payload

    medication_request_class.set_profile_urls(profile_urls)

    medication_request_class.set_identifier(identifier)

    medication_request_class.set_status(status)

    medication_request_class.set_status_reason_coding(status_reason_coding)

    medication_request_class.set_intent(intent)

    medication_request_class.set_category_coding(category_coding)

    medication_request_class.set_medication_reference(medication_reference)

    medication_request_class.set_subject(subject)

    medication_request_class.set_encounter(encounter)

    medication_request_class.set_authored_on(authored_on)

    medication_request_class.set_requester(requester)

    medication_request_class.set_reason_reference(reason_reference)

    medication_request_class.set_dosage_instruction_text(dosage_instruction_text)

    medication_request_class.set_dosage_instruction_timing_coding(dosage_instruction_timing_coding)
    medication_request_class.set_dosage_instruction_timing_text(dosage_instruction_timing_text)
    medication_request_class.set_dosage_instruction_route_coding(dosage_instruction_route_coding)
    medication_request_class.set_dosage_instruction_dose_rate_type_coding(dosage_instruction_dose_rate_type_coding)

    medication_request_class.set_dispense_request_validity_period_start(dispense_request_validity_period_start)
    medication_request_class.set_dispense_request_validity_period_end(dispense_request_validity_period_end)

    medication_request_class.create()

    assert medication_request_class.payload_template == expected
