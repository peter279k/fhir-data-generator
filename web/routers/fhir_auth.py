import os
import requests
from dotenv import load_dotenv
from fastapi import Path, Depends
from urllib.parse import urlencode
from fastapi.requests import Request
from fastapi.responses import Response, JSONResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


load_dotenv()
auth_scheme = HTTPBearer()


async def handle_request(request: Request, resource: str, token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    auth_response = auth_sport_data_jwt(token.credentials)
    if auth_response.status_code != 200:
        return JSONResponse({
            'status': auth_response.status_code,
            'message': 'Authenticating JWT is failed.',
            'data': [auth_response.json()],
        }, status_code=auth_response.status_code)

    resource_id = ''

    return by_pass_to_fhir_server(request.method.lower(), resource, resource_id, request.query_params, request.headers)

async def handle_request_on_resource_id(request: Request, resource: str, resource_id: str, token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    auth_response = auth_sport_data_jwt(token.credentials)
    if auth_response.status_code != 200:
        return JSONResponse({
            'status': auth_response.status_code,
            'message': 'Authenticating JWT is failed.',
            'data': [auth_response.json()],
        }, status_code=auth_response.status_code)

    return by_pass_to_fhir_server(request.method.lower(), resource, resource_id, request.query_params, request.headers)

def auth_sport_data_jwt(jwt_token: str):
    headers = {
        'Accept': 'applicaiton/json',
        'Authorization': f'Bearer {jwt_token}',
    }

    query_params = urlencode({
        'main_type': 'Sport',
        'type': 'Run',
        'data_size': '1',
    })
    sport_data_api_endpoint = os.getenv('sport_data_api_endpoint', '')
    request_url = f'{sport_data_api_endpoint}/data/processed?{query_params}'
    response = requests.get(request_url, headers=headers)

    return response

def by_pass_to_fhir_server(method: str, resource: str, resource_id: str, query_params: dict, headers: dict):
    if method == 'get':
        fhir_server_endpoint = os.getenv('fhir_server_endpoint')
        fhir_server_url = f'{fhir_server_endpoint}/{resource}'
        if resource_id != '':
            fhir_server_url = f'{fhir_server_endpoint}/{resource}/{resource_id}'

        if len(query_params.keys()) != 0:
            fhir_server_url += f'?{urlencode(query_params)}'

        headers = {
            'Accept': headers.get('Accept', 'application/fhir+json'),
            'Content-Type': headers.get('Content-Type', 'application/fhir+json'),
        }
        response = requests.get(fhir_server_url, headers=headers)

        return Response(
            content=response.text,
            status_code=response.status_code,
            media_type='application/fhir+json'
        )
    else:
        status_code = 405

        return Response(content={
            'status': status_code,
            'message': f'The {method.upper()} method is not allowed',
            'data': [],
        }, status_code=status_code, media_type='application/json')
