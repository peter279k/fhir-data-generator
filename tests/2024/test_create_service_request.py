from fixtures.service_request_2024 import *


def test_create(service_request_class, profile_urls, identifiers, status, intent, category_coding, code_coding, subject, authored_on, requester, expected_payload):
    expected = expected_payload

    service_request_class.set_profile_urls(profile_urls)

    service_request_class.set_identifiers(identifiers)

    service_request_class.set_status(status)

    service_request_class.set_intent(intent)

    service_request_class.set_category_coding(category_coding)

    service_request_class.set_code_coding(code_coding)

    service_request_class.set_subject(subject)

    service_request_class.set_authored_on(authored_on)

    service_request_class.set_requester(requester)

    service_request_class.create()

    assert service_request_class.payload_template == expected
