from fixtures.patient_ltc_tw_cs100 import *


def test_create(patient_class, identifiers, names, expected_payload):
    expected = expected_payload

    patient_class.set_names(names)

    patient_class.set_identifiers(identifiers)

    patient_class.create()

    assert patient_class.payload_template == expected
