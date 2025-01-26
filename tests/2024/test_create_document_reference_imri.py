from fixtures.document_reference_imri_2024 import *


def test_create(document_reference_class, profile_urls, status, subject, content, expected_payload):
    expected = expected_payload

    document_reference_class.set_profile_urls(profile_urls)

    document_reference_class.set_status(status)

    document_reference_class.set_subject(subject)

    document_reference_class.set_content(content)

    document_reference_class.create()

    assert document_reference_class.payload_template == expected
