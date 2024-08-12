from fixtures.medication_2024 import *


def test_create(medication_class, profile_urls, code_coding, code_text, form_coding, form_text, expected_payload):
    expected = expected_payload

    medication_class.set_profile_urls(profile_urls)

    medication_class.set_code_coding(code_coding)
    medication_class.set_code_text(code_text)

    medication_class.set_form_coding(form_coding)
    medication_class.set_form_text(form_text)

    medication_class.create()

    assert medication_class.payload_template == expected
