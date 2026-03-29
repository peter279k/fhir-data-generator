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
            'active': None,
            'practitioner': {},
            'organization': {},
            'code': [],
            'specialty': [],
            'telecom': [],
            'availableTime': [],
        }

        if practitioner_role_id == '':
            del self.payload_template['id']

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_active(self, active: bool):
        self.payload_template['active'] = active

    def set_practitioner(self, practitioner: dict):
        self.payload_template['practitioner'] = practitioner

    def set_organization(self, organization: dict):
        self.payload_template['organization'] = organization

    def set_code(self, code: list):
        self.payload_template['code'] = code

    def set_specialty(self, specialty: list):
        self.payload_template['specialty'] = specialty

    def set_telecom(self, telecom: list):
        self.payload_template['telecom'] = telecom

    def set_available_time(self, available_time: list):
        self.payload_template['availableTime'] = available_time

    def create(self):
        if self.payload_template['active'] is None:
            del self.payload_template['active']
        if len(self.payload_template['availableTime']) == 0:
            del self.payload_template['availableTime']
        if self.payload_template['specialty'] == []:
            del self.payload_template['specialty']
        if len(self.payload_template['telecom']) == 0:
            del self.payload_template['telecom']

        return self.payload_template

    def build_practitioner_role_id_query(self, practitioner_role_id: str):
        return urlencode({'_id': practitioner_role_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
