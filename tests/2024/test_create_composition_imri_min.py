from fixtures.composition_imri_2024 import *


def test_create(composition_class, profile_urls, status, type_coding, subject, date, author, title, encounter, section, expected_payload):
    expected = expected_payload

    composition_class.set_profile_urls(profile_urls)

    composition_class.set_status(status)

    composition_class.set_type_coding(type_coding)

    composition_class.set_subject(subject)

    composition_class.set_encounter(encounter)

    composition_class.set_date(date)

    composition_class.set_author(author)

    composition_class.set_title(title)

    composition_class.set_section(section)

    composition_class.create()

    assert composition_class.payload_template == expected
