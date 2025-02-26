from urllib.parse import urlencode


class DiagnosticReport:
    def __init__(self, diagnostic_report_id=''):
        self.diagnostic_report_id = diagnostic_report_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'DiagnosticReport',
            'id': diagnostic_report_id,
            'meta': {
                'profile': [],
            },
            'status': '',
            'category': [{
                'coding': [],
                'text': '',
            }],
            'code': {
                'coding': [],
                'text': '',
            },
            'subject': {},
            'effectiveDateTime': '',
            'issued': '',
            'performer': [],
            'result': [],
        }

        if diagnostic_report_id == '':
            del self.payload_template['id']

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_category_coding(self, category_coding: list):
        self.payload_template['category'][0]['coding'] = category_coding

    def set_category_text(self, category_text: str):
        self.payload_template['category'][0]['text'] = category_text

    def set_code_coding(self, coding: list):
        self.payload_template['code']['coding'] = coding

    def set_code_text(self, text: str):
        self.payload_template['code']['text'] = text

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_effective_datetime(self, effective_datetime: str):
        self.payload_template['effectiveDateTime'] = effective_datetime

    def set_issued(self, issued: str):
        self.payload_template['issued'] = issued

    def set_performer(self, performer: list):
        self.payload_template['performer'] = performer

    def set_result(self, result: list):
        self.payload_template['result'] = result

    def create(self):
        if self.payload_template['category'] == [{'coding': [], 'text': ''}]:
            del self.payload_template['category']
        if self.payload_template['code']['text'] == '':
            del self.payload_template['code']['text']
        if self.payload_template['performer'] == []:
            del self.payload_template['performer']
        if self.payload_template['issued'] == '':
            del self.payload_template['issued']
        if self.payload_template['effectiveDateTime'] == '':
            del self.payload_template['effectiveDateTime']

        return self.payload_template

    def build_diagnostic_report_id_query(self, diagnostic_report_id: str):
        return urlencode({'_id': diagnostic_report_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
