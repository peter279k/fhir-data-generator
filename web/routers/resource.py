import os
import sqlite3
from fastapi.responses import JSONResponse


def resource_handler():
    db_path = 'resource_log.sqlite3'
    if os.path.isfile(db_path) is False:
        response = {
            'status': 200,
            'data': [],
            'message': f'The SQLite3 {db_path} file is not found.',
        }
        return JSONResponse(status_code=200, content=response)

    sql = '''
        SELECT DISTINCT connect_name FROM resources
    '''
    with sqlite3.connect('resource_log.sqlite3') as db:
        result = db.execute(sql)
        rows = result.fetchall()
        result.close()

    response = {
        'status': 200,
        'data': [],
        'message': 'Query data is successful.',
    }

    for record in rows:
        response['data'] += record[0],

    return JSONResponse(status_code=200, content=response)

def query_resource_handler(connect_name):
    db_path = 'resource_log.sqlite3'
    if os.path.isfile(db_path) is False:
        response = {
            'status': 200,
            'data': [],
            'message': f'The SQLite3 {db_path} file is not found.',
        }
        return JSONResponse(status_code=200, content=response)

    sql = '''
        SELECT track_number, resource_name, resource_id, fhir_server_endpoint
        FROM resources WHERE connect_name = ?
    '''
    with sqlite3.connect('resource_log.sqlite3') as db:
        result = db.execute(sql, [connect_name])
        rows = result.fetchall()
        result.close()

    response = {
        'status': 200,
        'data': [],
        'message': 'Query data is successful.',
    }

    for record in rows:
        response['data'] += {
            'track_number': record[0],
            'resource_name': record[1],
            'resource_id': record[2],
            'fhir_server_endpoint': record[3],
        },

    return JSONResponse(status_code=200, content=response)
