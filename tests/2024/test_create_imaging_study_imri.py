from fixtures.imaging_study_2024 import *


def test_create(imaging_study_class, profile_urls, identifier, status, subject, encounter, started, number_of_series, number_of_instances, procedure_reference, procedure_code_coding, series_uid, series_modality, series_body_site, series_performer_actor, series_instance_uid, series_instance_sop_class, expected_payload):
    expected = expected_payload

    imaging_study_class.set_profile_urls(profile_urls)

    imaging_study_class.set_identifier(identifier)

    imaging_study_class.set_status(status)

    imaging_study_class.set_subject(subject)

    imaging_study_class.set_encounter(encounter)

    imaging_study_class.set_started(started)

    imaging_study_class.set_number_of_series(number_of_series)

    imaging_study_class.set_number_of_instances(number_of_instances)

    imaging_study_class.set_procedure_reference(procedure_reference)

    imaging_study_class.set_procedure_code_coding(procedure_code_coding)

    imaging_study_class.set_series_uid(series_uid)
    imaging_study_class.set_series_modality(series_modality)
    imaging_study_class.set_series_body_site(series_body_site)
    imaging_study_class.set_series_performer_actor(series_performer_actor)
    imaging_study_class.set_series_instance_uid(series_instance_uid)
    imaging_study_class.set_series_instance_sop_class(series_instance_sop_class)

    imaging_study_class.create()

    assert imaging_study_class.payload_template == expected
