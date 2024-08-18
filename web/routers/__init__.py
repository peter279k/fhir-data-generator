from .info import *
from .track import *
from fastapi import APIRouter


info_router = APIRouter(tags=['API版本資訊'])
info_router.add_api_route('/', read_root, methods=['GET'], description='取得該API服務版本', summary='API版本')

track_router = APIRouter(tags=['各式Track'])
track_router.add_api_route('/track2/2024/{current_form_name}', pat_content_consumer, methods=['POST'], description='Track2 2024相關', summary='Track2')
track_router.add_api_route('/track2/2024/source/{current_form_name}', pat_source_consumer, methods=['POST'], description='Track2 2024相關', summary='Track2')
track_router.add_api_route('/track2/2024/delete_source/{current_form_name}', delete_pat_source_consumer, methods=['POST'], description='Track2 2024相關', summary='Track2')
