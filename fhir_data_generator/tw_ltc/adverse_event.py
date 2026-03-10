from urllib.parse import urlencode


class AdverseEvent:
    def __init__(self, event_id=''):
        self.event_id = event_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'AdverseEvent',
            'id': event_id,
            'meta': {
                'profile': [],
            },
            'extension': [],
            'identifier': {},
            'actuality': '',
            'event': {},
            'subject': {},
            'date': '',
            'detected': '',
            'recordedDate': '',
            'location': {},
            'seriousness': {},
            'severity': {},
            'outcome': {},
            'recorder': {},
        }

        if event_id == '':
            del self.payload_template['id']

    def set_event_id(self, event_id):
        self.event_id = event_id

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_extension(self, extension: list):
        self.payload_template['extension'] = extension

    def set_identifier(self, identifier: dict):
        self.payload_template['identifier'] = identifier

    def set_actuality(self, actuality: str):
        self.payload_template['actuality'] = actuality

    def set_event(self, event: dict):
        self.payload_template['event'] = event

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_date(self, date: str):
        self.payload_template['date'] = date

    def set_recorded_date(self, recorded_date: str):
        self.payload_template['recordedDate'] = recorded_date

    def set_detected(self, detected: str):
        self.payload_template['detected'] = detected

    def set_location(self, location: dict):
        self.payload_template['location'] = location

    def set_seriousness(self, seriousness: dict):
        self.payload_template['seriousness'] = seriousness

    def set_severity(self, severity: dict):
        self.payload_template['severity'] = severity

    def set_outcome(self, outcome: dict):
        self.payload_template['outcome'] = outcome

    def set_recorder(self, recorder: dict):
        self.payload_template['recorder'] = recorder

    def set_event(self, event: dict):
        self.payload_template['event'] = event

    def create(self):
        if len(self.payload_template['extension']) == 0:
            del self.payload_template['extension']
        if self.payload_template['detected'] == '':
            del self.payload_template['detected']
        if self.payload_template['location'] == {}:
            del self.payload_template['location']
        if self.payload_template['seriousness'] == {}:
            del self.payload_template['seriousness']
        if self.payload_template['severity'] == {}:
            del self.payload_template['severity']
        if self.payload_template['outcome'] == {}:
            del self.payload_template['outcome']
        if self.payload_template['recorder'] == {}:
            del self.payload_template['recorder']
        if self.payload_template['event'] == {}:
            del self.payload_template['event']

        return self.payload_template

    def build_adverse_event_id_query(self, event_id: str):
        return urlencode({'_id': event_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
