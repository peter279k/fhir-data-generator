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
            'identifier': [],
            'name': [],
            'active': None,
            'telecom': [],
            'gender': '',
            'birthDate': '',
            'address': [],
            'contact': [],
            'managingOrganization': {},
        }

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_identifiers(self, identifiers: list):
        self.payload_template['identifier'] = identifiers

    def set_names(self, names: list):
        self.payload_template['name'] = names

    def set_active(self, active: bool):
        self.payload_template['active'] = active

    def set_telecom(self, telecom: list):
        self.payload_template['telecom'] = telecom

    def set_gender(self, gender: str):
        self.payload_template['gender'] = gender

    def set_birth_date(self, birth_date: str):
        self.payload_template['birthDate'] = birth_date

    def set_address(self, address: list):
        self.payload_template['address'] = address

    def set_contact(self, contact: list):
        self.payload_template['contact'] = contact

    def set_managing_organization(self, managing: dict):
        self.payload_template['managingOrganization'] = managing

    def create(self):
        if self.payload_template['active'] is None:
            del self.payload_template['active']
        if len(self.payload_template['telecom']) == 0:
            del self.payload_template['telecom']
        if self.payload_template['gender'] == '':
            del self.payload_template['gender']
        if self.payload_template['birthDate'] == '':
            del self.payload_template['birthDate']
        if len(self.payload_template['address']) == 0:
            del self.payload_template['address']
        if len(self.payload_template['contact']) == 0:
            del self.payload_template['contact']
        if self.payload_template['managingOrganization'] == {}:
            del self.payload_template['managingOrganization']

        return self.payload_template

    def build_patient_id_query(self, patient_id: str):
        return urlencode({'_id': patient_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
