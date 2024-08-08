import pytest
from fhir_data_generator import TWCoreImagingStudy as ImagingStudy


@pytest.fixture
def imaging_study_class():
    return ImagingStudy('img-example')

@pytest.fixture
def profile_urls():
    return [
        'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/ImagingStudy-twcore',
    ]

@pytest.fixture
def identifier():
    return [{
        'use': 'official',
        'type': {
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                'code': 'ACSN',
                'display': 'Accession ID'
            }]
        },
        'system': 'http://www.moi.gov.tw',
        'value': '2ffe0c20-50d8-49df-85f6-6452d1d201b9'
    }]

@pytest.fixture
def status():
    return 'available'

@pytest.fixture
def subject():
    return {
        'reference': 'Patient/pat-example'
    }

@pytest.fixture
def encounter():
    return {
        'reference': 'Encounter/enc-example'
    }

@pytest.fixture
def started():
    return '2022-08-01T19:00:14+08:00'

@pytest.fixture
def number_of_series():
    return 1

@pytest.fixture
def number_of_instances():
    return 1

@pytest.fixture
def procedure_reference():
    return {
        'reference': 'Procedure/pro-example'
    }

@pytest.fixture
def procedure_code_coding():
    return [{
        'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-10-pcs-2021-tw',
        'code': 'BW40ZZZ',
        'display': '腹部超音波'
    }]

@pytest.fixture
def series_uid():
    return '2.25.88017001449189502323411118737039844242'

@pytest.fixture
def series_modality():
    return {
        'system': 'http://dicom.nema.org/resources/ontology/DCM',
        'code': 'US'
    }

@pytest.fixture
def series_body_site():
    return {
        'system': 'http://snomed.info/sct',
        'code': '251007',
        'display': 'Pectoral region'
    }

@pytest.fixture
def series_performer_actor():
    return {
        'reference': 'Practitioner/pra-radio-example'
    }

@pytest.fixture
def series_instance_uid():
    return '2.25.284548087604447302186649612333159050027'

@pytest.fixture
def series_instance_sop_class():
    return {
        'system': 'urn:ietf:rfc:3986',
        'code': 'urn:oid:1.2.840.10008.5.1.4.1.1.3.1'
    }

@pytest.fixture
def expected_payload():
    return {
        'resourceType': 'ImagingStudy',
        'id': 'img-example',
        'meta': {
            'profile': [
                'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/ImagingStudy-twcore'
            ]
        },
        'identifier': [{
            'use': 'official',
            'type': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code': 'ACSN',
                    'display': 'Accession ID'
                }]
            },
            'system': 'http://www.moi.gov.tw',
            'value': '2ffe0c20-50d8-49df-85f6-6452d1d201b9'
        }],
        'status': 'available',
        'subject': {
            'reference': 'Patient/pat-example'
        },
        'encounter': {
            'reference': 'Encounter/enc-example'
        },
        'started': '2022-08-01T19:00:14+08:00',
        'numberOfSeries': 1,
        'numberOfInstances': 1,
        'procedureReference': {
            'reference': 'Procedure/pro-example'
        },
        'procedureCode': [{
            'coding': [{
                'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-10-pcs-2021-tw',
                'code': 'BW40ZZZ',
                'display': '腹部超音波'
            }]
        }],
        'series': [{
            'uid': '2.25.88017001449189502323411118737039844242',
            'modality': {
                'system': 'http://dicom.nema.org/resources/ontology/DCM',
                'code': 'US'
            },
            'bodySite': {
                'system': 'http://snomed.info/sct',
                'code': '251007',
                'display': 'Pectoral region'
            },
            'performer': [{
                'actor': {
                    'reference': 'Practitioner/pra-radio-example'
                }
            }],
            'instance': [{
                'uid': '2.25.284548087604447302186649612333159050027',
                'sopClass': {
                    'system': 'urn:ietf:rfc:3986',
                    'code': 'urn:oid:1.2.840.10008.5.1.4.1.1.3.1'
                }
            }]
        }]
    }
