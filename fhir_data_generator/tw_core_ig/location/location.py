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
            'type': [{
                'coding': [],
            }],
            'telecom': [],
            'address': {},
            'position': {},
            'managingOrganization': {},
            'hoursOfOperation': [{
                'daysOfWeek': [],
                'allDay': None,
            }],
        }

        if location_id == '':
            del self.payload_template['id']

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

    def set_type_coding(self, type_coding: list):
        self.payload_template['type'][0]['coding'] = type_coding

    def set_telecom(self, telecom: list):
        self.payload_template['telecom'] = telecom

    def set_address(self, address: dict):
        self.payload_template['address'] = address

    def set_position(self, position: dict):
        self.payload_template['position'] = position

    def set_managing_organization(self, managing_organization: dict):
        self.payload_template['managingOrganization'] = managing_organization

    def set_hours_of_operation_days_of_week(self, days_of_week: list):
        self.payload_template['hoursOfOperation'][0]['daysOfWeek'] = days_of_week

    def set_hours_of_operation_all_day(self, all_day: bool):
        self.payload_template['hoursOfOperation'][0]['allDay'] = all_day

    def create(self):
        return self.payload_template

    def build_location_id_query(self, location_id: str):
        return urlencode({'_id': location_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
