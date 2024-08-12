from fixtures.medication_dispense_2024 import *


def test_create(medication_dispense_class, profile_urls, status, category_coding, medication_reference, subject, context, performer_actor, type_coding, quantity, days_supply, when_prepared, when_handed_over, dosage_instruction, substitution_was_substituted, substitution_type_coding, substitution_reason_coding, expected_payload):
    expected = expected_payload

    medication_dispense_class.set_profile_urls(profile_urls)

    medication_dispense_class.set_status(status)

    medication_dispense_class.set_category_coding(category_coding)

    medication_dispense_class.set_medication_reference(medication_reference)

    medication_dispense_class.set_subject(subject)

    medication_dispense_class.set_context(context)

    medication_dispense_class.set_performer_actor(performer_actor)

    medication_dispense_class.set_type_coding(type_coding)

    medication_dispense_class.set_quantity(quantity)

    medication_dispense_class.set_days_supply(days_supply)

    medication_dispense_class.set_when_prepared(when_prepared)

    medication_dispense_class.set_when_handed_over(when_handed_over)

    medication_dispense_class.set_dosage_instruction(dosage_instruction)

    medication_dispense_class.set_substitution_was_substituted(substitution_was_substituted)
    medication_dispense_class.set_substitution_type_coding(substitution_type_coding)
    medication_dispense_class.set_substitution_reason_coding(substitution_reason_coding)

    medication_dispense_class.create()

    assert medication_dispense_class.payload_template == expected
