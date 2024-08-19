from typing import Dict
from pydantic import BaseModel


class ContentSourceModel(BaseModel):
    fhir_server: str
    oauth_token_info: Dict
    oauth_level: str
    patient_payload: Dict
