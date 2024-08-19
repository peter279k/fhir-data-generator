from urllib.parse import urlencode


class PractitionerRole:
    def __init__(self, practitioner_role_id=''):
        self.practitioner_role_id = practitioner_role_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'PractitionerRole',
            'id': practitioner_role_id,
            'meta': {
                'profile': [],
            },
            'identifier' : [],
            'active': True,
            'period': {},
            'practitioner': {},
            'code': [],
            'specialty': [{
                'coding': [],
            }],
            'location': [],
            'telecom': [],
            'availableTime': [],
            'notAvailable': [],
            'availabilityExceptions': '',
        }

        if practitioner_role_id == '':
            del self.payload_template['id']

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_identifiers(self, identifiers: list):
        self.payload_template['identifier'] = identifiers

    def set_active(self, active: bool):
        self.payload_template['active'] = active

    def set_period(self, period: dict):
        self.payload_template['period'] = period

    def set_practitioner(self, practitioner: dict):
        self.payload_template['practitioner'] = practitioner

    def set_code(self, code: list):
        self.payload_template['code'] = code

    def set_specialty_coding(self, specialty_coding: list):
        self.payload_template['specialty'][0]['coding'] = specialty_coding

    def set_location(self, location: list):
        self.payload_template['location'] = location

    def set_telecom(self, telecom: list):
        self.payload_template['telecom'] = telecom

    def set_available_time(self, available_time: list):
        self.payload_template['availableTime'] = available_time

    def set_not_available(self, not_available: list):
        self.payload_template['notAvailable'] = not_available

    def set_availability_exceptions(self, availability_exception: str):
        self.payload_template['availabilityExceptions'] = availability_exception

    def create(self):
        return self.payload_template

    def build_practitioner_role_id_query(self, practitioner_role_id: str):
        return urlencode({'_id': practitioner_role_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
