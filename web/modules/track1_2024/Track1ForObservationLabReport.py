import re
from fhir_data_generator import TWCoreObservationLabReport as Observation
from fhir_data_generator import SimpleClient, ClientCredentials, AuthorizationCode


class Track1ForObservationLabReport:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.payload = item_dict['patient_payload']
        self.http_method = 'POST'
        if item_dict['patient_payload'].get('id') is not None:
            self.http_method = 'PUT'
        self.resource = re.findall(r'Observation', resource)[0]

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

        json_payload = self.generate_observation_resource()

        req_path = f'/{self.resource}'
        if self.http_method == 'PUT':
            observation_id = self.payload['id']
            req_path = f'/{self.resource}/{observation_id}'

        response = simple_client.send(
            path=req_path,
            http_method=self.http_method.lower(),
            headers=simple_client.headers,
            json_payload=json_payload
        )

        return simple_client.handle_response(response)

    def generate_observation_resource(self):
        if self.http_method == 'PUT':
            observation_class = Observation(self.payload['id'])
        else:
            observation_class = Observation()

        profile_urls = self.payload['profile_urls']
        observation_class.set_profile_urls(profile_urls)

        # Temporary deleting  profile_urls
        if 'dicom' in self.item_dict['fhir_server']:
            del observation_class.payload_template['meta']

        observation_class.set_status(self.payload['status'])

        observation_class.set_category_coding(self.payload['category_coding'])

        observation_class.set_code_coding(self.payload['code_coding'])
        observation_class.set_code_text(self.payload['code_text'])

        observation_class.set_subject(self.payload['subject'])

        observation_class.set_effective_datetime(self.payload['effective_datetime'])

        observation_class.set_performer(self.payload['performer'])

        observation_class.set_value_quantity(self.payload['value_quantity'])

        observation_class.create()

        return observation_class.payload_template
