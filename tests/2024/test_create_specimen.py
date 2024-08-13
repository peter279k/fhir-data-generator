from fixtures.specimen_2024 import *


def test_create(specimen_class, profile_urls, identifier, accession_identifier, status, type_coding, subject, received_time, collection_collector, collection_collected_date_time, collection_quantity, collection_method_coding, collection_method_text, collection_body_site_coding, collection_body_site_text, collection_fasting_status_codeable_concept_coding, processing, container, note, expected_payload):
    expected = expected_payload

    specimen_class.set_profile_urls(profile_urls)

    specimen_class.set_identifier(identifier)

    specimen_class.set_accession_identifier(accession_identifier)

    specimen_class.set_status(status)

    specimen_class.set_type_coding(type_coding)

    specimen_class.set_subject(subject)

    specimen_class.set_received_time(received_time)

    specimen_class.set_collection_collector(collection_collector)
    specimen_class.set_collection_collected_date_time(collection_collected_date_time)
    specimen_class.set_collection_quantity(collection_quantity)
    specimen_class.set_collection_method_coding(collection_method_coding)
    specimen_class.set_collection_method_text(collection_method_text)
    specimen_class.set_collection_body_site_coding(collection_body_site_coding)
    specimen_class.set_collection_body_site_text(collection_body_site_text)
    specimen_class.set_collection_fasting_status_codeable_concept_coding(collection_fasting_status_codeable_concept_coding)

    specimen_class.set_processing(processing)

    specimen_class.set_container(container)

    specimen_class.set_note(note)

    specimen_class.create()

    assert specimen_class.payload_template == expected
