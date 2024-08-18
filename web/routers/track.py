from item_models.track2_2024 import *
from fastapi.responses import JSONResponse
from modules.track2_2024.Track2ForSource import Track2ForSource
from modules.track2_2024.Track2ForConsumer import Track2ForConsumer


def pat_content_consumer(item: ContentConsumerScenario1Model, current_form_name):
    if current_form_name == 'pat-consumer-sc1-json-2023-form':
        track = Track2ForConsumer(current_form_name, item.model_dump())
    elif current_form_name == 'pat-consumer-sc2-json-2023-form':
        track = Track2ForConsumer(current_form_name, item.model_dump())
    elif current_form_name == 'pat-consumer-sc3-json-2023-form':
        track = Track2ForConsumer(current_form_name, item.model_dump())

    return JSONResponse(content=track.get_response_content())

def pat_source_consumer(item: ContentSourceScenario1Model, current_form_name):
    if current_form_name == 'pat-source-sc1-json-2023-form':
        track = Track2ForSource(current_form_name, item.model_dump())
    elif current_form_name == 'pat-source-sc2-json-2023-form':
        track = Track2ForSource(current_form_name, item.model_dump())
    elif current_form_name == 'pat-source-sc3-json-2023-form':
        track = Track2ForSource(current_form_name, item.model_dump())

    return JSONResponse(content=track.get_response_content())

def delete_pat_source_consumer(item: DeleteContentSourceScenario1Model, current_form_name):
    if current_form_name == 'pat-source-sc1-json-2023-form':
        track = Track2ForSource(current_form_name, item.model_dump(), True)
    elif current_form_name == 'pat-source-sc2-json-2023-form':
        track = Track2ForSource(current_form_name, item.model_dump(), True)
    elif current_form_name == 'pat-source-sc3-json-2023-form':
        track = Track2ForSource(current_form_name, item.model_dump(), True)

    return JSONResponse(content=track.delete_resource())
