from urllib.parse import urlencode


class Procedure:
    def __init__(self, procedure_id):
        self.procedure_id = procedure_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'Procedure',
            'id': procedure_id,
            'meta': {
                'profile': [],
            },
            'status': '',
            'code': {
                'coding': [],
                'text': '',
            },
            'subject': {},
            'performedDateTime': '',
            'asserter': {},
            'performer': [],
            'bodySite': [{
                'coding': [],
            }],
        }

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_code_coding(self, coding: list):
        self.payload_template['code']['coding'] = coding

    def set_code_text(self, text: str):
        self.payload_template['code']['text'] = text

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_performed_date_time(self, performed_date_time: str):
        self.payload_template['performedDateTime'] = performed_date_time

    def set_asserter(self, asserter: dict):
        self.payload_template['asserter'] = asserter

    def set_performer(self, performer: list):
        self.payload_template['performer'] = performer

    def set_body_site_coding(self, body_site_coding: list):
        self.payload_template['bodySite'][0]['coding'] = body_site_coding

    def create(self):
        return self.payload_template

    def build_procedure_role_id_query(self, procedure_id: str):
        return urlencode({'_id': procedure_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
