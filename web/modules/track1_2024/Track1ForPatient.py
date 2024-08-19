import json
import base64
from fhir_data_generator import TWCorePatient as Patient
from fhir_data_generator import SimpleClient, ClientCredentials, AuthorizationCode


class Track1ForPatient:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.patient_payload = item_dict['patient_payload']
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

        json_payload = self.generate_patient_resource()

        req_path = f'/{self.resource}'
        if self.http_method == 'PUT':
            patient_id = self.patient_payload['id']
            req_path = f'/{self.resource}/{patient_id}'

        response = simple_client.send(
            path=req_path,
            http_method=self.http_method.lower(),
            headers=simple_client.headers,
            json_payload=json_payload
        )

        return simple_client.handle_response(response)

    def generate_patient_resource(self):
        if self.http_method == 'PUT':
            patient_class = Patient(self.patient_payload['id'])
        else:
            patient_class = Patient()

        profile_urls = self.patient_payload['profile_urls']
        patient_class.set_profile_urls(profile_urls)

        extension_url = self.patient_payload['extension_url']
        patient_class.set_extension_url(extension_url)

        extension_value_age = self.patient_payload['extension_value_age']
        patient_class.set_extension_value_age(extension_value_age)

        extension_extension_coding= self.patient_payload['extension_extension_coding']
        patient_class.set_extension_extension_coding(extension_extension_coding)

        extension_extension_url = self.patient_payload['extension_extension_url']
        patient_class.set_extension_extension_url(extension_extension_url)

        identifiers = self.patient_payload['identifiers']
        patient_class.set_identifiers(identifiers)

        active = self.patient_payload['active']
        patient_class.set_active(active)

        name_use = self.patient_payload['name_use']
        patient_class.set_name_use(name_use)

        name_text = self.patient_payload['name_text']
        patient_class.set_name_text(name_text)

        name_family = self.patient_payload['name_family']
        patient_class.set_name_family(name_family)

        name_given = self.patient_payload['name_given']
        patient_class.set_name_given(name_given)

        telecom = self.patient_payload['telecom']
        patient_class.set_telecom(telecom)

        gender = self.patient_payload['gender']
        patient_class.set_gender(gender)

        birth_date = self.patient_payload['birth_date']
        patient_class.set_birth_date(birth_date)

        address_extension = self.patient_payload['address_extension']
        patient_class.set_address_extension(address_extension)

        address_text = self.patient_payload['address_text']
        patient_class.set_address_text(address_text)

        address_line = self.patient_payload['address_line']
        patient_class.set_address_line(address_line)

        address_city = self.patient_payload['address_city']
        patient_class.set_address_city(address_city)

        address_district = self.patient_payload['address_district']
        patient_class.set_address_district(address_district)

        address_postal_code_extension = self.patient_payload['address_postal_code_extension']
        patient_class.set_address_postal_code_extension(address_postal_code_extension)

        marital_status_coding = self.patient_payload['marital_status_coding']
        patient_class.set_marital_status_coding(marital_status_coding)

        with open('./front_end/assets/img/patient.png', 'rb') as f:
            contents = f.read()

            encoded_image = base64.b64encode(contents)
            encoded_image = encoded_image.decode('utf-8')

        self.patient_payload['photo'][0]['data'] = encoded_image

        patient_class.set_photo(self.patient_payload['photo'])

        contact = self.patient_payload['contact']
        patient_class.set_contact(contact)

        contact_name = self.patient_payload['contact_name']
        patient_class.set_contact_name(contact_name)

        contact_telecom = self.patient_payload['contact_telecom']
        patient_class.set_contact_telecom(contact_telecom)

        communication_language_coding = self.patient_payload['communication_language_coding']
        patient_class.set_communication_language_coding(communication_language_coding)

        managing_organization = self.patient_payload['managing_organization']
        patient_class.set_managing_organization(managing_organization)

        patient_class.create()

        with open('patient.json', mode='w') as f:
            f.write(json.dumps(patient_class.payload_template))

        return patient_class.payload_template
