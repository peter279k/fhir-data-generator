from fixtures.procedure_ltc import *


def test_create_assisting_with_eating_and_drinking(procedure_class, profile_urls, status, code_codings, code_texts, subject, performer, performed_date_time, note, expected_payload):
    expected = expected_payload
    expected['code']['coding'] = code_codings[0]
    expected['code']['text'] = code_texts[0]

    procedure_class.set_profile_urls(profile_urls)

    procedure_class.set_status(status)

    procedure_class.set_code_coding(code_codings[0])
    procedure_class.set_code_text(code_texts[0])

    procedure_class.set_subject(subject)

    procedure_class.set_performer(performer)

    procedure_class.set_performed_date_time(performed_date_time)

    procedure_class.set_note(note)

    procedure_class.create()

    assert procedure_class.payload_template == expected

def test_create_bathing_patient(procedure_class, profile_urls, status, code_codings, code_texts, subject, performer, performed_date_time, note, expected_payload):
    expected = expected_payload
    expected['code']['coding'] = code_codings[1]
    expected['code']['text'] = code_texts[1]

    procedure_class.set_profile_urls(profile_urls)

    procedure_class.set_status(status)

    procedure_class.set_code_coding(code_codings[1])
    procedure_class.set_code_text(code_texts[1])

    procedure_class.set_subject(subject)

    procedure_class.set_performer(performer)

    procedure_class.set_performed_date_time(performed_date_time)

    procedure_class.set_note(note)

    procedure_class.create()

    assert procedure_class.payload_template == expected

def test_create_assisting_with_personal_hygiene(procedure_class, profile_urls, status, code_codings, code_texts, subject, performer, performed_date_time, note, expected_payload):
    expected = expected_payload
    expected['code']['coding'] = code_codings[2]
    expected['code']['text'] = code_texts[2]

    procedure_class.set_profile_urls(profile_urls)

    procedure_class.set_status(status)

    procedure_class.set_code_coding(code_codings[2])
    procedure_class.set_code_text(code_texts[2])

    procedure_class.set_subject(subject)

    procedure_class.set_performer(performer)

    procedure_class.set_performed_date_time(performed_date_time)

    procedure_class.set_note(note)

    procedure_class.create()

    assert procedure_class.payload_template == expected

def test_create_dressing_patient(procedure_class, profile_urls, status, code_codings, code_texts, subject, performer, performed_date_time, note, expected_payload):
    expected = expected_payload
    expected['code']['coding'] = code_codings[3]
    expected['code']['text'] = code_texts[3]

    procedure_class.set_profile_urls(profile_urls)

    procedure_class.set_status(status)

    procedure_class.set_code_coding(code_codings[3])
    procedure_class.set_code_text(code_texts[3])

    procedure_class.set_subject(subject)

    procedure_class.set_performer(performer)

    procedure_class.set_performed_date_time(performed_date_time)

    procedure_class.set_note(note)

    procedure_class.create()

    assert procedure_class.payload_template == expected

def test_create_assisting_with_toileting(procedure_class, profile_urls, status, code_codings, code_texts, subject, performer, performed_date_time, note, expected_payload):
    expected = expected_payload
    expected['code']['coding'] = code_codings[4]
    expected['code']['text'] = code_texts[4]

    procedure_class.set_profile_urls(profile_urls)

    procedure_class.set_status(status)

    procedure_class.set_code_coding(code_codings[4])
    procedure_class.set_code_text(code_texts[4])

    procedure_class.set_subject(subject)

    procedure_class.set_performer(performer)

    procedure_class.set_performed_date_time(performed_date_time)

    procedure_class.set_note(note)

    procedure_class.create()

    assert procedure_class.payload_template == expected

def test_create_escorting_subject_to_toilet(procedure_class, profile_urls, status, code_codings, code_texts, subject, performer, performed_date_time, note, expected_payload):
    expected = expected_payload
    expected['code']['coding'] = code_codings[5]
    expected['code']['text'] = code_texts[5]

    procedure_class.set_profile_urls(profile_urls)

    procedure_class.set_status(status)

    procedure_class.set_code_coding(code_codings[5])
    procedure_class.set_code_text(code_texts[5])

    procedure_class.set_subject(subject)

    procedure_class.set_performer(performer)

    procedure_class.set_performed_date_time(performed_date_time)

    procedure_class.set_note(note)

    procedure_class.create()

    assert procedure_class.payload_template == expected

def test_create_assistance_with_mobility(procedure_class, profile_urls, status, code_codings, code_texts, subject, performer, performed_date_time, note, expected_payload):
    expected = expected_payload
    expected['code']['coding'] = code_codings[6]
    expected['code']['text'] = code_texts[6]

    procedure_class.set_profile_urls(profile_urls)

    procedure_class.set_status(status)

    procedure_class.set_code_coding(code_codings[6])
    procedure_class.set_code_text(code_texts[6])

    procedure_class.set_subject(subject)

    procedure_class.set_performer(performer)

    procedure_class.set_performed_date_time(performed_date_time)

    procedure_class.set_note(note)

    procedure_class.create()

    assert procedure_class.payload_template == expected

def test_create_assistance_with_mobility_in_bed(procedure_class, profile_urls, status, code_codings, code_texts, subject, performer, performed_date_time, note, expected_payload):
    expected = expected_payload
    expected['code']['coding'] = code_codings[7]
    expected['code']['text'] = code_texts[7]

    procedure_class.set_profile_urls(profile_urls)

    procedure_class.set_status(status)

    procedure_class.set_code_coding(code_codings[7])
    procedure_class.set_code_text(code_texts[7])

    procedure_class.set_subject(subject)

    procedure_class.set_performer(performer)

    procedure_class.set_performed_date_time(performed_date_time)

    procedure_class.set_note(note)

    procedure_class.create()

    assert procedure_class.payload_template == expected

def test_create_change_of_diaper(procedure_class, profile_urls, status, code_codings, code_texts, subject, performer, performed_date_time, note, expected_payload):
    expected = expected_payload
    expected['code']['coding'] = code_codings[8]
    expected['code']['text'] = code_texts[8]

    procedure_class.set_profile_urls(profile_urls)

    procedure_class.set_status(status)

    procedure_class.set_code_coding(code_codings[8])
    procedure_class.set_code_text(code_texts[8])

    procedure_class.set_subject(subject)

    procedure_class.set_performer(performer)

    procedure_class.set_performed_date_time(performed_date_time)

    procedure_class.set_note(note)

    procedure_class.create()

    assert procedure_class.payload_template == expected
