from urllib.parse import urlencode


class MedicationAdministration:
    def __init__(self, medication_administration_id=''):
        self.medication_administration_id = medication_administration_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'MedicationAdministration',
            'id': medication_administration_id,
            'meta': {
                'profile': [],
            },
            'status': '',
            'medicationCodeableConcept': {
                'coding': [],
                'text': '',
            },
            'subject': {},
            'effectiveDateTime': '',
            'performer': [],
            'note': [],
            'dosage': {},
        }

        if medication_administration_id == '':
            del self.payload_template['id']

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_medication_codeable_concept_coding(self, concept_coding: list):
        self.payload_template['medicationCodeableConcept']['coding'] = concept_coding

    def set_medication_codeable_concept_text(self, text: str):
        self.payload_template['medicationCodeableConcept']['text'] = text

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_effective_date_time(self, effective_date_time: str):
        self.payload_template['effectiveDateTime'] = effective_date_time

    def set_performer(self, performer: list):
        self.payload_template['performer'] = performer

    def set_note(self, note: list):
        self.payload_template['note'] = note

    def set_dosage(self, dosage: dict):
        self.payload_template['dosage'] = dosage

    def create(self):
        return self.payload_template

    def build_medication_administration_id_query(self, medication_administration_id: str):
        return urlencode({'_id': medication_administration_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
