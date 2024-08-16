import os

from dotenv import load_dotenv
from fastapi.responses import JSONResponse

load_dotenv()


async def read_root():
    status_code = 200
    version = os.getenv('version')

    if version is None:
        version = 'Unknown'

    return JSONResponse({
        'status': status_code,
        'message': '取得版本成功',
        'data': [
            {
                'version': version,
            },
        ],
    }, status_code=status_code)
