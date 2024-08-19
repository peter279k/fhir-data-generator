from urllib.parse import urlencode


class MedicationRequest:
    def __init__(self, medication_request_id=''):
        self.medication_request_id = medication_request_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'MedicationRequest',
            'id': medication_request_id,
            'meta': {
                'profile': [],
            },
            'identifier': [],
            'status': '',
            'statusReason': {
                'coding': [],
            },
            'intent': '',
            'category': [{
                'coding': [],
            }],
            'medicationReference': {},
            'subject': {},
            'encounter': {},
            'authoredOn': '',
            'requester': {},
            'reasonReference': [],
            'dosageInstruction': [{
                'text': '',
                'timing': {
                    'code': {
                        'coding': [],
                        'text': '',
                    },
                },
                'route': {
                    'coding': [],
                },
                'doseAndRate': [{
                    'type': {
                        'coding': [],
                    },
                }],
            }],
            'dispenseRequest': {
                'validityPeriod': {
                    'start': '',
                    'end': '',
                },
            },
        }

        if medication_request_id == '':
            del self.payload_template['id']

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_identifier(self, identifier: list):
        self.payload_template['identifier'] = identifier

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_status_reason_coding(self, status_reason_coding: list):
        self.payload_template['statusReason']['coding'] = status_reason_coding

    def set_intent(self, intent: str):
        self.payload_template['intent'] = intent

    def set_category_coding(self, category_coding: list):
        self.payload_template['category'][0]['coding'] = category_coding

    def set_medication_reference(self, medication_reference: dict):
        self.payload_template['medicationReference'] = medication_reference

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_encounter(self, encounter: dict):
        self.payload_template['encounter'] = encounter

    def set_authored_on(self, authored_on: dict):
        self.payload_template['authoredOn'] = authored_on

    def set_requester(self, requester: dict):
        self.payload_template['requester'] = requester

    def set_reason_reference(self, reason_reference: list):
        self.payload_template['reasonReference'] = reason_reference

    def set_dosage_instruction_text(self, dosage_instruction_text: str):
        self.payload_template['dosageInstruction'][0]['text'] = dosage_instruction_text

    def set_dosage_instruction_timing_coding(self, dosage_instruction_timing_coding: list):
        self.payload_template['dosageInstruction'][0]['timing']['code']['coding'] = dosage_instruction_timing_coding

    def set_dosage_instruction_timing_text(self, dosage_instruction_timing_text: str):
        self.payload_template['dosageInstruction'][0]['timing']['code']['text'] = dosage_instruction_timing_text

    def set_dosage_instruction_route_coding(self, route_coding: list):
        self.payload_template['dosageInstruction'][0]['route']['coding'] = route_coding

    def set_dosage_instruction_dose_rate_type_coding(self, type_coding: list):
        self.payload_template['dosageInstruction'][0]['doseAndRate'][0]['type']['coding'] = type_coding

    def set_dispense_request_validity_period_start(self, validity_period_start: str):
        self.payload_template['dispenseRequest']['validityPeriod']['start'] = validity_period_start

    def set_dispense_request_validity_period_end(self, validity_period_end: str):
        self.payload_template['dispenseRequest']['validityPeriod']['end'] = validity_period_end

    def create(self):
        return self.payload_template

    def build_medication_request_id_query(self, medication_request_id: str):
        return urlencode({'_id': medication_request_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
