from fixtures.care_plan_imri_2024 import *


def test_create(care_plan_class, profile_urls, status, intent, description, subject, encounter, activity, expected_payload):
    expected = expected_payload

    care_plan_class.set_profile_urls(profile_urls)

    care_plan_class.set_status(status)

    care_plan_class.set_intent(intent)

    care_plan_class.set_description(description)

    care_plan_class.set_subject(subject)

    care_plan_class.set_encounter(encounter)

    care_plan_class.set_activity(activity)

    care_plan_class.create()

    assert care_plan_class.payload_template == expected
