from urllib.parse import urlencode


class AllergyIntoleranceNut:
    def __init__(self, allergy_intolerance_id):
        self.allergy_intolerance_id = allergy_intolerance_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'AllergyIntolerance',
            'id': allergy_intolerance_id,
            'meta': {
                'profile': [],
            },
            'clinicalStatus': {
                'coding': [],
                'text': '',
            },
            'verificationStatus': {
                'coding': [],
                'text': '',
            },
            'type': 'allergy',
            'category': [],
            'criticality': '',
            'code': {
                'coding': [],
                'text': '',
            },
            'patient': {},
            'onsetDateTime': '',
            'recordedDate': '',
            'recorder': {},
            'asserter': {},
            'lastOccurrence': '',
            'note': [],
            'reaction' : [{
                'substance' : {
                    'coding' : [{
                        'system' : 'http://snomed.info/sct',
                        'code' : '3193000',
                        'display' : 'alpha-1,4-Glucan-protein synthase (uridine diphosphate-forming)'
                    }],
                    'text' : 'alpha-1,4-Glucan-protein synthase (uridine diphosphate-forming)'
                },
                'manifestation' : [{
                    'coding' : [{
                        'system' : 'http://snomed.info/sct',
                        'code' : '39579001',
                        'display' : 'Anaphylaxis (disorder)'
                    }]
                }],
                'description' : '',
                'severity' : '',
                'exposureRoute' : {
                    'coding' : [{
                        'system' : 'http://snomed.info/sct',
                        'code' : '26643006',
                        'display' : 'Oral use'
                    }],
                    'text' : ''
                },
                'note' : [],
            }]
        }

    def set_allergy_intolerance_id(self, allergy_intolerance_id):
        self.allergy_intolerance_id = allergy_intolerance_id

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_clinical_status_coding(self, coding: list):
        self.payload_template['clinicalStatus']['coding'] = coding

    def set_clinical_status_text(self, text: str):
        self.payload_template['clinicalStatus']['text'] = text

    def set_verification_status_coding(self, coding: list):
        self.payload_template['verificationStatus']['coding'] = coding

    def set_verification_status_text(self, text: str):
        self.payload_template['verificationStatus']['text'] = text

    def set_category(self, category: list):
        self.payload_template['category'] = category

    def set_criticality(self, criticality: str):
        self.payload_template['criticality'] = criticality

    def set_code_coding(self, coding: list):
        self.payload_template['code']['coding'] = coding

    def set_code_text(self, text: str):
        self.payload_template['code']['text'] = text

    def set_patient(self, patient: dict):
        self.payload_template['patient'] = patient

    def set_onset_datetime(self, onset_datetime: str):
        self.payload_template['onsetDateTime'] = onset_datetime

    def set_recorded_date(self, recorded_date: str):
        self.payload_template['recordedDate'] = recorded_date

    def set_recorder(self, recorder: dict):
        self.payload_template['recorder'] = recorder

    def set_asserter(self, asserter: dict):
        self.payload_template['asserter'] = asserter

    def set_last_occurrence(self, last_occurrence: str):
        self.payload_template['lastOccurrence'] = last_occurrence

    def set_note(self, note: list):
        self.payload_template['note'] = note

    def set_reaction_description(self, description: str):
        self.payload_template['reaction'][0]['description'] = description

    def set_reaction_severity(self, severity: str):
        self.payload_template['reaction'][0]['severity'] = severity

    def set_reaction_exposure_route_text(self, text: str):
        self.payload_template['reaction'][0]['exposureRoute']['text'] = text

    def set_reaction_note(self, reaction_note: list):
        self.payload_template['reaction'][0]['note'] = reaction_note

    def create(self):
        return self.payload_template

    def build_allergy_intolerance_id_query(self, allergy_intolerance_id: str):
        return urlencode({'_id': allergy_intolerance_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
