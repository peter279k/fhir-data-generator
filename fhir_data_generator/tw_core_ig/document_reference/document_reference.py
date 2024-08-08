from urllib.parse import urlencode


class DocumentReference:
    def __init__(self, document_reference_id):
        self.document_reference_id = document_reference_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'DocumentReference',
            'id': document_reference_id,
            'meta': {
                'profile': [],
            },
            'status': '',
            'type': {
                'coding': [],
                'text': '',
            },
            'subject': {},
            'date': '',
            'author': [],
            'custodian': {},
            'content': [],
        }

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_type_coding(self, type_coding: list):
        self.payload_template['type']['coding'] = type_coding

    def set_type_text(self, type_text: str):
        self.payload_template['type']['text'] = type_text

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_date(self, date: str):
        self.payload_template['date'] = date

    def set_author(self, author: list):
        self.payload_template['author'] = author

    def set_custodian(self, custodian: dict):
        self.payload_template['custodian'] = custodian

    def set_content(self, content: list):
        self.payload_template['content'] = content

    def create(self):
        return self.payload_template

    def build_document_reference_id_query(self, document_reference_id: str):
        return urlencode({'_id': document_reference_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
