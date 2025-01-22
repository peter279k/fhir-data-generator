from urllib.parse import urlencode


class Patient:
    def __init__(self, patient_id=''):
        self.patient_id = patient_id

        self.payload_template = {
            'resourceType': 'Patient',
            'id': patient_id,
            'meta': {
                'profile': [],
            },
            'extension': [],
            'identifier': [],
            'name': [{
                'use': '',
                'text': '',
            }],
            'gender': '',
            'birthDate': '',
            'address': [],
        }

        if patient_id == '':
            del self.payload_template['id']

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_extension(self, extension: list):
        self.payload_template['extension'] = extension

    def set_identifiers(self, identifiers: list):
        self.payload_template['identifier'] = identifiers

    def set_name_use(self, name_use: str):
        self.payload_template['name'][0]['use'] = name_use

    def set_name_text(self, name_text: str):
        self.payload_template['name'][0]['text'] = name_text

    def set_gender(self, gender: str):
        self.payload_template['gender'] = gender

    def set_birth_date(self, birth_date: str):
        self.payload_template['birthDate'] = birth_date

    def set_address(self, address: list):
        self.payload_template['address'] = address

    def create(self):
        return self.payload_template

    def build_patient_id_query(self, patient_id: str):
        return urlencode({'_id': patient_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
