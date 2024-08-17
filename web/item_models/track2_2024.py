from typing import Dict
from pydantic import BaseModel


class ContentConsumerScenario1Model(BaseModel):
    fhir_server: str
    oauth_token_info: Dict
    oauth_level: str
    search_parameters: str

class ContentSourceScenario1Model(BaseModel):
    fhir_server: str
    oauth_token_info: Dict
    oauth_level: str
    patient_payload: Dict
