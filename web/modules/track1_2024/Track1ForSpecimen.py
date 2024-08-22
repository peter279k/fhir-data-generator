from fhir_data_generator import TWCoreSpecimen as Specimen
from fhir_data_generator import SimpleClient, ClientCredentials, AuthorizationCode


class Track1ForSpecimen:
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

        json_payload = self.generate_specimen_resource()

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

    def generate_specimen_resource(self):
        if self.http_method == 'PUT':
            specimen_class = Specimen(self.payload['id'])
        else:
            specimen_class = Specimen()

        profile_urls = self.payload['profile_urls']

        specimen_class.set_profile_urls(profile_urls)

        specimen_class.set_identifier(self.payload['identifier'])

        specimen_class.set_accession_identifier(self.payload['accession_identifier'])

        specimen_class.set_status(self.payload['status'])

        specimen_class.set_type_coding(self.payload['type_coding'])

        specimen_class.set_subject(self.payload['subject'])

        specimen_class.set_received_time(self.payload['received_time'])

        specimen_class.set_collection_collector(self.payload['collection_collector'])
        specimen_class.set_collection_collected_date_time(self.payload['collection_collected_date_time'])
        specimen_class.set_collection_quantity(self.payload['collection_quantity'])
        specimen_class.set_collection_method_coding(self.payload['collection_method_coding'])
        specimen_class.set_collection_method_text(self.payload['collection_method_text'])
        specimen_class.set_collection_body_site_coding(self.payload['collection_body_site_coding'])
        specimen_class.set_collection_body_site_text(self.payload['collection_body_site_text'])
        specimen_class.set_collection_fasting_status_codeable_concept_coding(self.payload['collection_fasting_status_codeable_concept_coding'])

        specimen_class.set_processing(self.payload['processing'])

        specimen_class.set_container(self.payload['container'])

        specimen_class.set_note(self.payload['note'])

        specimen_class.create()

        return specimen_class.payload_template
