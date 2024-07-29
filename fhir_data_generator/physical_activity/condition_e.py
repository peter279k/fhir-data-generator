from urllib.parse import urlencode


class ConditionE:
    def __init__(self, condition_id):
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
            'asserter': {},
        }

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

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

    def set_asserter(self, asserter: dict):
        self.payload_template['asserter'] = asserter

    def create(self):
        return self.payload_template

    def build_condition_e_id_query(self, condition_e_id: str):
        return urlencode({'_id': condition_e_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
