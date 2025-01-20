import json
import requests


client_id = 'admin-cli'

def password_login():
    client_id = 'admin-cli'
    username = 'admin'
    password = 'admin'
    grant_type = 'password'

    req_url = 'http://localhost:8080/realms/master/protocol/openid-connect/token'

    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}
    payload = f'client_id={client_id}&username={username}&password={password}&grant_type={grant_type}'

    print('Retrieving the legacy access token with the grant_type password...')

    response = requests.post(req_url, headers=headers, data=payload)

    if response.status_code != 200:
        raise Exception(f'{response.text}')


    legacy_access_token = response.json()['access_token']

    return legacy_access_token


legacy_access_token = password_login()
req_url = 'http://localhost:8080/admin/realms/master/clients?first=0&max=11'
headers = {'Accept': 'application/json', 'Authorization': f'Bearer {legacy_access_token}'}


print('Retrieving the use client info...')

response = requests.get(req_url, headers=headers)
if response.status_code != 200:
    raise Exception(f'{response.text}')


res_json = response.json()
client_info_id = None
for client_info in res_json:
    if client_info['clientId'] == client_id:
        client_info_id = client_info['id']
        break

if client_info_id is None:
    raise Exception('Retrieving the use client info is failed!')


req_url = f'http://localhost:8080/admin/realms/master/clients/{client_info_id}'

print('Updating client credentials....')

headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {legacy_access_token}',
    'Content-Type': 'application/json',
}
payload = {
    'id': client_info_id,
    'clientId': client_id,
    'name': '${client_admin-cli}',
    'surrogateAuthRequired': False,
    'enabled': True,
    'alwaysDisplayInConsole': False,
    'clientAuthenticatorType': 'client-secret',
    'redirectUris': ['*'],
    'webOrigins': [],
    'notBefore': 0,
    'bearerOnly': False,
    'consentRequired': False,
    'standardFlowEnabled': True,
    'implicitFlowEnabled': False,
    'directAccessGrantsEnabled': True,
    'serviceAccountsEnabled': True,
    'publicClient': False,
    'frontchannelLogout': False,
    'protocol': 'openid-connect',
    'attributes': {
        'oauth2.device.authorization.grant.enabled': False,
        'oidc.ciba.grant.enabled': False,
        'login_theme': '',
        'display.on.consent.screen': 'false',
        'consent.screen.text': '',
        'backchannel.logout.url': '',
        'backchannel.logout.session.required': 'true',
        'backchannel.logout.revoke.offline.tokens': 'false'
    },
    'authenticationFlowBindingOverrides': {},
    'fullScopeAllowed': False,
    'nodeReRegistrationTimeout': 0,
    'defaultClientScopes': ['web-origins', 'acr', 'profile', 'roles', 'basic', 'email'],
    'optionalClientScopes': ['address', 'phone', 'offline_access', 'microprofile-jwt'],
    'access': {'view': True, 'configure': True, 'manage': True},
    'description': '',
    'rootUrl': '',
    'baseUrl': '',
    'adminUrl': '',
    'authorizationServicesEnabled': False
}

response = requests.put(req_url, headers=headers, data=json.dumps(payload))

if response.status_code >= 400:
    raise Exception(f'{response.text}')

print('Retrieving the client secret...')

del headers['Content-Type']
req_url = f'http://localhost:8080/admin/realms/master/clients/{client_info_id}/client-secret'
response = requests.get(req_url, headers=headers)

if response.status_code >= 400:
    raise Exception(f'{response.text}')


client_secret_path = './tests/fixtures/client_secret.txt'
resp_json = response.json()
with open(client_secret_path, mode='w', encoding='utf-8') as f:
    f.write(resp_json['value'] + '\n')

print(f'The {client_secret_path} file is saved.')
