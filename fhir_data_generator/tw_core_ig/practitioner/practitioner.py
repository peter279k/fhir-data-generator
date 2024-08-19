from urllib.parse import urlencode


class Practitioner:
    def __init__(self, practitioner_id=''):
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
            'name': [],
            'telecom': [],
            'address': [],
            'gender': '',
            'birthDate': '',
            'photo': [],
            'qualification': [],
        }

        if practitioner_id == '':
            del self.payload_template['id']

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_identifiers(self, identifiers: list):
        self.payload_template['identifier'] = identifiers

    def set_active(self, active: bool):
        self.payload_template['active'] = active

    def set_name(self, name: list):
        self.payload_template['name'] = name

    def set_telecom(self, telecom: list):
        self.payload_template['telecom'] = telecom

    def set_address(self, address: list):
        self.payload_template['address'] = address

    def set_gender(self, gender: str):
        self.payload_template['gender'] = gender

    def set_birth_date(self, birth_date: str):
        self.payload_template['birthDate'] = birth_date

    def set_photo(self, photo: list):
        self.payload_template['photo'] = photo

    def set_qualification(self, qualification: list):
        self.payload_template['qualification'] = qualification

    def create(self):
        return self.payload_template

    def build_practitioner_id_query(self, practitioner_id: str):
        return urlencode({'_id': practitioner_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
