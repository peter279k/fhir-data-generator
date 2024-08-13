from fixtures.patient_2024 import *


def test_create(patient_class, profile_urls, extension_url, extension_value_age, extension_extension_coding, extension_extension_url, identifiers, active, name_use, name_text, name_family, name_given, telecom, gender, birth_date, address_extension, address_text, address_line, address_city, address_district, address_postal_code_extension, marital_status_coding, photo, contact, contact_name, contact_telecom, communication_language_coding, managing_organization, expected_payload):
    expected = expected_payload

    patient_class.set_profile_urls(profile_urls)

    patient_class.set_extension_url(extension_url)
    patient_class.set_extension_value_age(extension_value_age)
    patient_class.set_extension_extension_coding(extension_extension_coding)
    patient_class.set_extension_extension_url(extension_extension_url)

    patient_class.set_identifiers(identifiers)

    patient_class.set_active(active)

    patient_class.set_name_use(name_use)
    patient_class.set_name_text(name_text)
    patient_class.set_name_family(name_family)
    patient_class.set_name_given(name_given)

    patient_class.set_telecom(telecom)

    patient_class.set_gender(gender)

    patient_class.set_birth_date(birth_date)

    patient_class.set_address_extension(address_extension)
    patient_class.set_address_text(address_text)
    patient_class.set_address_line(address_line)
    patient_class.set_address_city(address_city)
    patient_class.set_address_district(address_district)
    patient_class.set_address_postal_code_extension(address_postal_code_extension)

    patient_class.set_marital_status_coding(marital_status_coding)

    patient_class.set_photo(photo)

    patient_class.set_contact(contact)
    patient_class.set_contact_name(contact_name)
    patient_class.set_contact_telecom(contact_telecom)

    patient_class.set_communication_language_coding(communication_language_coding)

    patient_class.set_managing_organization(managing_organization)

    patient_class.create()

    assert patient_class.payload_template == expected
