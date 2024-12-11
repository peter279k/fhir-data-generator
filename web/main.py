import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()

from routers import *
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


description = '''
MITW Track API

## Features功能特性

1. MITW 2024 Track #1, #2, and #13
2. FHIR Authentication Service for Golden Smart Home

'''

async def initial_sqlite3_db():
    sql = '''
        CREATE TABLE IF NOT EXISTS resources(
            id INTEGER NOT NULL PRIMARY KEY,
            connect_name VARCHAR(50) NOT NULL,
            track_number INTEGER NOT NULL,
            resource_name VARCHAR(30) NOT NULL,
            resource_id VARCHAR(100) NOT NULL,
            fhir_server_endpoint VARCHAR(100) NOT NULL,
            oauth_level VARCHAR(20) NOT NULL
        )
    '''
    with sqlite3.connect(f'./resource_log.sqlite3') as db:
        db.execute(sql)

    db.close()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await initial_sqlite3_db()
    yield

app = FastAPI(
    title='MITW Track API',
    description=description,
    version=os.getenv('version'),
    contact={
        'name': 'Peter Li',
        'email': 'peter279k@gmail.com',
    },
    lifespan=lifespan
)

app.mount('/front_end', StaticFiles(directory='front_end'), name='front_end')
app.include_router(info_router)
app.include_router(track_router)
app.include_router(resource_log_router)
app.include_router(fhir_sport_data_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    expose_headers=['Auth-Session', 'X-Token'],
)
