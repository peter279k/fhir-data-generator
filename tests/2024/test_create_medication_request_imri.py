from fixtures.medication_request_imri_2024 import *


def test_create(medication_request_class, profile_urls, status, intent, medication_codeable_concept, subject, encounter, requester, performer, based_on, expected_payload):
    expected = expected_payload

    medication_request_class.set_profile_urls(profile_urls)

    medication_request_class.set_status(status)

    medication_request_class.set_intent(intent)

    medication_request_class.set_medication_codeable_concept(medication_codeable_concept)

    medication_request_class.set_subject(subject)

    medication_request_class.set_encounter(encounter)

    medication_request_class.set_requester(requester)

    medication_request_class.set_performer(performer)

    medication_request_class.set_based_on(based_on)

    medication_request_class.create()

    assert medication_request_class.payload_template == expected
