from urllib.parse import urlencode


class Condition:
    def __init__(self, condition_id=''):
        self.condition_id = condition_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'Condition',
            'id': condition_id,
            'meta': {
                'profile': [],
            },
            'clinicalStatus': {
                'coding': [],
            },
            'category': [{
                'coding': [],
            }],
            'code': {
                'coding': [],
                'text': '',
            },
            'subject': {},
            'encounter': {},
            'note': [],
        }

        if condition_id == '':
            del self.payload_template['id']

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_identifier(self, identifier: list):
        self.payload_template['identifier'] = identifier

    def set_clinical_status_coding(self, clinical_status_coding: list):
        self.payload_template['clinicalStatus']['coding'] = clinical_status_coding

    def set_category_coding(self, category_coding: list):
        self.payload_template['category'][0]['coding'] = category_coding

    def set_code_coding(self, code_coding: list):
        self.payload_template['code']['coding'] = code_coding

    def set_code_text(self, code_text: str):
        self.payload_template['code']['text'] = code_text

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_encounter(self, encounter: dict):
        self.payload_template['encounter'] = encounter

    def set_note(self, note: list):
        self.payload_template['note'] = note

    def create(self):
        return self.payload_template

    def build_condition_id_query(self, condition_id: str):
        return urlencode({'_id': condition_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
