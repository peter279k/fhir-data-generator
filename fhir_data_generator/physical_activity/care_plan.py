from urllib.parse import urlencode


class CarePlan:
    def __init__(self, care_plan_id):
        self.care_plan_id = care_plan_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'CarePlan',
            'id': care_plan_id,
            'meta': {
                'profile': [],
            },
            'status': '',
            'intent': 'plan',
            'category': [{
                'coding': [],
            }],
            'description': '',
            'subject': {},
            'goal': [],
            'activity': [{
                'progress': [],
                'detail': {},
            }],
            'note': [],
        }

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_intent(self, intent: str):
        self.payload_template['intent'] = intent

    def set_category_coding(self, coding: list):
        self.payload_template['category'][0]['coding'] = coding

    def set_description(self, description: str):
        self.payload_template['description'] = description

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_author(self, author: dict):
        self.payload_template['author'] = author

    def set_goal(self, goal: list):
        self.payload_template['goal'] = goal

    def set_activity_progress(self, progress: list):
        self.payload_template['activity'][0]['progress'] = progress

    def set_activity_detail(self, detail: dict):
        self.payload_template['activity'][0]['detail'] = detail

    def set_note(self, note: list):
        self.payload_template['note'] = note

    def create(self):
        return self.payload_template

    def build_care_plan_id_query(self, care_plan_id: str):
        return urlencode({'_id': care_plan_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
