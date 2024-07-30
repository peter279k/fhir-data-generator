# Development setup

- Running the `git clone` to clone the repository.
- Preparing for the `pipenv` environment.
- Running the `pipenv install` command to install packages.
- Running the `pipenv install -d` command to install development packages.
- Running the `pipenv run poetry install` command to install local package.
- Running the `pipenv run pytest -vv` to run unit tests.
- Running the `pipenv run pytest --cov --cov-report html` to run unit tests and generate coverage report with the HTML format. The report will be generated in the `htmlcov` directory.

# Publishing package steps

- Running the `poetry check` command to check whether everything is okay.
- Running the `poetry build` command to build archived Python package file.
- Running the `poetry config pypi-token.pypi <pypi token>` command to configure Pypi token.
- Running the `poetry publish` command to publish the Python package.

# Publish package to test-pypi

- Running the `poetry config repositories.test-pypi https://test.pypi.org/legacy/` command to configure testPypi URL.
- Running the `poetry config pypi-token.test-pypi <test_pypi_token>` command to configure testPypi token.
- Running the `poetry publish -r test-pypi` command to publish the testPypi.

# Patients Examples

## Patient SC1

```python
import json
import uuid
from fhir_data_generator import Patient


patient = Patient(str(uuid.uuid4()))
patient.set_profile_url('https://fhir.server/path/to/profile/path')

identifier1 = {
    'use': 'official',
    'system': 'http://www.boca.gov.tw',
    'type': {
        'coding': [
            {
                'system': 'http://www.boca.gov.tw',
                'code': 'PPN',
                'display': 'Passport number',
            },
        ],
    },
    'value': 'E262344368'[2:],
}
identifier2 = {
    'use': 'official',
    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
    'type': {
        'coding': [
            {
                'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                'code': 'MR',
                'display': 'Medical record number',
            },
        ]
    },
    'value': '123456789',
}
managing_organization = 'Organization/MITW.ForIdentifier'
name = {
    'use': 'official',
    'text': '李小明',
    'family': '李',
    'given': ['小明'],
}
gender = 'male'
birth_date = '2023-12-23'
addresses = [
    {
        'use': 'home',
        'text': '105台北市松山區民生東路四段133號',
    },
    {
        'country': 'TW',
    },
]
scenario = 1
telecom = {
    'use': 'home',
    'system': 'phone',
    'value': '0905285349',
}

patient.set_identifier(identifier1)
patient.set_identifier(identifier2)
patient.set_active(True)
patient.set_managing_organization(managing_organization)
patient.set_name(name)
patient.set_gender(gender)
patient.set_birth_date(birth_date)
patient.set_address(addresses[0])
patient.set_address(addresses[1])
patient.set_telecom(telecom)

# Retrieving the Patient resource dict
patient_json_dict = patient.create(1)
print(patient_json_dict)

# Retrieve the Patient resource JSON string
print(json.dumps(patient_json_dict))
```
## Patient SC2

```python
import json
import uuid
from fhir_data_generator import Patient


Patient = Patient(str(uuid.uuid4()))

patient.set_profile_url('https://fhir.server/path/to/profile/path')

identifier1 = {
    'use': 'official',
    'system': 'http://www.boca.gov.tw',
    'type': {
        'coding': [
            {
                'system': 'http://www.boca.gov.tw',
                'code': 'PPN',
                'display': 'Passport number',
            },
        ],
    },
    'value': 'E262344368'[2:],
}
identifier2 = {
    'use': 'official',
    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
    'type': {
        'coding': [
            {
                'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                'code': 'MR',
                'display': 'Medical record number',
            },
        ]
    },
    'value': '123456789',
}

patient.set_identifier(identifier1)
patient.set_identifier(identifier2)

patient.set_active(True)

managing_organization = 'Organization/MITW.ForIdentifier'
patient.set_managing_organization(managing_organization)

names = [
    {
        'use': 'official',
        'family': 'Li',
        'given': [
            'Peter'
        ],
        'text': 'Peter Li',
    },
]

patient.set_name(names[0])

gender = 'male'
patient.set_gender(gender)

birth_date = '2023-12-23'
patient.set_birth_date(birth_date)

addresses = [
    {
        'use': 'home',
        'text': '105台北市松山區民生東路四段133號',
    },
    {
        'country': 'TW',
    },
]

patient.set_address(addresses[0])
patient.set_address(addresses[1])

telecom = {
    'use': 'home',
    'system': 'phone',
    'value': '0905285349',
}
patient.set_telecom(telecom)

communications = [
    {
        'language': {
            'coding': [
                {
                    'system': 'http://terminology.hl7.org/CodeSystem/v3-ietf3066',
                    'code': 'en-US',
                },
            ],
            'text': 'English (US)',
        },
    },
]

patient.set_communication(communications[0])

scenario = 2

# Retrieving the Patient resource dict
patient_json_dict = patient.create(scenario)
print(patient_json_dict)

# Retrieve the Patient resource JSON string
print(json.dumps(patient_json_dict))
```

## Patient SC3

```python
import json
import uuid
from fhir_data_generator import Patient


patient = Patient(str(uuid.uuid4()))
patient.set_profile_url('https://fhir.server/path/to/profile/path')

patient.set_identifier(identifiers[0])
patient.set_identifier(identifiers[1])

gender = 'male'
patient.set_gender(gender)

birth_date = '2023-12-23'
patient.set_birth_date(birth_date)

contacts = [
    {
        'relationship': [
            {
                'coding': [
                    {
                        'system': 'http://terminology.hl7.org/CodeSystem/v2-0131',
                        'code': 'CP',
                    },
                ],
                'text': 'Contact person',
            },
        ],
        'name': {
            'text': 'Peter Li',
            'family': 'Li',
            'given': [
                'Peter',
            ],
        },
        'telecom': [
            {
                'system': 'phone',
                'value': '0905285349',
                'use': 'mobile',
            },
            {
                'system': 'email',
                'value': 'peter279k@gmail.com',
            },
        ],
    },
]
patient.set_contact(contacts[0])

addresses = [
    {
        'use': 'home',
        'text': '105台北市松山區民生東路四段133號',
    },
    {
        'country': 'TW',
    },
]
patient.set_address(addresses[0])
patient.set_address(addresses[1])

patient.set_active(True)

managing_organization = 'Organization/MITW.ForIdentifier'
patient.set_managing_organization(managing_organization)

scenario = 3

# Retrieving the Patient resource dict
patient_json_dict = patient.create(scenario)
print(patient_json_dict)

# Retrieve the Patient resource JSON string
print(json.dumps(patient_json_dict))
```

## Observation BMI Example

```python
import json
import uuid
from fhir_data_generator import Observation


observation = Observation(str(uuid.uuid4()))

profile_urls = ['https://fhir.server/path/to/profile/path']
observation.set_profile_urls(profile_urls)

status = 'final
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
```

### CarePlan Example (MITW 2024)

```python
import json
import uuid
from fhir_data_generator import CarePlan


care_plan = CarePlan(str(uuid.uuid4()))

profile_urls = [
    'https://hapi.fhir.tw/fhir/StructureDefinition/Careplan-sport',
]
care_plan.set_profile_urls(profile_urls)

status = 'active'
care_plan.set_status(status)

intent = 'plan'
care_plan.set_intent(intent)

category_coding = [
    {
        'system': 'https://hapi.fhir.tw/fhir/CodeSystem/tempcode',
        'code': 'PhysicalActivity',
        'display': 'Physical Activity',
    }
]
care_plan.set_category_coding(category_coding)

description = '椎間盤間隔小/退化擠壓狀況 核心訓練以髖部(臀部)和腹部訓練為主'
care_plan.set_description(description)

subject = {
    'reference': 'Patient/patient-tw-example',
}
care_plan.set_subject(subject)

author = {
    'reference': 'Practitioner/practitioner-c-example'
}
care_plan.set_author(author)

goal = [{
    'reference': 'Goal/goal-example',
}]
care_plan.set_goal(goal)

activity_progress = [
    {
        'time': '2024-07-03',
        'text': '滾筒放鬆：1.胸椎伸展 8趟 2.上背滾動 10趟 3.胸椎旋轉 左右各8次 核心：1.死蟲 後腳跟點地板 單邊各六下 兩組 2.橋式+彈力圈 20下 1組 3.徒手弓箭步單側負重6公斤10下一組,前腳墊高10下一組',
    },
]
care_plan.set_activity_progress(activity_progress)

activity_detail = {
    'status': 'completed',
    'description': '機械臀推/彈力箱臀推 感受度不佳 暫時不做',
}
care_plan.set_activity_detail(activity_detail)

note = [{
    'time': '2024-07-04',
    'text': '肚臍對應後方腰椎摸會痛，活動筋骨及輕微推拿後有好一點',
}]
care_plan.set_note(note)

# Retrieving the CarePlan resource dict
care_plan_json_dict = care_plan.create()
print(care_plan_json_dict)

# Retrieve the CarePlan resource JSON string
print(json.dumps(care_plan_json_dict))
```

### Goal Example (MITW 2024)

```python
import json
import uuid
from fhir_data_generator import Goal


goal = Goal(str(uuid.uuid4()))

profile_urls = [
    'https://hapi.fhir.tw/fhir/StructureDefinition/Goal-sport',
]
goal.set_profile_urls(profile_urls)

lifecycle_status = 'proposed'
goal.set_lifecycle_status(lifecycle_status)

category_coding = [{
    'system': 'https://hapi.fhir.tw/fhir/CodeSystem/tempcode',
    'code': 'PhysicalActivity',
    'display': 'Physical Activity'
}]
goal.set_category_coding(category_coding)

description_text = 'L5-S1椎間盤突出，在六個月內減少突出程度2-3毫米，疼痛評分減少50%'
goal.set_description_text(description_text)

subject = {
    'reference': 'Patient/patient-tw-example',
}
goal.set_subject(subject)

target_measure_coding = [{
    'system': 'http://loinc.org',
    'code': '41950-7',
    'display': 'Number of steps in 24 hour Measured',
}]
goal.set_target_measure_coding(target_measure_coding)

target_detail_quantity = {
    'value': 5000,
    'unit': 'steps per day',
    'system': 'http://unitsofmeasure.org',
    'code': '/d',
}
goal.set_target_detail_quantity(target_detail_quantity)

# Retrieving the Goal resource dict
goal_json_dict = goal.create()
print(goal_json_dict)

# Retrieve the Goal resource JSON string
print(json.dumps(goal_json_dict))
```

### Practitioner for Physical Activity Example (MITW 2024)

```python
import json
import uuid
from fhir_data_generator import PhysicalActivityPractitioner as Practitioner


practitioner = Practitioner(str(uuid.uuid4()))

profile_urls = [
    'https://hapi.fhir.tw/fhir/StructureDefinition/TWCorePractitioner',
]
practitioner.set_profile_urls(profile_urls)

identifiers = [
    {
        'use': 'official',
        'type': {
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                'code': 'MB'
            }]
        },
        'system': 'https://www.morefit.com.tw/tw',
        'value': 'S1006',
    }
]
practitioner.set_identifiers(identifiers)

active = True
practitioner.set_active(active)

name_text = '陳漸升'
practitioner.set_name_text(name_text)

# Retrieving the Practitioner for Physical Activity resource dict
practitioner_json_dict = practitioner.create()
print(practitioner_json_dict)

# Retrieve the Practitioner for Physical Activity resource JSON string
print(json.dumps(practitioner_json_dict))
```

### Condition E for Physical Activity Example (MITW 2024)

```python
import json
import uuid
from fhir_data_generator import ConditionE


condition_e = ConditionE(str(uuid.uuid4()))

profile_urls = [
    'https://hapi.fhir.tw/fhir/StructureDefinition/Condition-excercise-history',
]
condition_e.set_profile_urls(profile_urls)

clinical_status_coding = [{
    'system': 'http://terminology.hl7.org/CodeSystem/condition-clinical',
    'code': 'active',
}]
condition_e.set_clinical_status_coding(clinical_status_coding)

category_coding = [{
    'system': 'https://hapi.fhir.tw/fhir/CodeSystem/tempcode',
    'code': 'PhysicalActivity',
    'display': 'Physical Activity',
}]
condition_e.set_category_coding(category_coding)

code_coding =[{
    'system': 'http://snomed.info/sct',
    'code': '229072005',
    'display': 'Aerobic exercises',
}]
condition_e.set_code_coding(code_coding)

code_text = '一週2次有氧運動 每次30分鐘'
condition_e.set_code_text(code_text)

subject = {
    'reference': 'Patient/patient-tw-example',
}
condition_e.set_subject(subject)

asserter = {
    'reference': 'Practitioner/practitioner-d-example',
}
condition_e.set_asserter(asserter)

# Retrieving the Condition E for Physical Activity resource dict
condition_e_json_dict = condition_e.create()
print(condition_e_json_dict)

# Retrieve the Condition E for Physical Activity resource JSON string
print(json.dumps(condition_e_json_dict))
```

### Organization H for Physical Activity example (MITW 2024)

```python
import json
import uuid
from fhir_data_generator import OrganizationH


organization_h = OrganizationH(str(uuid.uuid4()))

profile_urls = ['https://hapi.fhir.tw/fhir/StructureDefinition/TWCoreOrganization']
organization_h.set_profile_urls(profile_urls)

identifiers = [
    {
        'use': 'official',
        'type': {
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                'code': 'PRN'
            }],
        },
        'system': 'https://www.vghtpe.gov.tw',
        'value': '0601160016',
    },
]
organization_h.set_identifiers(identifiers)

type_coding = [{
    'system': 'http://terminology.hl7.org/CodeSystem/organization-type',
    'code': 'prov',
}]
organization_h.set_type_coding(type_coding)

name = '臺北醫院'
organization_h.set_name(name)

# Retrieving the Organization H for Physical Activity resource dict
organization_h_json_dict = organization_h.create()
print(organization_h_json_dict)

# Retrieve the Organization H for Physical Activity resource JSON string
print(json.dumps(organization_h_json_dict))
```

### Organization S for Physical Activity example (MITW 2024)

```python
import json
import uuid
from fhir_data_generator import OrganizationS


organization_s = OrganizationS(str(uuid.uuid4()))

profile_urls = ['https://hapi.fhir.tw/fhir/StructureDefinition/TWCoreOrganization']
organization_s.set_profile_urls(profile_urls)

identifiers = [
    {
        'use': 'official',
        'type': {
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                'code': 'PRN'
            }],
        },
        'system': 'https://www.morefit.com.tw',
        'value': '85037366',
    },
]
organization_s.set_identifiers(identifiers)

type_coding = [{
    'system': 'http://terminology.hl7.org/CodeSystem/organization-type',
    'code': 'team',
}]
organization_s.set_type_coding(type_coding)

name = 'morefit
organization_s.set_name(name)

organization_s.create()

# Retrieving the Organization S for Physical Activity resource dict
organization_s_json_dict = organization_s.create()
print(organization_s_json_dict)

# Retrieve the Organization S for Physical Activity resource JSON string
print(json.dumps(organization_s_json_dict))
```

### Patient EX for Physical Activity example (MITW 2024)

```python
import json
import uuid
from fhir_data_generator import PatientEX


patient_ex = PatientEX(str(uuid.uuid4()))

profile_urls = ['https://hapi.fhir.tw/fhir/StructureDefinition/Patient-sport']
patient_ex.set_profile_urls(profile_urls)

extension_url = 'https://hapi.fhir.tw/fhir/StructureDefinition/person-age'
patient_ex.set_extension_url(extension_url)

extension_value_age = {
    'value': 32,
    'unit': '32',
    'system': 'http://unitsofmeasure.org',
    'code': 'a',
}
patient_ex.set_extension_value_age(extension_value_age)

identifiers = [{
    'system': 'https://www.morefit.com.tw',
    'value': '0938110330',
}]
patient_ex.set_identifiers(identifiers)

name_text = '連小妹'
patient_ex.set_name_text(name_text)

gender = 'female'
patient_ex.set_gender(gender)

birth_date = '1990-01-01'
patient_ex.set_birth_date(birth_date)

# Retrieving the Patient EX for Physical Activity resource dict
patient_ex_json_dict = patient_ex.create()
print(patient_ex_json_dict)

# Retrieve the Patient EX for Physical Activity resource JSON string
print(json.dumps(patient_ex_json_dict))
```

### Patient TW for Physical Activity example (MITW 2024)

```python
import json
import uuid
from fhir_data_generator import PatientTW


patient_tw = PatientTW(str(uuid.uuid4()))

profile_urls = ['https://hapi.fhir.tw/fhir/StructureDefinition/TWCorePatient']
patient_tw.set_profile_urls(profile_urls)

extension_url = 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/person-age'
patient_tw.set_extension_url(extension_url)

extension_value_age = {
    'value': 32,
    'system': 'http://unitsofmeasure.org',
    'code': 'a',
}
patient_tw.set_extension_value_age(extension_value_age)

extension_extension_coding = [{
    'system': 'urn:iso:std:iso:3166',
    'code': 'TW',
}]
patient_tw.set_extension_extension_coding(extension_extension_coding)

extension_extension_url = 'http://hl7.org/fhir/StructureDefinition/patient-nationality'
patient_tw.set_extension_extension_url(extension_extension_url)

identifiers = [{
    'use': 'official',
    'type': {
        'coding': [{
            'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
            'code': 'NNxxx',
            '_code': {
                'extension': [{
                    'extension': [
                        {
                            'url': 'suffix',
                            'valueString': 'TWN'
                        },
                        {
                                'url': 'valueSet',
                                'valueCanonical': 'http://hl7.org/fhir/ValueSet/iso3166-1-3'
                        }
                    ],
                    'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/identifier-suffix'
                }]
            }
        }]
    },
    'system': 'http://www.moi.gov.tw',
    'value': 'A123456789'
}]
patient_tw.set_identifiers(identifiers)

active = True
patient_tw.set_active(active)

name_user = 'official'
patient_tw.set_name_use(name_use)

name_text = '連小妹'
patient_tw.set_name_text(name_text)

gender = 'female'
patient_tw.set_gender(gender)

birth_date = '1990-01-01'
patient_tw.set_birth_date(birth_date)

# Retrieving the Patient TW for Physical Activity resource dict
patient_tw_json_dict = patient_tw.create()
print(patient_tw_json_dict)

# Retrieve the Patient TW for Physical Activity resource JSON string
print(json.dumps(patient_tw_json_dict))
```

### ServiceRequest for Physical Activity example (MITW 2024)

```python
import json
import uuid
from fhir_data_generator import PhysicalActivityServiceRequest


service_request = PhysicalActivityServiceRequest(str(uuid.uuid4()))

profile_urls = ['https://hapi.fhir.tw/fhir/StructureDefinition/ServiceRequest-sport']
service_request.set_profile_urls(profile_urls)

identifiers = [{
    'system': 'https://www.health.ntpc.gov.tw/',
    'value': 's141526',
}]
service_request.set_identifiers(identifiers)

status = 'completed'
service_request.set_status(status)

intent = 'order'
service_request.set_intent(intent)

category_coding = [{
    'system': 'https://hapi.fhir.tw/fhir/CodeSystem/tempcode',
    'code': 'PhysicalActivity',
    'display': 'Physical Activity'
}]
service_request.set_category_coding(category_coding)

code_coding = [{
    'system': 'http://snomed.info/sct',
    'code': '229065009',
    'display': 'Exercise therapy',
}]
service_request.set_code_coding(code_coding)

subject= {
    'reference': 'Patient/patient-tw-example',
}
service_request.set_subject(subject)

authored_on = '2024-07-01'
service_request.set_authored_on(authored_on)

requester = {
    'reference': 'Practitioner/practitioner-d-example',
}
service_request.set_requester(requester)

# Retrieving the ServiceRequest for Physical Activity resource dict
service_request_json_dict = service_request.create()
print(service_request_json_dict)

# Retrieve the ServiceRequest for Physical Activity resource JSON string
print(json.dumps(service_request_json_dict))
```

# References

- https://hackersandslackers.com/python-poetry-package-manager
- https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04
- https://www.freecodecamp.org/news/how-to-build-and-publish-python-packages-with-poetry
- https://stackoverflow.com/questions/68882603/using-python-poetry-to-publish-to-test-pypi-org
