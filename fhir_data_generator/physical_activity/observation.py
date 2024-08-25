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
            'valueCodeableConcept': {},
            'valueQuantity': {},
            'bodySite': {},
            'component': [],
            'hasMember': [],
        }

        if observation_id == '':
            del self.payload_template['id']

    def set_observation_id(self, observation_id):
        self.observation_id = observation_id

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_category_coding(self, coding: list):
        self.payload_template['category'][0]['coding'] = coding

    def set_code_coding(self, coding: list):
        self.payload_template['code']['coding'] = coding

    def set_code_text(self, text: str):
        self.payload_template['code']['text'] = text

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_effective_datetime(self, effective_datetime: str):
        self.payload_template['effectiveDateTime'] = effective_datetime

    def set_performer(self, performer: list):
        self.payload_template['performer'] = performer

    def set_value_quantity(self, value_quantity: dict):
        self.payload_template['valueQuantity'] = value_quantity

    def set_has_member(self, has_member: list):
        self.payload_template['hasMember'] = has_member

    def set_component(self, component: list):
        self.payload_template['component'] = component

    def set_body_site(self, body_site: dict):
        self.payload_template['bodySite'] = body_site

    def set_value_codeable_concept(self, codeable_concept: dict):
        self.payload_template['valueCodeableConcept'] = codeable_concept

    def create(self):
        if len(self.payload_template['hasMember']) == 0:
            del self.payload_template['hasMember']

        if len(self.payload_template['component']) == 0:
            del self.payload_template['component']
        else:
            del self.payload_template['valueQuantity']

        if self.payload_template['bodySite'] == {}:
            del self.payload_template['bodySite']

        if self.payload_template['valueCodeableConcept'] == {}:
            del self.payload_template['valueCodeableConcept']

        if (self.payload_template['code']['text'] == ''):
           del self.payload_template['code']['text']

        return self.payload_template

    def build_observation_id_query(self, observation_id: str):
        return urlencode({'_id': observation_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
