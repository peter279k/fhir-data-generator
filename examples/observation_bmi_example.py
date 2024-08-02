import json
import uuid
from fhir_data_generator import Observation


observation = Observation(str(uuid.uuid4()))

profile_urls = ['https://fhir.server/path/to/profile/path']
observation.set_profile_urls(profile_urls)

status = 'final'
observation.set_status(status)

category_coding = [{
    'system': 'http://terminology.hl7.org/CodeSystem/observation-category',
    'code': 'vital-signs',
    'display': 'Vital Signs',
}]
observation.set_category_coding(category_coding)

code_coding = [{
    'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/loinc-tw',
    'code': '39156-5',
    'display': 'Body mass index (BMI) [Ratio]',
}]
observation.set_code_coding(code_coding)

code_text = 'Body mass index (BMI) [Ratio]'
observation.set_code_text(code_text)

subject= {
    'reference': 'Patient/pat-example',
}
observation.set_subject(subject)

effective_datetime = '2023-12-23'
observation.set_effective_datetime(effective_datetime)

performer = [{
    'reference': 'Practitioner/pra-dr-example',
}]
observation.set_performer(performer)

value_quantity = {
    'value': 18.3,
    'unit': 'kg/m2',
    'system': 'http://unitsofmeasure.org',
    'code': 'kg/m2',
}
observation.set_value_quantity(value_quantity)

# Retrieving the Observation resource dict
observation_json_dict = observation.create()
print(observation_json_dict)

# Retrieve the Observation resource JSON string
print(json.dumps(observation_json_dict))
