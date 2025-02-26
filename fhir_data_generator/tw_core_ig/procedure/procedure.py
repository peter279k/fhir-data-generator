from urllib.parse import urlencode


class Procedure:
    def __init__(self, procedure_id=''):
        self.procedure_id = procedure_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'Procedure',
            'id': procedure_id,
            'meta': {
                'profile': [],
            },
            'partOf': [],
            'status': '',
            'category': {
                'coding': [],
            },
            'code': {
                'coding': [],
                'text': '',
            },
            'subject': {},
            'encounter': {},
            'performedDateTime': '',
            'asserter': {},
            'performer': [],
            'bodySite': [{
                'coding': [],
            }],
            'reasonReference': [],
            'report': [],
            'note': [],
            'usedCode': [],
        }

        if procedure_id == '':
            del self.payload_template['id']

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_part_of(self, part_of: list):
        self.payload_template['partOf'] = part_of

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_category(self, category: dict):
        self.payload_template['category'] = category

    def set_code_coding(self, coding: list):
        self.payload_template['code']['coding'] = coding

    def set_code_text(self, text: str):
        self.payload_template['code']['text'] = text

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_encounter(self, encounter: dict):
        self.payload_template['encounter'] = encounter

    def set_performed_date_time(self, performed_date_time: str):
        self.payload_template['performedDateTime'] = performed_date_time

    def set_asserter(self, asserter: dict):
        self.payload_template['asserter'] = asserter

    def set_performer(self, performer: list):
        self.payload_template['performer'] = performer

    def set_body_site_coding(self, body_site_coding: list):
        self.payload_template['bodySite'][0]['coding'] = body_site_coding

    def set_reason_reference(self, reason_reference: list):
        self.payload_template['reasonReference'] = reason_reference

    def set_report(self, report: list):
        self.payload_template['report'] = report

    def set_note(self, note: list):
        self.payload_template['note'] = note

    def set_used_code(self, used_code: list):
        self.payload_template['usedCode'] = used_code

    def create(self):
        if self.payload_template['partOf'] == []:
            del self.payload_template['partOf']
        if self.payload_template['category'] == {'coding': []}:
            del self.payload_template['category']
        if self.payload_template['encounter'] == {}:
            del self.payload_template['encounter']
        if self.payload_template['performedDateTime'] == '':
            del self.payload_template['performedDateTime']
        if self.payload_template['asserter'] == {}:
            del self.payload_template['asserter']
        if self.payload_template['performer'] == []:
            del self.payload_template['performer']
        if self.payload_template['bodySite'] == [{'coding': []}]:
            del self.payload_template['bodySite']
        if self.payload_template['report'] == []:
            del self.payload_template['report']
        if self.payload_template['note'] == []:
            del self.payload_template['note']
        if self.payload_template['usedCode'] == []:
            del self.payload_template['usedCode']
        if self.payload_template['reasonReference'] == []:
            del self.payload_template['reasonReference']
        if self.payload_template['code']['text'] == '':
            del self.payload_template['code']['text']

        return self.payload_template

    def build_procedure_role_id_query(self, procedure_id: str):
        return urlencode({'_id': procedure_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
