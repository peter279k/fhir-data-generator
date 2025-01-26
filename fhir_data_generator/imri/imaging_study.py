from urllib.parse import urlencode


class ImagingStudy:
    def __init__(self, imaging_study_id=''):
        self.imaging_study_id = imaging_study_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'ImagingStudy',
            'id': imaging_study_id,
            'meta': {
                'profile': [],
            },
            'status': '',
            'subject': {},
            'encounter': {},
            'started': '',
            'interpreter': [],
            'description': '',
        }

        if imaging_study_id == '':
            del self.payload_template['id']

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_encounter(self, encounter: dict):
        self.payload_template['encounter'] = encounter

    def set_started(self, started: str):
        self.payload_template['started'] = started

    def set_interpreter(self, interpreter: list):
        self.payload_template['interpreter'] = interpreter

    def set_description(self, description: str):
        self.payload_template['description'] = description

    def create(self):
        return self.payload_template

    def build_imaging_study_id_query(self, imaging_study_id: str):
        return urlencode({'_id': imaging_study_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
