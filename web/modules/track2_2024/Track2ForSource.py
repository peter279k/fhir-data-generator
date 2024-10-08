from fhir_data_generator import Patient
from fhir_data_generator import SimpleClient, ClientCredentials, AuthorizationCode


class Track2ForSource:
    def __init__(self, current_form_name: str, item_dict: dict, to_delete=False):
        self.current_form_name = current_form_name
        self.item_dict = item_dict
        self.resource = '/Patient'
        self.patient_payload = item_dict.get('patient_payload')
        self.to_delete = to_delete

        self.http_method = 'PUT'
        if to_delete is False and self.patient_payload.get('id') is None:
            self.http_method = 'POST'

    def delete_resource(self):
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

        patient_id = self.item_dict['patient_id']
        req_path = f'{self.resource}/{patient_id}'
        self.http_method = 'DELETE'

        response = simple_client.send(
            path=req_path,
            http_method=self.http_method.lower(),
            headers=simple_client.headers
        )

        return simple_client.handle_response(response)

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

        json_payload = self.generate_patient_resource()

        req_path = f'{self.resource}'
        if self.http_method == 'PUT':
            patient_id = self.patient_payload['id']
            req_path = f'{self.resource}/{patient_id}'

        response = simple_client.send(
            path=req_path,
            http_method=self.http_method.lower(),
            headers=simple_client.headers,
            json_payload=json_payload
        )

        return simple_client.handle_response(response)

    def generate_patient_resource(self):
        if self.http_method == 'PUT':
            patient = Patient(self.patient_payload['id'])
        else:
            patient = Patient()

        patient.set_profile_url(self.patient_payload['profile_url'])

        scenario = 1

        for identifier_info in self.patient_payload['identifiers']:
            patient.set_identifier(identifier_info)

        if len(self.patient_payload['communications']) > 0 and self.patient_payload.get('contact') is None:
            scenario = 2
        else:
            scenario = 3

        for communication_info in self.patient_payload['communications']:
            patient.set_communication(communication_info)

        patient.set_active(bool(self.patient_payload['active']))
        patient.set_managing_organization(self.patient_payload['managing_organization'])
        patient.set_name(self.patient_payload['name'])
        patient.set_gender(self.patient_payload['gender'])
        patient.set_birth_date(self.patient_payload['birth_date'])

        if scenario == 3:
            patient.set_address(self.patient_payload['addresses'][0])
            patient.set_contact(self.patient_payload['contact'][0])

        else:
            patient.set_address(self.patient_payload['addresses'][0])
            patient.set_address(self.patient_payload['addresses'][1])
            for telecom_val in self.patient_payload['telecom']:
                patient.set_telecom(telecom_val)

        if self.http_method == 'PUT':
            return patient.create(scenario, update=True)

        return patient.create(scenario)
