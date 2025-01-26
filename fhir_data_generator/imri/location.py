from urllib.parse import urlencode


class Location:
    def __init__(self, location_id=''):
        self.location_id = location_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'Location',
            'id': location_id,
            'meta': {
                'profile': [],
            },
            'identifier': [],
            'name': '',
        }

        if location_id == '':
            del self.payload_template['id']

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_identifier(self, identifier: list):
        self.payload_template['identifier'] = identifier

    def set_name(self, name: str):
        self.payload_template['name'] = name

    def create(self):
        return self.payload_template

    def build_location_id_query(self, location_id: str):
        return urlencode({'_id': location_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
