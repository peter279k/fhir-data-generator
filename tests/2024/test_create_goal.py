from fixtures.goal_2024 import *


def test_create(goal_class, profile_urls, identifiers, lifecycle_status, category_coding, description_text, subject, target_measure_coding, target_detail_quantity, expected_payload):
    expected = expected_payload

    goal_class.set_profile_urls(profile_urls)

    goal_class.set_identifiers(identifiers)

    goal_class.set_lifecycle_status(lifecycle_status)

    goal_class.set_category_coding(category_coding)

    goal_class.set_description_text(description_text)

    goal_class.set_subject(subject)

    goal_class.set_target_measure_coding(target_measure_coding)
    goal_class.set_target_detail_quantity(target_detail_quantity)

    goal_class.create()

    assert goal_class.payload_template == expected
