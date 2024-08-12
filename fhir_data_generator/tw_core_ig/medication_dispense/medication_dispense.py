from urllib.parse import urlencode


class MedicationDispense:
    def __init__(self, medication_dispense_id):
        self.medication_dispense_id = medication_dispense_id

        self.profile_urls = []

        self.payload_template = {
            'resourceType': 'MedicationDispense',
            'id': medication_dispense_id,
            'meta': {
                'profile': [],
            },
            'status': '',
            'category': {
                'coding': [],
            },
            'medicationReference': {},
            'subject': {},
            'context': {},
            'performer': [{
                'actor': {},
            }],
            'type': {
                'coding': [],
            },
            'quantity': {},
            'daysSupply': {},
            'whenPrepared': '',
            'whenHandedOver': '',
            'dosageInstruction': [],
            'substitution': {
                'wasSubstituted': None,
                'type': {
                    'coding': [],
                },
                'reason': [{
                    'coding': [],
                }],
            },
        }

    def set_profile_urls(self, profile_urls: list):
        self.payload_template['meta']['profile'] = profile_urls

    def set_identifier(self, identifier: list):
        self.payload_template['identifier'] = identifier

    def set_status(self, status: str):
        self.payload_template['status'] = status

    def set_category_coding(self, category_coding: list):
        self.payload_template['category']['coding'] = category_coding

    def set_medication_reference(self, medication_reference: dict):
        self.payload_template['medicationReference'] = medication_reference

    def set_subject(self, subject: dict):
        self.payload_template['subject'] = subject

    def set_context(self, context: dict):
        self.payload_template['context'] = context

    def set_performer_actor(self, performer_actor: dict):
        self.payload_template['performer'][0]['actor'] = performer_actor

    def set_type_coding(self, type_coding: dict):
        self.payload_template['type']['coding'] = type_coding

    def set_quantity(self, quantity: dict):
        self.payload_template['quantity'] = quantity

    def set_days_supply(self, days_supply: dict):
        self.payload_template['daysSupply'] = days_supply

    def set_when_prepared(self, when_prepared: str):
        self.payload_template['whenPrepared'] = when_prepared

    def set_when_handed_over(self, when_handed_over: str):
        self.payload_template['whenHandedOver'] = when_handed_over

    def set_dosage_instruction(self, dosage_instruction: list):
        self.payload_template['dosageInstruction'] = dosage_instruction

    def set_substitution_was_substituted(self, was_substituted: bool):
        self.payload_template['substitution']['wasSubstituted'] = was_substituted

    def set_substitution_type_coding(self, substitution_type_coding: list):
        self.payload_template['substitution']['type']['coding'] = substitution_type_coding

    def set_substitution_reason_coding(self, substitution_reason_coding: list):
        self.payload_template['substitution']['reason'][0]['coding'] = substitution_reason_coding

    def create(self):
        return self.payload_template

    def build_medication_dispense_id_query(self, medication_dispense_id: str):
        return urlencode({'_id': medication_dispense_id})

    def build_search_param(self, query_params: dict):
        return urlencode(query_params)
