from urllib.parse import urlencode


class Media:
    def __init__(self, media_id):
        self.media_id = media_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'Media',
            'id': media_id,
            'meta': {
                'profile': [],
            },
            'status': '',
            'type': {
                'coding': [],
            },
            'view': {
                'coding': [],
                'text': '',
            },
            'subject': {},
            'createdDateTime': '',
            'issued': '',
            'operator': {},
            'reasonCode': [{
                'coding': [],
            }],
            'bodySite': {
                'coding': [],
            },
            'deviceName': '',
            'height': None,
            'width': None,
            'content': {},
            'note': [],
        }

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_type_coding(self, type_coding: list):
        self.payload_template['type']['coding'] = type_coding

    def set_view_coding(self, view_coding: list):
        self.payload_template['view']['coding'] = view_coding

    def set_view_text(self, view_text: str):
        self.payload_template['view']['text'] = view_text

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_created_datetime(self, created_datetime: str):
        self.payload_template['createdDateTime'] = created_datetime

    def set_issued(self, issued: str):
        self.payload_template['issued'] = issued

    def set_operator(self, operator: dict):
        self.payload_template['operator'] = operator

    def set_reason_code_coding(self, reason_code_coding: list):
        self.payload_template['reasonCode'][0]['coding'] = reason_code_coding

    def set_body_site_coding(self, body_site_coding: list):
        self.payload_template['bodySite']['coding'] = body_site_coding

    def set_device_name(self, device_name: str):
        self.payload_template['deviceName'] = device_name

    def set_height(self, height: int):
        self.payload_template['height'] = height

    def set_width(self, width: int):
        self.payload_template['width'] = width

    def set_content(self, content: dict):
        self.payload_template['content'] = content

    def set_note(self, note: list):
        self.payload_template['note'] = note

    def create(self):
        return self.payload_template

    def build_media_id_query(self, media_id: str):
        return urlencode({'_id': media_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
