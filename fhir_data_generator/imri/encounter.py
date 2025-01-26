from urllib.parse import urlencode


class Encounter:
    def __init__(self, encounter_id=''):
        self.encounter_id = encounter_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'Encounter',
            'id': encounter_id,
            'meta': {
                'profile': [],
            },
            'status': '',
            'class': {},
            'serviceType': {
                'coding': [],
            },
            'subject': {},
            'participant': [{
                'individual': {},
            }],
            'period': {},
            'hospitalization': {},
        }

        if encounter_id == '':
            del self.payload_template['id']

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_class(self, the_class: dict):
        self.payload_template['class'] = the_class

    def set_service_type_coding(self, service_type_coding: list):
        self.payload_template['serviceType']['coding'] = service_type_coding

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_participant_individual(self, participant_individual: dict):
        self.payload_template['participant'][0]['individual'] = participant_individual

    def set_period(self, period: dict):
        self.payload_template['period'] = period

    def set_hospitalization(self, hospitalization: dict):
        self.payload_template['hospitalization'] = hospitalization

    def create(self):
        return self.payload_template

    def build_encounter_id_query(self, encounter_id: str):
        return urlencode({'_id': encounter_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
