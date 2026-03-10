from fixtures.adverse_event_ltc import *


def test_create_adverse_event_ltc_cs100_example(adverse_event_classes, profile_urls, extension, identifiers, actuality, events, subjects, dates, recorded_dates, expected_payload):
    expected = expected_payload
    expected['id'] = adverse_event_classes[0].event_id
    expected['extension'] = extension
    expected['identifier'] = identifiers[0]
    expected['event'] = events[0]
    expected['subject'] = subjects[0]
    expected['date'] = dates[0]
    expected['recordedDate'] = recorded_dates[0]

    del expected['detected']
    del expected['location']
    del expected['seriousness']
    del expected['severity']
    del expected['outcome']
    del expected['recorder']

    adverse_event_class = adverse_event_classes[0]

    adverse_event_class.set_profile_urls(profile_urls)

    adverse_event_class.set_extension(extension)

    adverse_event_class.set_identifier(identifiers[0])

    adverse_event_class.set_actuality(actuality)

    adverse_event_class.set_event(events[0])

    adverse_event_class.set_subject(subjects[0])

    adverse_event_class.set_date(dates[0])

    adverse_event_class.set_recorded_date(recorded_dates[0])

    adverse_event_class.create()

    assert adverse_event_class.payload_template == expected

def test_create_adverse_event_ltc_example(adverse_event_classes, profile_urls, identifiers, actuality, events, subjects, dates, detected, location, seriousness, severity, outcome, recorder, recorded_dates, expected_payload):
    expected = expected_payload
    expected['id'] = adverse_event_classes[1].event_id
    expected['identifier'] = identifiers[1]
    expected['event'] = events[1]
    expected['subject'] = subjects[1]
    expected['date'] = dates[1]
    expected['detected'] = detected
    expected['recordedDate'] = recorded_dates[1]
    expected['location'] = location
    expected['seriousness'] = seriousness
    expected['severity'] = severity
    expected['outcome'] = outcome
    expected['recorder'] = recorder

    del expected['extension']

    adverse_event_class = adverse_event_classes[1]

    adverse_event_class.set_profile_urls(profile_urls)

    adverse_event_class.set_identifier(identifiers[1])

    adverse_event_class.set_actuality(actuality)

    adverse_event_class.set_event(events[1])

    adverse_event_class.set_subject(subjects[1])

    adverse_event_class.set_date(dates[1])

    adverse_event_class.set_detected(detected)

    adverse_event_class.set_location(location)

    adverse_event_class.set_seriousness(seriousness)

    adverse_event_class.set_severity(severity)

    adverse_event_class.set_outcome(outcome)

    adverse_event_class.set_recorder(recorder)

    adverse_event_class.set_recorded_date(recorded_dates[1])

    adverse_event_class.create()

    assert adverse_event_class.payload_template == expected
