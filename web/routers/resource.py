import os
import sqlite3
from fastapi.responses import JSONResponse


def resource_handler():
    db_path = 'resource_log.sqlite3'
    if os.path.isfile(db_path) is False:
        response = {
            'status': 400,
            'data': [],
            'message': f'The SQLite3 {db_path} file is not found.',
        }
        return JSONResponse(status_code=400, content=response)

    response = {
        'status': 200,
        'data': {
            'fhir-lists': [],
            'connect-activity': [],
            'track-lists': [],
            'resource-lists': [],
        },
        'message': 'Query data is successful.',
    }

    data_mapping = ['connect-activity', 'track-lists', 'resource-lists', 'fhir-lists']
    tables = ['connect_name', 'track_number', 'resource_name', 'fhir_server_endpoint']
    sql = '''
        SELECT DISTINCT {} FROM resources
    '''
    with sqlite3.connect('resource_log.sqlite3') as db:
        for index,table_name in enumerate(tables):
            result = db.execute(sql.format(table_name))
            rows = result.fetchall()
            result.close()

            for record in rows:
                response['data'][data_mapping[index]] += record[0],

    return JSONResponse(status_code=200, content=response)

def query_resource_handler(fhir_lists: str = '', connect_activity: str = '', track_lists: int = 1, resource_lists: str = ''):
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
        FROM resources
        WHERE
        fhir_server_endpoint = ? AND
        connect_name = ? AND
        track_number = ? AND
        resource_name = ?
    '''
    with sqlite3.connect('resource_log.sqlite3') as db:
        result = db.execute(sql, [
            fhir_lists,
            connect_activity,
            track_lists,
            resource_lists,
        ])
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
