from fixtures.questionnaire_response_ltc import *


def test_create_cdr_moderate_example(questionnaire_response_classes, profile_urls, extensions, questionnaires, status, subject, authored_lists, author, source, items, expected_payload):
    expected = expected_payload
    expected_payload['id'] = questionnaire_response_classes[0].response_id
    expected['extension'] = extensions[0]
    expected['authored'] = authored_lists[0]
    expected['item'] = items[0]
    expected['meta']['profile'] = profile_urls[0]
    expected['questionnaire'] = questionnaires[0]

    questionnaire_response_classes[0].set_profile_urls(profile_urls[0])

    questionnaire_response_classes[0].set_extension(extensions[0])

    questionnaire_response_classes[0].set_questionnaire(questionnaires[0])

    questionnaire_response_classes[0].set_status(status)

    questionnaire_response_classes[0].set_subject(subject)

    questionnaire_response_classes[0].set_authored(authored_lists[0])

    questionnaire_response_classes[0].set_author(author)

    questionnaire_response_classes[0].set_source(source)

    questionnaire_response_classes[0].set_item(items[0])

    questionnaire_response_classes[0].create()

    assert questionnaire_response_classes[0].payload_template == expected

def test_create_cdr_example(questionnaire_response_classes, profile_urls, extensions, questionnaires, status, subject, authored_lists, author, source, items, expected_payload):
    expected = expected_payload
    expected_payload['id'] = questionnaire_response_classes[1].response_id
    expected['extension'] = extensions[1]
    expected['authored'] = authored_lists[1]
    expected['item'] = items[1]
    expected['meta']['profile'] = profile_urls[1]
    expected['questionnaire'] = questionnaires[1]

    questionnaire_response_classes[1].set_profile_urls(profile_urls[1])

    questionnaire_response_classes[1].set_extension(extensions[1])

    questionnaire_response_classes[1].set_questionnaire(questionnaires[1])

    questionnaire_response_classes[1].set_status(status)

    questionnaire_response_classes[1].set_subject(subject)

    questionnaire_response_classes[1].set_authored(authored_lists[1])

    questionnaire_response_classes[1].set_author(author)

    questionnaire_response_classes[1].set_source(source)

    questionnaire_response_classes[1].set_item(items[1])

    questionnaire_response_classes[1].create()

    assert questionnaire_response_classes[1].payload_template == expected

def test_create_cdr_complete_example(questionnaire_response_classes, profile_urls, extensions, questionnaires, status, subject, authored_lists, author, source, items, expected_payload):
    expected = expected_payload
    expected_payload['id'] = questionnaire_response_classes[2].response_id
    expected['extension'] = extensions[2]
    expected['authored'] = authored_lists[2]
    expected['item'] = items[2]
    expected['meta']['profile'] = profile_urls[1]
    expected['questionnaire'] = questionnaires[1]

    questionnaire_response_classes[2].set_profile_urls(profile_urls[1])

    questionnaire_response_classes[2].set_extension(extensions[2])

    questionnaire_response_classes[2].set_questionnaire(questionnaires[1])

    questionnaire_response_classes[2].set_status(status)

    questionnaire_response_classes[2].set_subject(subject)

    questionnaire_response_classes[2].set_authored(authored_lists[2])

    questionnaire_response_classes[2].set_author(author)

    questionnaire_response_classes[2].set_source(source)

    questionnaire_response_classes[2].set_item(items[2])

    questionnaire_response_classes[2].create()

    assert questionnaire_response_classes[2].payload_template == expected

def test_create_mmse_example(questionnaire_response_classes, profile_urls, extensions, questionnaires, status, subject, authored_lists, author, source, mmse_items, expected_payload):
    items = mmse_items
    expected = expected_payload
    expected_payload['id'] = questionnaire_response_classes[3].response_id
    expected['extension'] = extensions[3]
    expected['authored'] = authored_lists[3]
    expected['item'] = items[0]
    expected['meta']['profile'] = profile_urls[1]
    expected['questionnaire'] = questionnaires[1]

    questionnaire_response_classes[3].set_profile_urls(profile_urls[1])

    questionnaire_response_classes[3].set_extension(extensions[3])

    questionnaire_response_classes[3].set_questionnaire(questionnaires[1])

    questionnaire_response_classes[3].set_status(status)

    questionnaire_response_classes[3].set_subject(subject)

    questionnaire_response_classes[3].set_authored(authored_lists[3])

    questionnaire_response_classes[3].set_author(author)

    questionnaire_response_classes[3].set_source(source)

    questionnaire_response_classes[3].set_item(items[0])

    questionnaire_response_classes[3].create()

    assert questionnaire_response_classes[3].payload_template == expected

def test_create_mmse_complete_example(questionnaire_response_classes, profile_urls, extensions, questionnaires, status, subject, authored_lists, author, source, mmse_items, expected_payload):
    items = mmse_items
    expected = expected_payload
    expected_payload['id'] = questionnaire_response_classes[4].response_id
    expected['extension'] = extensions[4]
    expected['authored'] = authored_lists[4]
    expected['item'] = items[1]
    expected['meta']['profile'] = profile_urls[1]
    expected['questionnaire'] = questionnaires[1]

    questionnaire_response_classes[4].set_profile_urls(profile_urls[1])

    questionnaire_response_classes[4].set_extension(extensions[4])

    questionnaire_response_classes[4].set_questionnaire(questionnaires[1])

    questionnaire_response_classes[4].set_status(status)

    questionnaire_response_classes[4].set_subject(subject)

    questionnaire_response_classes[4].set_authored(authored_lists[4])

    questionnaire_response_classes[4].set_author(author)

    questionnaire_response_classes[4].set_source(source)

    questionnaire_response_classes[4].set_item(items[1])

    questionnaire_response_classes[4].create()

    assert questionnaire_response_classes[4].payload_template == expected

def test_create_mmse_impaired_example(questionnaire_response_classes, profile_urls, extensions, questionnaires, status, subject, authored_lists, author, source, mmse_items, expected_payload):
    items = mmse_items
    expected = expected_payload
    expected_payload['id'] = questionnaire_response_classes[5].response_id
    expected['extension'] = extensions[5]
    expected['authored'] = authored_lists[5]
    expected['item'] = items[2]
    expected['meta']['profile'] = profile_urls[1]
    expected['questionnaire'] = questionnaires[1]

    questionnaire_response_classes[5].set_profile_urls(profile_urls[1])

    questionnaire_response_classes[5].set_extension(extensions[5])

    questionnaire_response_classes[5].set_questionnaire(questionnaires[1])

    questionnaire_response_classes[5].set_status(status)

    questionnaire_response_classes[5].set_subject(subject)

    questionnaire_response_classes[5].set_authored(authored_lists[5])

    questionnaire_response_classes[5].set_author(author)

    questionnaire_response_classes[5].set_source(source)

    questionnaire_response_classes[5].set_item(items[2])

    questionnaire_response_classes[5].create()

    assert questionnaire_response_classes[5].payload_template == expected

