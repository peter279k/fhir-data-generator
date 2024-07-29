from urllib.parse import urlencode


class Practitioner:
    def __init__(self, practitioner_id):
        self.practitioner_id = practitioner_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'Practitioner',
            'id': practitioner_id,
            'meta': {
                'profile': [],
            },
            'identifier' : [],
            'active': True,
            'name': [{
                'text': '',
            }],
        }

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_identifiers(self, identifiers: list):
        self.payload_template['identifier'] = identifiers

    def set_active(self, active: bool):
        self.payload_template['active'] = active

    def set_name_text(self, name_text: str):
        self.payload_template['name'][0]['text'] = name_text

    def create(self):
        return self.payload_template

    def build_practitioner_id_query(self, practitioner_id: str):
        return urlencode({'_id': practitioner_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
