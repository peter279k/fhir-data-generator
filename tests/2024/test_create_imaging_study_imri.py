from fixtures.imaging_study_imri_2024 import *


def test_create(imaging_study_class, profile_urls, status, subject, encounter, started, interpreter, description, expected_payload):
    expected = expected_payload

    imaging_study_class.set_profile_urls(profile_urls)

    imaging_study_class.set_status(status)

    imaging_study_class.set_subject(subject)

    imaging_study_class.set_encounter(encounter)

    imaging_study_class.set_started(started)

    imaging_study_class.set_interpreter(interpreter)

    imaging_study_class.set_description(description)

    imaging_study_class.create()

    assert imaging_study_class.payload_template == expected
