from urllib.parse import urlencode


class Composition:
    def __init__(self, composition_id=''):
        self.composition_id = composition_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'Composition',
            'id': composition_id,
            'meta': {
                'profile': [],
            },
            'status': '',
            'type': {
                'coding': [],
            },
            'subject': {},
            'encounter': {},
            'date': '',
            'author': [],
            'title': '',
            'section': [],
        }

        if composition_id == '':
            del self.payload_template['id']

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_type_coding(self, type_coding: list):
        self.payload_template['type']['coding'] = type_coding

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_encounter(self, encounter: dict):
        self.payload_template['encounter'] = encounter

    def set_date(self, date: str):
        self.payload_template['date'] = date

    def set_author(self, author: list):
        self.payload_template['author'] = author

    def set_title(self, title: str):
        self.payload_template['title'] = title

    def set_section(self, section: list):
        self.payload_template['section'] = section

    def create(self):
        if self.payload_template['encounter'] == {}:
            del self.payload_template['encounter']

        return self.payload_template

    def build_composition_id_query(self, composition_id: str):
        return urlencode({'_id': composition_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
