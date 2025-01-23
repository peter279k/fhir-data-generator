from urllib.parse import urlencode


class Coverage:
    def __init__(self, coverage_id=''):
        self.coverage_id = coverage_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'Coverage',
            'id': coverage_id,
            'meta': {
                'profile': [],
            },
            'status': '',
            'beneficiary': {},
            'payor': [],
        }

        if coverage_id == '':
            del self.payload_template['id']

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_beneficiary(self, beneficiary: dict):
        self.payload_template['beneficiary'] = beneficiary

    def set_payor(self, payor: list):
        self.payload_template['payor'] = payor

    def create(self):
        return self.payload_template

    def build_coverage_id_query(self, coverage_id: str):
        return urlencode({'_id': coverage_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
