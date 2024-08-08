from urllib.parse import urlencode


class ImagingStudy:
    def __init__(self, imaging_study_id):
        self.imaging_study_id = imaging_study_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'ImagingStudy',
            'id': imaging_study_id,
            'meta': {
                'profile': [],
            },
            'identifier': [],
            'status': '',
            'subject': {},
            'encounter': {},
            'started': '',
            'numberOfSeries': None,
            'numberOfInstances': None,
            'procedureReference': {},
            'procedureCode': [{
                'coding': [],
            }],
            'series': [{
                'uid': '',
                'modality': {},
                'bodySite': {},
                'performer': [{
                    'actor': {},
                }],
                'instance': [{
                    'uid': '',
                    'sopClass': {},
                }],
            }],
        }

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_identifier(self, identifier: list):
        self.payload_template['identifier'] = identifier

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_encounter(self, encounter: dict):
        self.payload_template['encounter'] = encounter

    def set_started(self, started: str):
        self.payload_template['started'] = started

    def set_number_of_series(self, number_of_series: int):
        self.payload_template['numberOfSeries'] = number_of_series

    def set_number_of_instances(self, number_of_instances: int):
        self.payload_template['numberOfInstances'] = number_of_instances

    def set_procedure_reference(self, procedure_reference: dict):
        self.payload_template['procedureReference'] = procedure_reference

    def set_procedure_code_coding(self, procedure_code_coding: list):
        self.payload_template['procedureCode'][0]['coding'] = procedure_code_coding

    def set_series_uid(self, uid: str):
        self.payload_template['series'][0]['uid'] = uid

    def set_series_modality(self, modality: dict):
        self.payload_template['series'][0]['modality'] = modality

    def set_series_body_site(self, body_site: dict):
        self.payload_template['series'][0]['bodySite'] = body_site

    def set_series_performer_actor(self, performer_actor: dict):
        self.payload_template['series'][0]['performer'][0]['actor'] = performer_actor

    def set_series_instance_uid(self, uid: str):
        self.payload_template['series'][0]['instance'][0]['uid'] = uid

    def set_series_instance_sop_class(self, sop_class: dict):
        self.payload_template['series'][0]['instance'][0]['sopClass'] = sop_class

    def create(self):
        return self.payload_template

    def build_imaging_study_id_query(self, imaging_study_id: str):
        return urlencode({'_id': imaging_study_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
