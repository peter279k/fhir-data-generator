from urllib.parse import urlencode


class QuestionnaireResponse:
    def __init__(self, response_id=''):
        self.response_id = response_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'QuestionnaireResponse',
            'id': response_id,
            'meta': {
                'profile': [],
            },
            'extension': [],
            'questionnaire': '',
            'status': '',
            'subject': {},
            'authored': '',
            'author': {},
            'source': {},
            'item': [],
        }

        if response_id == '':
            del self.payload_template['id']

    def set_response_id(self, response_id):
        self.response_id = response_id

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_extension(self, extension: list):
        self.payload_template['extension'] = extension

    def set_questionnaire(self, questionnaire_url: str):
        self.payload_template['questionnaire'] = questionnaire_url

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_authored(self, authored: str):
        self.payload_template['authored'] = authored

    def set_author(self, author: dict):
        self.payload_template['author'] = author

    def set_source(self, source: dict):
        self.payload_template['source'] = source

    def set_item(self, item: list):
        self.payload_template['item'] = item

    def create(self):
        if len(self.payload_template['meta']['profile']) == 0:
            del self.payload_template['meta']

        if len(self.payload_template['extension']) == 0:
            del self.payload_template['extension']

        if self.payload_template['questionnaire'] == '':
            del self.payload_template['questionnaire']

        if self.payload_template['subject'] == {}:
            del self.payload_template['subject']

        if self.payload_template['authored'] == '':
            del self.payload_template['authored']

        if self.payload_template['author'] == {}:
            del self.payload_template['author']

        if self.payload_template['source'] == {}:
            del self.payload_template['source']

        if len(self.payload_template['item']) == 0:
            del self.payload_template['item']

        return self.payload_template

    def build_questionnaire_response_id_query(self, response_id: str):
        return urlencode({'_id': response_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
