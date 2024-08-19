from urllib.parse import urlencode


class Medication:
    def __init__(self, medication_id=''):
        self.medication_id = medication_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'Medication',
            'id': medication_id,
            'meta': {
                'profile': [],
            },
            'code': {
                'coding': [],
                'text': '',
            },
            'form': {
                'coding': [],
                'text': '',
            },
        }

        if medication_id == '':
            del self.payload_template['id']

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_code_coding(self, coding: list):
        self.payload_template['code']['coding'] = coding

    def set_code_text(self, code_text: str):
        self.payload_template['code']['text'] = code_text

    def set_form_coding(self, form_coding: list):
        self.payload_template['form']['coding'] = form_coding

    def set_form_text(self, form_text: str):
        self.payload_template['form']['text'] = form_text

    def create(self):
        return self.payload_template

    def build_encounter_id_query(self, encounter_id: str):
        return urlencode({'_id': encounter_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
