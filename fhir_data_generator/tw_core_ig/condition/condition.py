from urllib.parse import urlencode


class Condition:
    def __init__(self, condition_id):
        self.condition_id = condition_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'Condition',
            'id': condition_id,
            'meta': {
                'profile': [],
            },
            'clinicalStatus': {
                'coding': [],
            },
            'verificationStatus': {
                'coding': [],
            },
            'category': [{
                'coding': [],
            }],
            'severity': {
                'coding': [],
            },
            'code': {
                'coding': [],
                'text': '',
            },
            'subject': {},
            'onsetDateTime': '',
            'abatementDateTime': '',
            'asserter': {},
        }

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_clinical_status_coding(self, clinical_status_coding: list):
        self.payload_template['clinicalStatus']['coding'] = clinical_status_coding

    def set_verification_status_coding(self, verification_status_coding: list):
        self.payload_template['verificationStatus']['coding'] = verification_status_coding

    def set_category_coding(self, category_coding: list):
        self.payload_template['category'][0]['coding'] = category_coding

    def set_severity_coding(self, severity_coding: list):
        self.payload_template['severity']['coding'] = severity_coding

    def set_code_coding(self, code_coding: list):
        self.payload_template['code']['coding'] = code_coding

    def set_code_text(self, code_text: str):
        self.payload_template['code']['text'] = code_text

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_onset_datetime(self, onset_datetime: str):
        self.payload_template['onsetDateTime'] = onset_datetime

    def set_abatement_datetime(self, abatement_dateTime: str):
        self.payload_template['abatementDateTime'] = abatement_dateTime

    def set_asserter(self, asserter: dict):
        self.payload_template['asserter'] = asserter

    def create(self):
        return self.payload_template

    def build_condition_id_query(self, condition_id: str):
        return urlencode({'_id': condition_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
