from urllib.parse import urlencode


class Encounter:
    def __init__(self, encounter_id):
        self.encounter_id = encounter_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'Encounter',
            'id': encounter_id,
            'meta': {
                'profile': [],
            },
            'identifier': [],
            'status': '',
            'class': {},
            'type': [{
                'coding': [],
            }],
            'serviceType': {
                'coding': [],
                'text': '',
            },
            'subject': {},
            'participant': [{
                'type': [{
                    'coding': [],
                }],
                'period': {},
                'individual': {},
            }],
            'period': {},
            'reasonCode': [{
                'coding': [],
            }],
            'hospitalization': {
                'dischargeDisposition': {
                    'coding': [],
                },
            },
            'location': [{
                'location': {},
            }],
        }

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_identifier(self, identifier: list):
        self.payload_template['identifier'] = identifier

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_class(self, the_class: dict):
        self.payload_template['class'] = the_class

    def set_type_coding(self, type_coding: list):
        self.payload_template['type'][0]['coding'] = type_coding

    def set_service_type_coding(self, service_type_coding: list):
        self.payload_template['serviceType']['coding'] = service_type_coding

    def set_service_type_text(self, service_type_text: str):
        self.payload_template['serviceType']['text'] = service_type_text

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_participant_type_coding(self, participant_type_coding: list):
        self.payload_template['participant'][0]['type'][0]['coding'] = participant_type_coding

    def set_participant_period(self, participant_period: dict):
        self.payload_template['participant'][0]['period'] = participant_period

    def set_participant_individual(self, participant_individual: dict):
        self.payload_template['participant'][0]['individual'] = participant_individual

    def set_period(self, period: dict):
        self.payload_template['period'] = period

    def set_reason_code_coding(self, reason_code_coding: list):
        self.payload_template['reasonCode'][0]['coding'] = reason_code_coding

    def set_hospitalization_discharge_disposition_coding(self, coding: list):
        self.payload_template['hospitalization']['dischargeDisposition']['coding'] = coding

    def set_location(self, location_location: dict):
        self.payload_template['location'][0]['location'] = location_location

    def create(self):
        return self.payload_template

    def build_encounter_id_query(self, encounter_id: str):
        return urlencode({'_id': encounter_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
