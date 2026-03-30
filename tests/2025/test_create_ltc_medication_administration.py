from fixtures.ltc_medication_administration import *


def test_create(medication_administration_class, profile_urls, status, medication_codeable_concept_coding, medication_codeable_concept_text, subject, effective_date_time, performer, note, dosage, expected_payload):
    expected = expected_payload

    medication_administration_class.set_profile_urls(profile_urls)

    medication_administration_class.set_status(status)

    medication_administration_class.set_medication_codeable_concept_coding(medication_codeable_concept_coding)
    medication_administration_class.set_medication_codeable_concept_text(medication_codeable_concept_text)

    medication_administration_class.set_subject(subject)

    medication_administration_class.set_effective_date_time(effective_date_time)

    medication_administration_class.set_performer(performer)

    medication_administration_class.set_note(note)

    medication_administration_class.set_dosage(dosage)

    medication_administration_class.create()

    assert medication_administration_class.payload_template == expected
