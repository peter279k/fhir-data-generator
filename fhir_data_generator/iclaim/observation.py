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
            'identifier': [],
            'status': '',
            'category': [{
                'coding': [],
            }],
            'code': {
                'coding': [],
            },
            'subject': {},
            'issued': '',
            'effectiveDateTime': '',
            'performer': [],
            'valueCodeableConcept': {},
            'valueQuantity': {},
            'interpretation': [],
            'note': [],
            'bodySite': {
                'coding': [],
            },
            'referenceRange': [],
        }

        if observation_id == '':
            del self.payload_template['id']

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_identifier(self, identifier: list):
        self.payload_template['identifier'] = identifier

    def set_category_coding(self, category_coding: list):
        self.payload_template['category'][0]['coding'] = category_coding

    def set_code_coding(self, code_coding: list):
        self.payload_template['code']['coding'] = code_coding

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_issued(self, issued: str):
        self.payload_template['issued'] = issued

    def set_effective_datetime(self, effective_datetime: str):
        self.payload_template['effectiveDateTime'] = effective_datetime

    def set_performer(self, performer: list):
        self.payload_template['performer'] = performer

    def set_value_codeable_concept(self, value_codeable_concept: dict):
        self.payload_template['valueCodeableConcept'] = value_codeable_concept

    def set_value_quantity(self, value_quantity: dict):
        self.payload_template['valueQuantity'] = value_quantity

    def set_interpretation(self, interpretation: list):
        self.payload_template['interpretation'] = interpretation

    def set_note(self, note: list):
        self.payload_template['note'] = note

    def set_body_site_coding(self, body_site_coding: list):
        self.payload_template['bodySite']['coding'] = body_site_coding

    def set_reference_range(self, reference_range: list):
        self.payload_template['referenceRange'] = reference_range

    def create(self):
        if self.payload_template['identifier'] == []:
            del self.payload_template['identifier']
        if self.payload_template['issued'] == '':
            del self.payload_template['issued']
        if self.payload_template['valueQuantity'] == {}:
            del self.payload_template['valueQuantity']
        if self.payload_template['interpretation'] == []:
            del self.payload_template['interpretation']
        if self.payload_template['note'] == []:
            del self.payload_template['note']
        if self.payload_template['bodySite'] == {'coding': []}:
            del self.payload_template['bodySite']
        if self.payload_template['referenceRange'] == []:
            del self.payload_template['referenceRange']
        if self.payload_template['valueCodeableConcept'] == {}:
            del self.payload_template['valueCodeableConcept']

        return self.payload_template

    def build_observation_id_query(self, observation_id: str):
        return urlencode({'_id': observation_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
