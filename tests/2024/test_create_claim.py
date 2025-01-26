from fixtures.claim_iclaim_2024 import *


def test_create(claim_class, profile_urls, identifier, status, type_coding, patient, created, provider, priority_coding, diagnosis, insurance, item, total, expected_payload):
    expected = expected_payload

    claim_class.set_profile_urls(profile_urls)

    claim_class.set_identifier(identifier)

    claim_class.set_status(status)

    claim_class.set_type_coding(type_coding)

    claim_class.set_patient(patient)

    claim_class.set_created(created)

    claim_class.set_provider(provider)

    claim_class.set_priority_coding(priority_coding)

    claim_class.set_diagnosis(diagnosis)

    claim_class.set_insurance(insurance)

    claim_class.set_item(item)

    claim_class.set_total(total)

    claim_class.create()

    assert claim_class.payload_template == expected
