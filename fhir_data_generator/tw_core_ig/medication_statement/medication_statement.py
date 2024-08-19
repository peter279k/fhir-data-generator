from urllib.parse import urlencode


class MedicationStatement:
    def __init__(self, medication_statement_id=''):
        self.medication_statement_id = medication_statement_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'MedicationStatement',
            'id': medication_statement_id,
            'meta': {
                'profile': [],
            },
            'status': '',
            'category': {
                'coding': [],
                'text': '',
            },
            'medicationCodeableConcept': {
                'coding': [],
                'text': '',
            },
            'subject': {},
            'effectiveDateTime': '',
            'dateAsserted': '',
            'reasonCode': [{
                'coding': [],
                'text': '',
            }],
            'note': [],
            'dosage': [{
                'text': '',
                'timing': {
                    'repeat': {},
                },
                'route': {
                    'coding': [],
                    'text': '',
                },
            }],
        }

        if medication_statement_id == '':
            del self.payload_template['id']

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_category_coding(self, category_coding: list):
        self.payload_template['category']['coding'] = category_coding

    def set_category_text(self, text: str):
        self.payload_template['category']['text'] = text

    def set_medication_codeable_concept_coding(self, concept_coding: list):
        self.payload_template['medicationCodeableConcept']['coding'] = concept_coding

    def set_medication_codeable_concept_text(self, text: str):
        self.payload_template['medicationCodeableConcept']['text'] = text

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_effective_date_time(self, effective_date_time: str):
        self.payload_template['effectiveDateTime'] = effective_date_time

    def set_date_asserted(self, date_asserted: str):
        self.payload_template['dateAsserted'] = date_asserted

    def set_reason_code_coding(self, code_coding: list):
        self.payload_template['reasonCode'][0]['coding'] = code_coding

    def set_reason_code_text(self, code_text: str):
        self.payload_template['reasonCode'][0]['text'] = code_text

    def set_note(self, note: list):
        self.payload_template['note'] = note

    def set_dosage_text(self, text: str):
        self.payload_template['dosage'][0]['text'] = text

    def set_dosage_timing_repeat(self, timing_repeat: dict):
        self.payload_template['dosage'][0]['timing']['repeat'] = timing_repeat

    def set_dosage_route_coding(self, route_coding: list):
        self.payload_template['dosage'][0]['route']['coding'] = route_coding

    def set_dosage_route_text(self, route_text: str):
        self.payload_template['dosage'][0]['route']['text'] = route_text

    def create(self):
        return self.payload_template

    def build_medication_statement_id_query(self, medication_statement_id: str):
        return urlencode({'_id': medication_statement_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
