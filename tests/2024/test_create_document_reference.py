from fixtures.document_reference_2024 import *


def test_create(document_reference_class, profile_urls, status, type_coding, type_text, subject, date, author, custodian, content, expected_payload):
    expected = expected_payload

    document_reference_class.set_profile_urls(profile_urls)

    document_reference_class.set_status(status)

    document_reference_class.set_type_coding(type_coding)
    document_reference_class.set_type_text(type_text)

    document_reference_class.set_subject(subject)

    document_reference_class.set_date(date)

    document_reference_class.set_author(author)

    document_reference_class.set_custodian(custodian)

    document_reference_class.set_content(content)

    document_reference_class.create()

    assert document_reference_class.payload_template == expected
