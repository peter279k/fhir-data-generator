from urllib.parse import urlencode


class Claim:
    def __init__(self, claim_id=''):
        self.claim_id = claim_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'Claim',
            'id': claim_id,
            'meta': {
                'profile': [],
            },
            'identifier': [{}],
            'status': '',
            'type': {
                'coding': [],
            },
            'use': 'claim',
            'patient': {},
            'created': '',
            'provider': {},
            'priority': {
                'coding': [],
            },
            'diagnosis': [],
            'insurance': [],
            'item': [],
            'total': {},
        }

        if claim_id == '':
            del self.payload_template['id']

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_identifier(self, identifier: list):
        self.payload_template['identifier'] = identifier

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_type_coding(self, type_coding: list):
        self.payload_template['type']['coding'] = type_coding

    def set_patient(self, patient: dict):
        self.payload_template['patient'] = patient

    def set_created(self, created: str):
        self.payload_template['created'] = created

    def set_provider(self, provider: dict):
        self.payload_template['provider'] = provider

    def set_priority_coding(self, coding: list):
        self.payload_template['priority']['coding'] = coding

    def set_diagnosis(self, diagnosis: list):
        self.payload_template['diagnosis'] = diagnosis

    def set_insurance(self, insurance: list):
        self.payload_template['insurance'] = insurance

    def set_item(self, item: list):
        self.payload_template['item'] = item

    def set_total(self, total: dict):
        self.payload_template['total'] = total

    def create(self):
        return self.payload_template

    def build_composition_id_query(self, composition_id: str):
        return urlencode({'_id': composition_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
