from item_models.track1_2024 import *
from item_models.track2_2024 import *
from fastapi.responses import JSONResponse
from modules.track2_2024.Track2ForSource import Track2ForSource
from modules.track1_2024.Track1ForPatient import Track1ForPatient
from modules.track2_2024.Track2ForConsumer import Track2ForConsumer
from modules.track1_2024.Track1ForEncounter import Track1ForEncounter
from modules.track1_2024.Track1ForPractitioner import Track1ForPractitioner
from modules.track1_2024.Track1ForOrganization import Track1ForOrganization
from modules.track1_2024.Track1ForPractitionerRole import Track1ForPractitionerRole
from modules.track1_2024.Track1ForAllergyIntolerance import Track1ForAllergyIntolerance


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

def track1_source_creator(item: ContentSourceModel, resource_name):
    if resource_name == 'Patient':
        track = Track1ForPatient(resource_name, item.model_dump())
    if resource_name == 'Organization':
        track = Track1ForOrganization(resource_name, item.model_dump())
    if resource_name == 'Practitioner':
        track = Track1ForPractitioner(resource_name, item.model_dump())
    if resource_name == 'PractitionerRole':
        track = Track1ForPractitionerRole(resource_name, item.model_dump())
    if resource_name == 'Encounter':
        track = Track1ForEncounter(resource_name, item.model_dump())
    if resource_name == 'AllergyIntolerance':
        track = Track1ForAllergyIntolerance(resource_name, item.model_dump())

    return JSONResponse(content=track.get_response_content())
