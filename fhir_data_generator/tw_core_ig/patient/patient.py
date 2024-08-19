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
            'extension': [
                {
                    'url': '',
                    'valueAge' : {},
                },
                {
                    'extension': [{
                        'url': 'code',
                        'valueCodeableConcept': {
                            'coding': [],
                        },
                    }],
                    'url': '',
                },
            ],
            'identifier': [],
            'active': True,
            'name': [{
                'use': '',
                'text': '',
                'family': '',
                'given': [],
            }],
            'telecom': [],
            'gender': '',
            'birthDate': '',
            'address': [{
                'extension': [],
                'text': '',
                'line': [],
                'city': '',
                'district': '',
                '_postalCode': {
                    'extension': [],
                },
                'country': 'TW',
            }],
            'maritalStatus': {
                'coding': [],
            },
            'photo': [],
            'contact': [{
                'relationship': [{
                    'coding': [],
                }],
                'name': {},
                'telecom': [],
            }],
            'communication': [{
                'language': {
                    'coding': [],
                },
            }],
            'managingOrganization': {},
        }

        if patient_id == '':
            del self.payload_template['id']

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_extension_url(self, extension_url: str):
        self.payload_template['extension'][0]['url'] = extension_url

    def set_extension_value_age(self, value_age: dict):
        self.payload_template['extension'][0]['valueAge'] = value_age

    def set_extension_extension_coding(self, extension_coding: list):
        self.payload_template['extension'][1]['extension'][0]['valueCodeableConcept']['coding'] = extension_coding

    def set_extension_extension_url(self, extension_extension_url: str):
        self.payload_template['extension'][1]['url'] = extension_extension_url

    def set_identifiers(self, identifiers: list):
        self.payload_template['identifier'] = identifiers

    def set_active(self, active: bool):
        self.payload_template['active'] = active

    def set_name_use(self, name_use: str):
        self.payload_template['name'][0]['use'] = name_use

    def set_name_text(self, name_text: str):
        self.payload_template['name'][0]['text'] = name_text

    def set_name_family(self, name_family: str):
        self.payload_template['name'][0]['family'] = name_family

    def set_name_given(self, name_given: str):
        self.payload_template['name'][0]['given'] = name_given

    def set_telecom(self, telecom: list):
        self.payload_template['telecom'] = telecom

    def set_gender(self, gender: str):
        self.payload_template['gender'] = gender

    def set_birth_date(self, birth_date: str):
        self.payload_template['birthDate'] = birth_date

    def set_address_extension(self, address_extension: list):
        self.payload_template['address'][0]['extension'] = address_extension

    def set_address_text(self, address_text: str):
        self.payload_template['address'][0]['text'] = address_text

    def set_address_line(self, address_line: list):
        self.payload_template['address'][0]['line'] = address_line

    def set_address_city(self, address_city: str):
        self.payload_template['address'][0]['city'] = address_city

    def set_address_district(self, address_district: str):
        self.payload_template['address'][0]['district'] = address_district

    def set_address_postal_code_extension(self, address_postal_code: list):
        self.payload_template['address'][0]['_postalCode']['extension'] = address_postal_code

    def set_marital_status_coding(self, marital_status_coding: list):
        self.payload_template['maritalStatus']['coding'] = marital_status_coding

    def set_photo(self, photo: list):
        self.payload_template['photo'] = photo

    def set_contact(self, contact_relationship_coding: dict):
        self.payload_template['contact'][0]['relationship'][0]['coding'] = contact_relationship_coding

    def set_contact_name(self, contact_name: dict):
        self.payload_template['contact'][0]['name'] = contact_name

    def set_contact_telecom(self, contact_telecom: list):
        self.payload_template['contact'][0]['telecom'] = contact_telecom

    def set_communication_language_coding(self, communication_lang_coding: list):
        self.payload_template['communication'][0]['language']['coding'] = communication_lang_coding

    def set_managing_organization(self, managing_organization: dict):
        self.payload_template['managingOrganization'] = managing_organization

    def create(self):
        return self.payload_template

    def build_patient_id_query(self, patient_id: str):
        return urlencode({'_id': patient_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
