from fixtures.encounter_imri_2024 import *


def test_create(encounter_class, profile_urls, status, fixture_class, service_type_coding, subject, participant_individual, period, hospitalization, expected_payload):
    expected = expected_payload

    encounter_class.set_profile_urls(profile_urls)

    encounter_class.set_status(status)

    encounter_class.set_class(fixture_class)

    encounter_class.set_service_type_coding(service_type_coding)

    encounter_class.set_subject(subject)

    encounter_class.set_participant_individual(participant_individual)

    encounter_class.set_period(period)

    encounter_class.set_hospitalization(hospitalization)

    encounter_class.create()

    assert encounter_class.payload_template == expected
