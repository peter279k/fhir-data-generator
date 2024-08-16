from urllib.parse import urlencode


class Observation:
    def __init__(self, observation_id):
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
            'valueQuantity': {},
        }

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

    def set_value_quantity(self, value_quantity: dict):
        self.payload_template['valueQuantity'] = value_quantity

    def create(self):
        return self.payload_template

    def build_medication_statement_id_query(self, medication_statement_id: str):
        return urlencode({'_id': medication_statement_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)