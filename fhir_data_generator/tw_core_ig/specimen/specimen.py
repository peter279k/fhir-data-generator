from urllib.parse import urlencode


class Specimen:
    def __init__(self, specimen_id=''):
        self.specimen_id = specimen_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'Specimen',
            'id': specimen_id,
            'meta': {
                'profile': [],
            },
            'identifier': [],
            'accessionIdentifier': {},
            'status': '',
            'type': {
                'coding': [],
            },
            'subject': {},
            'receivedTime': '',
            'collection': {
                'collector': {},
                'collectedDateTime': '',
                'quantity': {},
                'method': {
                    'coding': [],
                    'text': '',
                },
                'bodySite': {
                    'coding': [],
                    'text': '',
                },
                'fastingStatusCodeableConcept': {
                    'coding': [],
                },
            },
            'processing': [],
            'container': [],
            'note': [],
        }

        if specimen_id == '':
            del self.payload_template['id']

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_identifier(self, identifier: list):
        self.payload_template['identifier'] = identifier

    def set_accession_identifier(self, accession_identifier: dict):
        self.payload_template['accessionIdentifier'] = accession_identifier

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_type_coding(self, type_coding: list):
        self.payload_template['type']['coding'] = type_coding

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_received_time(self, received_time: str):
        self.payload_template['receivedTime'] = received_time

    def set_collection_collector(self, collection_collector: dict):
        self.payload_template['collection']['collector'] = collection_collector

    def set_collection_collected_date_time(self, collection_collected_date_time: str):
        self.payload_template['collection']['collectedDateTime'] = collection_collected_date_time

    def set_collection_quantity(self, collection_quantity: dict):
        self.payload_template['collection']['quantity'] = collection_quantity

    def set_collection_method_coding(self, collection_method_coding: list):
        self.payload_template['collection']['method']['coding'] = collection_method_coding

    def set_collection_method_text(self, collection_method_text: str):
        self.payload_template['collection']['method']['text'] = collection_method_text

    def set_collection_body_site_coding(self, collection_body_site_coding: list):
        self.payload_template['collection']['bodySite']['coding'] = collection_body_site_coding

    def set_collection_body_site_text(self, collection_body_site_text: str):
        self.payload_template['collection']['bodySite']['text'] = collection_body_site_text

    def set_collection_fasting_status_codeable_concept_coding(self, coding: list):
        self.payload_template['collection']['fastingStatusCodeableConcept']['coding'] = coding

    def set_processing(self, processing: list):
        self.payload_template['processing'] = processing

    def set_container(self, container: list):
        self.payload_template['container'] = container

    def set_note(self, note: list):
        self.payload_template['note'] = note

    def create(self):
        return self.payload_template

    def build_specimen_id_query(self, specimen_id: str):
        return urlencode({'_id': specimen_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
