from fhir_data_generator import TWCoreAllergyIntoleranceNut as AllergyIntolerance
from fhir_data_generator import SimpleClient, ClientCredentials, AuthorizationCode


class Track1ForAllergyIntolerance:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.payload = item_dict['patient_payload']
        self.http_method = 'POST'
        if item_dict['patient_payload'].get('id') is not None:
            self.http_method = 'PUT'
        self.resource = resource

    def get_response_content(self):
        oauth_level = self.item_dict.get('oauth_level')
        req_url = self.item_dict.get('fhir_server')
        simple_client = SimpleClient(req_url)

        oauth_token_info = self.item_dict.get('oauth_token_info')
        client_id = oauth_token_info['client_id']
        client_secret = oauth_token_info['client_secret']
        token_url = oauth_token_info['token_url']
        authorization_code_url = oauth_token_info['authorization_code_url']
        redirect_callback_url = oauth_token_info['redirect_callback_url']
        username = oauth_token_info['username']
        password = oauth_token_info['password']

        if oauth_level == 'level1':
            client_credentials = ClientCredentials(
                client_id=client_id,
                client_secret=client_secret,
                req_url=token_url
            )
            client_credentials.send()
            access_token = client_credentials.retrieve_token()
            simple_client.headers['Authorization'] = f'Bearer {access_token}'
        elif oauth_level == 'level3':
            authorization_code = AuthorizationCode(
                client_id=client_id,
                client_secret=client_secret,
                redirect_uri=redirect_callback_url,
                req_auth_code_url=authorization_code_url,
                access_token_req_url=token_url,
                form_action_payload={'username': username, 'password': password},
            )
            authorization_code.retrieve_authorization_code()
            authorization_code.send()
            access_token = authorization_code.retrieve_token()
            simple_client.headers['Authorization'] = f'Bearer {access_token}'

        json_payload = self.generate_allergy_intolerance_resource()

        req_path = f'/{self.resource}'
        if self.http_method == 'PUT':
            practitioner_role_id = self.payload['id']
            req_path = f'/{self.resource}/{practitioner_role_id}'

        response = simple_client.send(
            path=req_path,
            http_method=self.http_method.lower(),
            headers=simple_client.headers,
            json_payload=json_payload
        )

        return simple_client.handle_response(response)

    def generate_allergy_intolerance_resource(self):
        if self.http_method == 'PUT':
            allergy_intolerance_class = AllergyIntolerance(self.payload['id'])
        else:
            allergy_intolerance_class = AllergyIntolerance()

        profile_urls = self.payload['profile_urls']

        allergy_intolerance_class.set_profile_urls(profile_urls)

        allergy_intolerance_class.set_clinical_status_coding(self.payload['clinical_status_coding'])
        allergy_intolerance_class.set_clinical_status_text(self.payload['clinical_status_text'])

        allergy_intolerance_class.set_verification_status_coding(self.payload['verification_status_coding'])
        allergy_intolerance_class.set_verification_status_text(self.payload['verification_status_text'])

        allergy_intolerance_class.set_category(self.payload['category'])

        allergy_intolerance_class.set_criticality(self.payload['criticality'])

        allergy_intolerance_class.set_code_coding(self.payload['code_coding'])
        allergy_intolerance_class.set_code_text(self.payload['code_text'])

        allergy_intolerance_class.set_patient(self.payload['patient'])
        allergy_intolerance_class.set_onset_datetime(self.payload['onset_datetime'])
        allergy_intolerance_class.set_recorded_date(self.payload['recorded_date'])
        allergy_intolerance_class.set_recorder(self.payload['recorder'])
        allergy_intolerance_class.set_asserter(self.payload['asserter'])
        allergy_intolerance_class.set_last_occurrence(self.payload['last_occurrence'])
        allergy_intolerance_class.set_note(self.payload['note'])

        allergy_intolerance_class.set_reaction_description(self.payload['reaction_description'])
        allergy_intolerance_class.set_reaction_severity(self.payload['reaction_severity'])
        allergy_intolerance_class.set_reaction_exposure_route_text(self.payload['reaction_exposure_route_text'])
        allergy_intolerance_class.set_reaction_note(self.payload['reaction_note'])

        allergy_intolerance_class.create()

        return allergy_intolerance_class.payload_template
