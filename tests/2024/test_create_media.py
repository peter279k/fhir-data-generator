from fixtures.media_2024 import *


def test_create(media_class, profile_urls, status, type_coding, view_coding, view_text, subject, created_datetime, issued, operator, reason_code_coding, body_site_coding, device_name, height, width, content, note, expected_payload):
    expected = expected_payload

    media_class.set_profile_urls(profile_urls)

    media_class.set_status(status)

    media_class.set_type_coding(type_coding)

    media_class.set_view_coding(view_coding)
    media_class.set_view_text(view_text)

    media_class.set_created_datetime(created_datetime)

    media_class.set_issued(issued)

    media_class.set_operator(operator)

    media_class.set_reason_code_coding(reason_code_coding)

    media_class.set_body_site_coding(body_site_coding)

    media_class.set_device_name(device_name)

    media_class.set_subject(subject)

    media_class.set_height(height)

    media_class.set_width(width)

    media_class.set_content(content)

    media_class.set_note(note)

    media_class.create()

    assert media_class.payload_template == expected
