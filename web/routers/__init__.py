from .info import *
from .track import *
from .resource import *
from fastapi import APIRouter


info_router = APIRouter(tags=['API版本資訊'])
info_router.add_api_route('/', read_root, methods=['GET'], description='取得該API服務版本', summary='API版本')

track_router = APIRouter(tags=['各式Track'])
track_router.add_api_route('/track2/2024/{current_form_name}', pat_content_consumer, methods=['POST'], description='Track2 2024相關', summary='Track2')
track_router.add_api_route('/track2/2024/source/{current_form_name}', pat_source_consumer, methods=['POST'], description='Track2 2024相關', summary='Track2')
track_router.add_api_route('/track2/2024/delete_source/{current_form_name}', delete_pat_source_consumer, methods=['POST'], description='Track2 2024相關', summary='Track2')

track_router.add_api_route('/track1/2024/source/{resource_name}', track1_source_creator, methods=['POST'], description='Track1 2024相關', summary='Track1')
track_router.add_api_route('/track1/2024/consumer/{resource_name}', track1_consumer, methods=['POST'], description='Track1 2024相關', summary='Track1')

track_router.add_api_route('/track13/2024/source/{resource_name}', track13_source_creator, methods=['POST'], description='Track13 2024相關', summary='Track13')
track_router.add_api_route('/track13/2024/consumer/{resource_name}', track13_consumer, methods=['POST'], description='Track13 2024相關', summary='Track13')

resource_log_router = APIRouter(tags=['Resource log'])
resource_log_router.add_api_route('/resources/option_lists', resource_handler, methods=['GET'], description='取得聯測松年度列表', summary='Resource log')
resource_log_router.add_api_route('/resources/query/', query_resource_handler, methods=['GET'], description='取得聯測松年度列表', summary='Resource log')
