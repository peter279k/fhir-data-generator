from item_models.track2_2024 import *
from fastapi.responses import JSONResponse
from modules.track2_2024.Track2ForConsumer import Track2ForConsumer


def pat_content_consumer(item: ContentConsumerScenario1Model, current_form_name):
    if current_form_name == 'pat-consumer-sc1-json-2023-form':
        track = Track2ForConsumer(current_form_name, item.model_dump())
    elif current_form_name == 'pat-consumer-sc2-json-2023-form':
        track = Track2ForConsumer(current_form_name, item.model_dump())
    elif current_form_name == 'pat-consumer-sc3-json-2023-form':
        track = Track2ForConsumer(current_form_name, item.model_dump)

    return JSONResponse(content=track.get_response_content())