from urllib.parse import urlencode


class Goal:
    def __init__(self, goal_id):
        self.goal_id = goal_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'Goal',
            'id': goal_id,
            'meta': {
                'profile': [],
            },
            'identifier' : [],
            'lifecycleStatus': '',
            'category': [{
                'coding': [],
            }],
            'description': {
                'text': '',
            },
            'subject': {},
            'target': [{
                'measure': {
                    'coding': [],
                },
                'detailQuantity': {},
            }],
        }

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_identifiers(self, identifiers: list):
        self.payload_template['identifier'] = identifiers

    def set_lifecycle_status(self, lifecycle_status: str):
        self.payload_template['lifecycleStatus'] = lifecycle_status

    def set_category_coding(self, coding: list):
        self.payload_template['category'][0]['coding'] = coding

    def set_description_text(self, text: str):
        self.payload_template['description']['text'] = text

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_target_measure_coding(self, target_measure_coding: list):
        self.payload_template['target'][0]['measure']['coding'] = target_measure_coding

    def set_target_detail_quantity(self, target_detail_quantity: dict):
        self.payload_template['target'][0]['detailQuantity'] = target_detail_quantity

    def create(self):
        return self.payload_template

    def build_goal_id_query(self, goal_id: str):
        return urlencode({'_id': goal_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
