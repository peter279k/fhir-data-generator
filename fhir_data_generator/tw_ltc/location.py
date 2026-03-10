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
            'status': '',
            'name': '',
            'description': '',
            'mode': '',
            'type': [],
            'address': {},
            'position': {},
        }

        if location_id == '':
            del self.payload_template['id']

    def set_location_id(self, location_id):
        self.location_id = location_id

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_name(self, name: str):
        self.payload_template['name'] = name

    def set_description(self, description: str):
        self.payload_template['description'] = description

    def set_mode(self, mode: str):
        self.payload_template['mode'] = mode

    def set_type(self, type: list):
        self.payload_template['type'] = type

    def set_address(self, address: dict):
        self.payload_template['address'] = address

    def set_position(self, position: dict):
        self.payload_template['position'] = position

    def create(self):
        if self.payload_template['status'] == '':
            del self.payload_template['status']
        if self.payload_template['name'] == '':
            del self.payload_template['name']
        if self.payload_template['description'] == '':
            del self.payload_template['description']
        if self.payload_template['mode'] == '':
            del self.payload_template['mode']
        if len(self.payload_template['type']) == 0:
            del self.payload_template['type']
        if self.payload_template['address'] == {}:
            del self.payload_template['address']
        if self.payload_template['position'] == {}:
            del self.payload_template['position']

        return self.payload_template

    def build_location_id_query(self, location_id: str):
        return urlencode({'_id': location_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
