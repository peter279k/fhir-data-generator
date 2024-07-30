from urllib.parse import urlencode


class PhysicalActivityServiceRequest:
    def __init__(self, service_request_id):
        self.service_request_id = service_request_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'ServiceRequest',
            'id': service_request_id,
            'meta': {
                'profile': [],
            },
            'identifier': [],
            'status': '',
            'intent': '',
            'category': [{
                'coding': [],
            }],
            'code': {
                'coding': [],
            },
            'subject': {},
            'authoredOn': '',
            'requester': {},
        }

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_identifiers(self, identifiers: list):
        self.payload_template['identifier'] = identifiers

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_intent(self, intent: str):
        self.payload_template['intent'] = intent

    def set_category_coding(self, category_coding: list):
        self.payload_template['category'][0]['coding'] = category_coding

    def set_code_coding(self, code_coding: list):
        self.payload_template['code']['coding'] = code_coding

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_authored_on(self, authored_on: str):
        self.payload_template['authoredOn'] = authored_on

    def set_requester(self, requester: dict):
        self.payload_template['requester'] = requester

    def create(self):
        return self.payload_template

    def build_service_request_id_query(self, service_request_id: str):
        return urlencode({'_id': service_request_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
