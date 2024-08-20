import base64
from fhir_data_generator import TWCorePractitionerRole as PractitionerRole
from fhir_data_generator import SimpleClient, ClientCredentials, AuthorizationCode


class Track1ForPractitionerRole:
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

        json_payload = self.generate_practitioner_role_resource()

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

    def generate_practitioner_role_resource(self):
        if self.http_method == 'PUT':
            practitioner_role_class = PractitionerRole(self.payload['id'])
        else:
            practitioner_role_class = PractitionerRole()

        profile_urls = self.payload['profile_urls']
        practitioner_role_class.set_profile_urls(profile_urls)

        practitioner_role_class.set_identifiers(self.payload['identifiers'])

        practitioner_role_class.set_active(self.payload['active'])

        practitioner_role_class.set_period(self.payload['period'])

        practitioner_role_class.set_practitioner(self.payload['practitioner'])

        practitioner_role_class.set_specialty_coding(self.payload['specialty_coding'])

        practitioner_role_class.set_code(self.payload['code'])

        practitioner_role_class.set_location(self.payload['location'])

        practitioner_role_class.set_telecom(self.payload['telecom'])

        practitioner_role_class.set_available_time(self.payload['available_time'])

        practitioner_role_class.set_not_available(self.payload['not_available'])

        practitioner_role_class.set_availability_exceptions(self.payload['availability_exceptions'])

        return practitioner_role_class.payload_template
