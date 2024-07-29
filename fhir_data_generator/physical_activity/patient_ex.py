from urllib.parse import urlencode


class PatientEX:
    def __init__(self, patient_id=''):
        self.patient_id = patient_id

        self.payload_template = {
            'resourceType': 'Patient',
            'id': patient_id,
            'meta': {
                'profile': [],
            },
            'extension': [{
                'url': '',
                'valueAge' : {},
            }],
            'identifier': [],
            'name': [{
                'text': '',
            }],
            'gender': '',
            'birthDate': '',
        }

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_extension_url(self, extension_url: str):
        self.payload_template['extension'][0]['url'] = extension_url

    def set_extension_value_age(self, value_age: dict):
        self.payload_template['extension'][0]['valueAge'] = value_age

    def set_identifiers(self, identifiers: list):
        self.payload_template['identifier'] = identifiers

    def set_name_text(self, name_text: str):
        self.payload_template['name'][0]['text'] = name_text

    def set_gender(self, gender: str):
        self.payload_template['gender'] = gender

    def set_birth_date(self, birth_date: str):
        self.payload_template['birthDate'] = birth_date

    def create(self):
        return self.payload_template

    def build_patient_id_query(self, patient_id: str):
        return urlencode({'_id': patient_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
