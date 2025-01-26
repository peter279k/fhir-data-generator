from fixtures.condition_iclaim_2024 import *


def test_create(condition_class, profile_urls, identifier, clinical_status_coding, category_coding, code_coding, subject, encounter, recorded_date, recorder, asserter, stage, note, expected_payload):
    expected = expected_payload

    condition_class.set_profile_urls(profile_urls)

    condition_class.set_identifier(identifier)

    condition_class.set_clinical_status_coding(clinical_status_coding)

    condition_class.set_category_coding(category_coding)

    condition_class.set_code_coding(code_coding)

    condition_class.set_subject(subject)

    condition_class.set_encounter(encounter)

    condition_class.set_recorded_date(recorded_date)

    condition_class.set_recorder(recorder)

    condition_class.set_asserter(asserter)

    condition_class.set_stage(stage)

    condition_class.set_note(note)

    condition_class.create()

    assert condition_class.payload_template == expected
