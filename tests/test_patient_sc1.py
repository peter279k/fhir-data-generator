from fixtures.patient_info import *


def test_set_meta_profile(patient_class, profile_urls):
    expected = profile_urls
    expected_len = 1

    patient_class.set_profile_url(profile_urls[0])

    assert patient_class.profile_urls == expected
    assert len(patient_class.profile_urls) == expected_len

def test_remove_meta_profile(patient_class, profile_urls):
    expected = []
    expected_len = 0
    profile_url = profile_urls[0]

    patient_class.set_profile_url(profile_url)
    patient_class.remove_profile_url(profile_url)

    assert patient_class.profile_urls == expected
    assert len(patient_class.profile_urls) == expected_len

def test_set_identifier(patient_class, identifiers):
    expected = identifiers
    expected_len = 2

    patient_class.set_identifier(identifiers[0])
    patient_class.set_identifier(identifiers[1])

    assert patient_class.identifiers == expected
    assert len(patient_class.identifiers) == expected_len

def test_remove_identifier(patient_class, identifiers):
    expected = [identifiers[0]]
    expected_len = 1

    patient_class.set_identifier(identifiers[0])
    patient_class.set_identifier(identifiers[1])

    patient_class.remove_identifier(identifiers[1])


    assert patient_class.identifiers == expected
    assert len(patient_class.identifiers) == expected_len

def test_set_active(patient_class, inactive):
    expected = inactive

    patient_class.set_active(expected)

    assert patient_class.active == expected

def test_set_managing_organization(patient_class, managing_organization):
    expected = managing_organization

    patient_class.set_managing_organization(expected)

    assert patient_class.managing_organization_reference == expected

def test_set_name(patient_class, names):
    expected = names
    expected_len = 1

    patient_class.set_name(names[0])

    assert patient_class.names == expected
    assert len(patient_class.names) == expected_len

def test_remove_name(patient_class, names):
    expected = []
    expected_len = 0

    patient_class.set_name(names[0])
    patient_class.remove_name(names[0])

    assert patient_class.names == expected
    assert len(patient_class.names) == expected_len

def test_set_gender(patient_class, gender):
    expected = gender

    patient_class.set_gender(expected)

    assert patient_class.gender == expected

def test_set_birth_date(patient_class, birth_date):
    expected = birth_date

    patient_class.set_birth_date(expected)

    assert patient_class.birth_date == expected

def test_set_address(patient_class, addresses):
    expected = addresses
    expected_len = 2

    patient_class.set_address(addresses[0])
    patient_class.set_address(addresses[1])

    assert patient_class.addresses == expected
    assert len(patient_class.addresses) == expected_len

def test_remove_address(patient_class, addresses):
    expected = [addresses[1]]
    expected_len = 1

    patient_class.set_address(addresses[0])
    patient_class.set_address(addresses[1])

    patient_class.remove_address(addresses[0])

    assert patient_class.addresses == expected
    assert len(patient_class.addresses) == expected_len

def test_set_telecom(patient_class, telecoms):
    expected = telecoms
    expected_len = 1

    patient_class.set_telecom(telecoms[0])

    assert patient_class.telecoms == expected
    assert len(patient_class.telecoms) == expected_len

def test_remove_telecom(patient_class, telecoms):
    expected = []
    expected_len = 0

    patient_class.set_telecom(telecoms[0])

    patient_class.remove_telecom(telecoms[0])

    assert patient_class.telecoms == expected
    assert len(patient_class.telecoms) == expected_len

def test_create(patient_class, profile_urls, identifiers, inactive, managing_organization, names, gender, birth_date, addresses, telecoms, patient_sc1_payload):
    expected = patient_sc1_payload
    scenario = 1

    patient_class.set_profile_url(profile_urls[0])

    patient_class.set_identifier(identifiers[0])
    patient_class.set_identifier(identifiers[1])

    patient_class.set_active(inactive)

    patient_class.set_managing_organization(managing_organization)

    patient_class.set_name(names[0])

    patient_class.set_gender(gender)

    patient_class.set_birth_date(birth_date)

    patient_class.set_address(addresses[0])
    patient_class.set_address(addresses[1])

    patient_class.set_telecom(telecoms[0])

    patient_class.create(scenario)

    assert patient_class.payload_template == expected
