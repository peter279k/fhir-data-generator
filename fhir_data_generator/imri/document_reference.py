from urllib.parse import urlencode


class DocumentReference:
    def __init__(self, document_reference_id=''):
        self.document_reference_id = document_reference_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'DocumentReference',
            'id': document_reference_id,
            'meta': {
                'profile': [],
            },
            'status': '',
            'subject': {},
            'content': [],
        }

        if document_reference_id == '':
            del self.payload_template['id']

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_content(self, content: list):
        self.payload_template['content'] = content

    def create(self):
        return self.payload_template

    def build_document_reference_id_query(self, document_reference_id: str):
        return urlencode({'_id': document_reference_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
