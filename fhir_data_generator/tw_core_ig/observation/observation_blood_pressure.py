from urllib.parse import urlencode


class Observation:
    def __init__(self, observation_id=''):
        self.observation_id = observation_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'Observation',
            'id': observation_id,
            'meta': {
                'profile': [],
            },
            'status': '',
            'category': [{
                'coding': [],
            }],
            'code': {
                'coding': [],
                'text': '',
            },
            'subject': {},
            'effectiveDateTime': '',
            'performer': [],
            'component': [],
        }

        if observation_id == '':
            del self.payload_template['id']

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_category_coding(self, category_coding: list):
        self.payload_template['category'][0]['coding'] = category_coding

    def set_code_coding(self, code_coding: list):
        self.payload_template['code']['coding'] = code_coding

    def set_code_text(self, code_text: str):
        self.payload_template['code']['text'] = code_text

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_effective_datetime(self, effective_datetime: str):
        self.payload_template['effectiveDateTime'] = effective_datetime

    def set_performer(self, performer: list):
        self.payload_template['performer'] = performer

    def set_component(self, component: list):
        self.payload_template['component'] = component

    def create(self):
        return self.payload_template

    def build_observation_id_query(self, observation_id: str):
        return urlencode({'_id': observation_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
