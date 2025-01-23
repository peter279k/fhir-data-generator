from fixtures.coverage_iclaim_2024 import *


def test_create(coverage_class, profile_urls, status, beneficiary, payor, expected_payload):
    expected = expected_payload

    coverage_class.set_profile_urls(profile_urls)

    coverage_class.set_status(status)

    coverage_class.set_beneficiary(beneficiary)

    coverage_class.set_payor(payor)

    coverage_class.create()

    assert coverage_class.payload_template == expected
