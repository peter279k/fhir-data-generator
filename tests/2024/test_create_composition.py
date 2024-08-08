from fixtures.composition_2024 import *


def test_create(composition_class, profile_urls, status, type_coding, category, subject, date, author, title, confidentiality, attester, custodian, event_code, event_period, section_entry, expected_payload):
    expected = expected_payload

    composition_class.set_profile_urls(profile_urls)

    composition_class.set_status(status)

    composition_class.set_type_coding(type_coding)

    composition_class.set_category(category)

    composition_class.set_subject(subject)

    composition_class.set_date(date)

    composition_class.set_author(author)

    composition_class.set_title(title)

    composition_class.set_confidentiality(confidentiality)

    composition_class.set_attester(attester)

    composition_class.set_custodian(custodian)

    composition_class.set_event_code(event_code)
    composition_class.set_event_period(event_period)

    composition_class.set_section_entry(section_entry)

    composition_class.create()

    assert composition_class.payload_template == expected
