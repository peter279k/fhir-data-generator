from urllib.parse import urlencode


class OrganizationH:
    def __init__(self, organization_id):
        self.organization_id = organization_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'Organization',
            'id': organization_id,
            'meta': {
                'profile': [],
            },
            'identifier': [],
            'type': [{
                'coding': [],
            }],
            'name': '',
        }

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_identifiers(self, identifiers: list):
        self.payload_template['identifier'] = identifiers

    def set_type_coding(self, type_coding: list):
        self.payload_template['type'][0]['coding'] = type_coding

    def set_name(self, name: str):
        self.payload_template['name'] = name

    def create(self):
        return self.payload_template

    def build_organization_id_query(self, organization_id: str):
        return urlencode({'_id': organization_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
