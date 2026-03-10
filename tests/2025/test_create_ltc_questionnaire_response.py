from fixtures.questionnaire_response_ltc import *


def test_create_moderate_example(questionnaire_response_classes, profile_urls, extensions, questionnaire, status, subject, authored_lists, author, source, items, expected_payload):
    expected = expected_payload
    expected_payload['id'] = questionnaire_response_classes[0].response_id
    expected['extension'] = extensions[0]
    expected['authored'] = authored_lists[0]
    expected['item'] = items[0]

    questionnaire_response_classes[0].set_profile_urls(profile_urls)

    questionnaire_response_classes[0].set_extension(extensions[0])

    questionnaire_response_classes[0].set_questionnaire(questionnaire)

    questionnaire_response_classes[0].set_status(status)

    questionnaire_response_classes[0].set_subject(subject)

    questionnaire_response_classes[0].set_authored(authored_lists[0])

    questionnaire_response_classes[0].set_author(author)

    questionnaire_response_classes[0].set_source(source)

    questionnaire_response_classes[0].set_item(items[0])

    questionnaire_response_classes[0].create()

    assert questionnaire_response_classes[0].payload_template == expected

def test_create_example(questionnaire_response_classes, profile_urls, extensions, questionnaire, status, subject, authored_lists, author, source, items, expected_payload):
    expected = expected_payload
    expected_payload['id'] = questionnaire_response_classes[1].response_id
    expected['extension'] = extensions[1]
    expected['authored'] = authored_lists[1]
    expected['item'] = items[1]

    questionnaire_response_classes[1].set_profile_urls(profile_urls)

    questionnaire_response_classes[1].set_extension(extensions[1])

    questionnaire_response_classes[1].set_questionnaire(questionnaire)

    questionnaire_response_classes[1].set_status(status)

    questionnaire_response_classes[1].set_subject(subject)

    questionnaire_response_classes[1].set_authored(authored_lists[1])

    questionnaire_response_classes[1].set_author(author)

    questionnaire_response_classes[1].set_source(source)

    questionnaire_response_classes[1].set_item(items[1])

    questionnaire_response_classes[1].create()

    assert questionnaire_response_classes[1].payload_template == expected

def test_create_complete_example(questionnaire_response_classes, profile_urls, extensions, questionnaire, status, subject, authored_lists, author, source, items, expected_payload):
    expected = expected_payload
    expected_payload['id'] = questionnaire_response_classes[2].response_id
    expected['extension'] = extensions[2]
    expected['authored'] = authored_lists[2]
    expected['item'] = items[2]

    questionnaire_response_classes[2].set_profile_urls(profile_urls)

    questionnaire_response_classes[2].set_extension(extensions[2])

    questionnaire_response_classes[2].set_questionnaire(questionnaire)

    questionnaire_response_classes[2].set_status(status)

    questionnaire_response_classes[2].set_subject(subject)

    questionnaire_response_classes[2].set_authored(authored_lists[2])

    questionnaire_response_classes[2].set_author(author)

    questionnaire_response_classes[2].set_source(source)

    questionnaire_response_classes[2].set_item(items[2])

    questionnaire_response_classes[2].create()

    assert questionnaire_response_classes[2].payload_template == expected
