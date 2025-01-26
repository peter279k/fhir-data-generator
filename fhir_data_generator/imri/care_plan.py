from urllib.parse import urlencode


class CarePlan:
    def __init__(self, care_plan_id=''):
        self.care_plan_id = care_plan_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'CarePlan',
            'id': care_plan_id,
            'meta': {
                'profile': [],
            },
            'status': '',
            'intent': 'proposal',
            'description': '',
            'subject': {},
            'encounter': {},
            'activity': [],
        }

        if care_plan_id == '':
            del self.payload_template['id']

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_intent(self, intent: str):
        self.payload_template['intent'] = intent

    def set_description(self, description: str):
        self.payload_template['description'] = description

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_encounter(self, encounter: dict):
        self.payload_template['encounter'] = encounter

    def set_activity(self, activity: list):
        self.payload_template['activity'] = activity

    def create(self):
        return self.payload_template

    def build_care_plan_id_query(self, care_plan_id: str):
        return urlencode({'_id': care_plan_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
