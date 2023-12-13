from fixtures.patient_sc1_info import *


def test_set_fhir_server_endpoint(patient_class):
    expected = 'https://hapi.fhir.tw/fhir/Patient'

    patient_class.set_fhir_server_endpoint('https://hapi.fhir.tw/fhir/Patient')

    assert patient_class.api_endpoint == expected

def test_build_patient_id_query(patient_class):
    expected = '_id=61847'

    result = patient_class.build_patient_id_query('61847')

    assert result == expected

def test_build_search_param(patient_class):
    expected = 'given=%E5%B0%8F%E6%98%8E&organization=III'

    result = patient_class.build_search_param({'given': '小明', 'organization': 'III'})

    assert result == expected

def test_build_patient_id_query_on_fhir_server_endpoint(patient_class):
    expected = 'https://hapi.fhir.tw/fhir/Patient?_id=61847'

    patient_class.set_fhir_server_endpoint('https://hapi.fhir.tw/fhir/Patient')
    id_query_param = patient_class.build_patient_id_query('61847')
    result = f'{patient_class.api_endpoint}?{id_query_param}'

    assert result == expected

def test_build_search_param_on_fhir_server_endpoint(patient_class):
    expected = 'https://hapi.fhir.tw/fhir/Patient?given=%E5%B0%8F%E6%98%8E&organization=III'

    patient_class.set_fhir_server_endpoint('https://hapi.fhir.tw/fhir/Patient')
    search_param = patient_class.build_search_param({'given': '小明', 'organization': 'III'})
    result = f'{patient_class.api_endpoint}?{search_param}'

    assert result == expected
