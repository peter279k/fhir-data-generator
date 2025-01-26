from fixtures.composition_iclaim_2024 import *


def test_create(composition_class, profile_urls, identifier, status, type_coding, subject, date, author, title, section_title, section_code, section_entry, expected_payload):
    expected = expected_payload

    composition_class.set_profile_urls(profile_urls)

    composition_class.set_identifier(identifier)

    composition_class.set_status(status)

    composition_class.set_type_coding(type_coding)

    composition_class.set_subject(subject)

    composition_class.set_date(date)

    composition_class.set_author(author)

    composition_class.set_title(title)

    composition_class.set_section_title(section_title)
    composition_class.set_section_code(section_code)
    composition_class.set_section_entry(section_entry)

    composition_class.create()

    assert composition_class.payload_template == expected
