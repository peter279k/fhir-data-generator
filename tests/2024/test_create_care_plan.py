from fixtures.care_plan_2024 import *


def test_create(care_plan_class, profile_urls, status, intent, category_coding, description, subject, author, goal, activity_progress, activity_detail, note, expected_payload):
    expected = expected_payload

    care_plan_class.set_profile_urls(profile_urls)

    care_plan_class.set_status(status)

    care_plan_class.set_intent(intent)

    care_plan_class.set_category_coding(category_coding)

    care_plan_class.set_description(description)

    care_plan_class.set_subject(subject)

    care_plan_class.set_author(author)

    care_plan_class.set_goal(goal)

    care_plan_class.set_activity_progress(activity_progress)
    care_plan_class.set_activity_detail(activity_detail)

    care_plan_class.set_note(note)

    care_plan_class.create()

    assert care_plan_class.payload_template == expected
