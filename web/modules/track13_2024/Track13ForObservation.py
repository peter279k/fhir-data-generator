import re
import json
from fhir_data_generator import PhysicalActivityObservation as Observation
from fhir_data_generator import SimpleClient, ClientCredentials, AuthorizationCode


class Track13ForObservation:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.payload = item_dict['patient_payload']
        self.component_form = [
            'gaitcycle-r',
            'gaitcycle-l',
            'weighttraining',
            'gaittype-l',
            'gaittype-r',
            'treadmill',
            'bloodpressure',
        ]
        self.concept_form = ['gaittype-l', 'gaittype-r', 'weighttraining']
        self.has_member_form = 'tbw'
        self.body_site_form = ['gaitcycle-r', 'gaitcycle-l', 'gaittype-l', 'gaittype-r']
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

        observation_class.set_status(self.payload['status'])

        observation_class.set_category_coding(self.payload['category_coding'])

        observation_class.set_code_coding(self.payload['code_coding'])
        observation_class.set_code_text(self.payload['code_text'])

        observation_class.set_subject(self.payload['subject'])

        observation_class.set_effective_datetime(self.payload['effective_datetime'])

        observation_class.set_performer(self.payload['performer'])

        if self.payload['type'] in self.component_form:
            observation_class.set_component(self.payload['component'])
        if self.payload['type'] in self.concept_form:
            observation_class.set_value_codeable_concept(self.payload['value_codeable_concept'])
        if self.payload['type'] == self.has_member_form:
            observation_class.set_has_member(self.payload['has_member'])
        if self.payload['type'] in self.body_site_form:
            observation_class.set_body_site(self.payload['body_site'])

        observation_class.create()

        file_name = self.payload['type']
        with open(f'{file_name}.json', 'w') as f:
            f.write(json.dumps(observation_class.payload_template))

        return observation_class.payload_template
