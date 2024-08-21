from item_models.track1_2024 import *
from item_models.track2_2024 import *
from fastapi.responses import JSONResponse
from modules.track1_2024.Track1ForMedia import Track1ForMedia
from modules.track2_2024.Track2ForSource import Track2ForSource
from modules.track1_2024.Track1ForPatient import Track1ForPatient
from modules.track1_2024.Track1ForLocation import Track1ForLocation
from modules.track2_2024.Track2ForConsumer import Track2ForConsumer
from modules.track1_2024.Track1ForCondition import Track1ForCondition
from modules.track1_2024.Track1ForEncounter import Track1ForEncounter
from modules.track1_2024.Track1ForProcedure import Track1ForProcedure
from modules.track1_2024.Track1ForMedication import Track1ForMedication
from modules.track1_2024.Track1ForPractitioner import Track1ForPractitioner
from modules.track1_2024.Track1ForOrganization import Track1ForOrganization
from modules.track1_2024.Track1ForImagingStudy import Track1ForImagingStudy
from modules.track1_2024.Track1ForPractitionerRole import Track1ForPractitionerRole
from modules.track1_2024.Track1ForDiagnosticReport import Track1ForDiagnosticReport
from modules.track1_2024.Track1ForMedicationRequest import Track1ForMedicationRequest
from modules.track1_2024.Track1ForDocumentReference import Track1ForDocumentReference
from modules.track1_2024.Track1ForMedicationDispense import Track1ForMedicationDispense
from modules.track1_2024.Track1ForAllergyIntolerance import Track1ForAllergyIntolerance
from modules.track1_2024.Track1ForMedicationStatement import Track1ForMedicationStatement


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
    if resource_name == 'Condition':
        track = Track1ForCondition(resource_name, item.model_dump())
    if resource_name == 'DiagnosticReport':
        track = Track1ForDiagnosticReport(resource_name, item.model_dump())
    if resource_name == 'DocumentReference':
        track = Track1ForDocumentReference(resource_name, item.model_dump())
    if resource_name == 'ImagingStudy':
        track = Track1ForImagingStudy(resource_name, item.model_dump())
    if resource_name == 'Location':
        track = Track1ForLocation(resource_name, item.model_dump())
    if resource_name == 'Media':
        track = Track1ForMedia(resource_name, item.model_dump())
    if resource_name == 'Medication':
        track = Track1ForMedication(resource_name, item.model_dump())
    if resource_name == 'MedicationRequest':
        track = Track1ForMedicationRequest(resource_name, item.model_dump())
    if resource_name == 'MedicationDispense':
        track = Track1ForMedicationDispense(resource_name, item.model_dump())
    if resource_name == 'MedicationStatement':
        track = Track1ForMedicationStatement(resource_name, item.model_dump())
    if resource_name == 'Procedure':
        track = Track1ForProcedure(resource_name, item.model_dump())

    return JSONResponse(content=track.get_response_content())
