import os

from dotenv import load_dotenv

load_dotenv()

from routers import *
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


description = '''
MITW Track API

## Features功能特性

1. MITW 2024 Track #1, #2, and #13

'''

app = FastAPI(
    title='MITW Track API',
    description=description,
    version=os.getenv('version'),
    contact={
        'name': 'Peter Li',
        'email': 'peter279k@gmail.com',
    },
)

app.mount('/front_end', StaticFiles(directory='front_end'), name='front_end')
app.include_router(info_router)
app.include_router(track_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    expose_headers=['Auth-Session', 'X-Token'],
)
