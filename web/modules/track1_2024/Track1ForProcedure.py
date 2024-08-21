from fhir_data_generator import TWCoreProcedure as Procedure
from fhir_data_generator import SimpleClient, ClientCredentials, AuthorizationCode


class Track1ForProcedure:
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

        json_payload = self.generate_procedure_resource()

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

    def generate_procedure_resource(self):
        if self.http_method == 'PUT':
            procedure_class = Procedure(self.payload['id'])
        else:
            procedure_class = Procedure()

        profile_urls = self.payload['profile_urls']

        procedure_class.set_profile_urls(profile_urls)

        procedure_class.set_status(self.payload['status'])

        procedure_class.set_code_coding(self.payload['code_coding'])
        procedure_class.set_code_text(self.payload['code_text'])

        procedure_class.set_subject(self.payload['subject'])

        procedure_class.set_performed_date_time(self.payload['performed_date_time'])

        procedure_class.set_asserter(self.payload['asserter'])

        procedure_class.set_performer(self.payload['performer'])

        procedure_class.set_body_site_coding(self.payload['body_site_coding'])

        procedure_class.create()

        return procedure_class.payload_template
