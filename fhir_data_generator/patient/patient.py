from urllib.parse import urlencode


class Patient:
    def __init__(self, patient_id=''):
        self.patient_id = patient_id

        self.profile_urls = []
        self.profile_urls_append = self.profile_urls.append
        self.profile_urls_remove = self.profile_urls.remove

        self.identifiers = []
        self.identifiers_append = self.identifiers.append
        self.identifiers_remove = self.identifiers.remove

        self.managing_organization_reference = ''

        self.active = True

        self.names = []
        self.names_append = self.names.append
        self.names_remove = self.names.remove

        self.gender = ''

        self.birth_date = ''

        self.addresses = []
        self.addresses_append = self.addresses.append
        self.addresses_remove = self.addresses.remove

        self.telecoms = []
        self.telecoms_append = self.telecoms.append
        self.telecoms_remove = self.telecoms.remove

        self.contacts = []
        self.contacts_append = self.contacts.append
        self.contacts_remove = self.contacts.remove

        self.communications = []
        self.communications_append = self.communications.append
        self.communications_remove = self.communications.remove

        self.allowed_scenario = [1, 2, 3]
        self.payload_template = {
            'resourceType': 'Patient',
            'meta': {
                'profile': [],
            },
            'identifier': [],
            'active': True,
            'managingOrganization': {
                'reference': '',
            },
            'name': [],
            'gender': '',
            'birthDate': '',
            'address': [],
            'telecom': [],
        }

        self.api_endpoint = ''

    def set_profile_url(self, profile_url: str):
        if profile_url not in self.profile_urls:
            self.profile_urls_append(profile_url)

        return True

    def remove_profile_url(self, profile_url: str):
        if profile_url in self.profile_urls:
            self.profile_urls_remove(profile_url)

        return True

    def set_identifier(self, identifier: dict):
        if identifier not in self.identifiers:
            self.identifiers_append(identifier)

        return True

    def remove_identifier(self, identifier: dict):
        if identifier in self.identifiers:
            self.identifiers_remove(identifier)

        return True

    def set_active(self, active: bool):
        self.active = active

        return True

    def set_managing_organization(self, managing_organization: str):
        self.managing_organization_reference = managing_organization

        return True

    def set_name(self, name: dict):
        if name not in self.names:
            self.names_append(name)

        return True

    def remove_name(self, name: dict):
        if name in self.names:
            self.names_remove(name)

        return True

    def set_gender(self, gender: str):
        self.gender = gender

        return True

    def set_birth_date(self, birth_date: str):
        self.birth_date = birth_date

        return True

    def set_address(self, address: dict):
        if address not in self.addresses:
            self.addresses_append(address)

        return True

    def remove_address(self, address: dict):
        if address in self.addresses:
            self.addresses_remove(address)

        return True

    def set_telecom(self, telecom: dict):
        if telecom not in self.telecoms:
            self.telecoms_append(telecom)

        return True

    def remove_telecom(self, telecom: dict):
        if telecom in self.telecoms:
            self.telecoms_remove(telecom)

        return True

    def set_contact(self, contact: dict):
        if contact not in self.contacts:
            self.contacts_append(contact)

        return True

    def remove_contact(self, contact: dict):
        if contact in self.contacts:
            self.contacts_remove(contact)

        return True

    def set_communication(self, communication: dict):
        if communication not in self.communications:
            self.communications_append(communication)

        return True

    def remove_communication(self, communication: dict):
        if communication in self.communications:
            self.communications_remove(communication)

        return True

    def set_patient_id(self, patient_id: str):
        self.patient_id = patient_id

        return True

    def create(self, scenario=1, update=False):
        if scenario not in self.allowed_scenario:
            raise Exception(f'The specific {scenario} is not invalid.')

        self.payload_template['meta']['profile'] = self.profile_urls
        self.payload_template['identifier'] = self.identifiers
        self.payload_template['active'] = self.active
        self.payload_template['managingOrganization']['reference'] = self.managing_organization_reference
        self.payload_template['name'] = self.names
        self.payload_template['gender'] = self.gender
        self.payload_template['birthDate'] = self.birth_date
        self.payload_template['address'] = self.addresses
        self.payload_template['telecom'] = self.telecoms

        if update is True:
            self.payload_template['id'] = self.patient_id

        if scenario == 2:
            self.payload_template['communication'] = self.communications

        if scenario == 3:
            del self.payload_template['name']
            del self.payload_template['telecom']
            self.payload_template['contact'] = self.contacts

        return self.payload_template

    def set_fhir_server_endpoint(self, api_endpoint: str):
        self.api_endpoint = api_endpoint

        return True

    def build_patient_id_query(self, patient_id: str):
        return urlencode({'_id': patient_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
