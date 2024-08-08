from fixtures.encounter_2024 import *


def test_create(encounter_class, profile_urls, identifier, status, fixture_class, type_coding, service_type_coding, service_type_text, subject, participant_type_coding, participant_period, participant_individual, period, reason_code_coding, hospitalization_discharge_disposition_coding, location, expected_payload):
    expected = expected_payload

    encounter_class.set_profile_urls(profile_urls)

    encounter_class.set_identifier(identifier)

    encounter_class.set_status(status)

    encounter_class.set_class(fixture_class)

    encounter_class.set_type_coding(type_coding)

    encounter_class.set_service_type_coding(service_type_coding)
    encounter_class.set_service_type_text(service_type_text)

    encounter_class.set_subject(subject)

    encounter_class.set_participant_type_coding(participant_type_coding)
    encounter_class.set_participant_period(participant_period)
    encounter_class.set_participant_individual(participant_individual)

    encounter_class.set_period(period)

    encounter_class.set_reason_code_coding(reason_code_coding)

    encounter_class.set_hospitalization_discharge_disposition_coding(hospitalization_discharge_disposition_coding)

    encounter_class.set_location(location)

    encounter_class.create()

    assert encounter_class.payload_template == expected
