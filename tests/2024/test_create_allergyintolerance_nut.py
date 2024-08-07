from fixtures.allergyintolerance_nut_2024 import *


def test_create(allergy_intolerance_class, profile_urls, clinical_status_coding, clinical_status_text, verification_status_coding, verification_status_text, category, criticality, code_coding, code_text, patient, onset_datetime, recorded_date, recorder, asserter, last_occurrence, note, reaction_description, reaction_severity, reaction_exposure_route_text, reaction_note, expected_payload):
    expected = expected_payload

    allergy_intolerance_class.set_profile_urls(profile_urls)

    allergy_intolerance_class.set_clinical_status_coding(clinical_status_coding)
    allergy_intolerance_class.set_clinical_status_text(clinical_status_text)

    allergy_intolerance_class.set_verification_status_coding(verification_status_coding)
    allergy_intolerance_class.set_verification_status_text(verification_status_text)

    allergy_intolerance_class.set_category(category)

    allergy_intolerance_class.set_criticality(criticality)

    allergy_intolerance_class.set_code_coding(code_coding)
    allergy_intolerance_class.set_code_text(code_text)

    allergy_intolerance_class.set_patient(patient)
    allergy_intolerance_class.set_onset_datetime(onset_datetime)
    allergy_intolerance_class.set_recorded_date(recorded_date)
    allergy_intolerance_class.set_recorder(recorder)
    allergy_intolerance_class.set_asserter(asserter)
    allergy_intolerance_class.set_last_occurrence(last_occurrence)
    allergy_intolerance_class.set_note(note)

    allergy_intolerance_class.set_reaction_description(reaction_description)
    allergy_intolerance_class.set_reaction_severity(reaction_severity)
    allergy_intolerance_class.set_reaction_exposure_route_text(reaction_exposure_route_text)
    allergy_intolerance_class.set_reaction_note(reaction_note)

    allergy_intolerance_class.create()

    assert allergy_intolerance_class.payload_template == expected
