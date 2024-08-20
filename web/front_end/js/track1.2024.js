async function doGenerateRequest(trackServerEndpoint, oauthServerEndpoint, patientPayload, errorMessage) {
    await $.ajax({
        url: `/track1/2024/source/Patient`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track2_server,
            oauth_token_info: oauthServerEndpoint['track#1'],
            oauth_level: $('#source-token-level :selected').val(),
            patient_payload: patientPayload,
        }),
    }).done((data) => {
        let jsonData = data.json;
        let patientResource = jsonData;
        if (data.status !== 200 && data.status !== 201) {
            errorMessage['text'] = `error; HTTP status code: ${data.status}`;
            Swal.fire(errorMessage);

            return false;
        }
        $('result-patient-id').html(patientResource.id);
        localStorage.setItem('created_patient_id', patientResource.id);

        let identifiers = patientResource.identifier;
        let identifierHtml = '';
        identifierHtml += `<li>病患識別碼型別: <span name="result-patient-identifier" class="text-primary">${identifiers[0].type.coding[0].system}#${identifiers[0].type.coding[0].code}</span></li>`;
        identifierHtml += `<li>身份證字號: <span name="result-patient-identifier" class="text-primary">${identifiers[0].value}</span></li>`;

        $('#result-patient-identifier1').html(identifierHtml);

        identifierHtml = '';
        identifierHtml += `<li>病患識別碼型別: <span name="result-patient-identifier" class="text-primary">${identifiers[1].type.coding[0].system}#${identifiers[1].type.coding[0].code}</span></li>`;
        identifierHtml += `<li>病歷號: <span name="result-patient-identifier" class="text-primary">${identifiers[1].value}</span></li>`;

        $('#result-patient-identifier2').html(identifierHtml);

        $('#result-patient-active').html(patientResource.active);
        $('#result-patient-name').html(`${patientResource.name[0].text} ${patientResource.name[0].family}, ${patientResource.name[0].given[0]}`);

        let genderMapping = {
            'male': '男性',
            'female': '女性',
        };
        $('#result-patient-gender').html(genderMapping[patientResource.gender]);

        $('#result-patient-birth-date').html(patientResource.birthDate);

        $('#result-patient-age').html(
            `[extension: ${patientResource.extension[0].url}]: ${patientResource.extension[0].valueAge.value}`
        );
        $('#result-patient-nationality').html(
            `[extension: ${patientResource.extension[1].url}]: ${patientResource.extension[1].extension[0].valueCodeableConcept.coding[0].code}`
        );

        $('#result-patient-phone').html(
            `${patientResource.telecom[0].system}`
        )
        $('#result-patient-mobile').html(
            `${patientResource.telecom[0].value}`
        )
        $('#result-patient-period').html(
            `${patientResource.telecom[0].period.start}~${patientResource.telecom[0].period.end}`
        )

        $('#result-patient-address').html(
            `(${patientResource.address[0]._postalCode.extension[0].valueCodeableConcept.coding[0].code})${patientResource.address[0].text}`
        );
        $('#result-patient-address-postal').html(
            `${patientResource.address[0]._postalCode.extension[0].valueCodeableConcept.coding[0].code}`
        );
        $('#result-patient-address-city').html(
            `${patientResource.address[0].city}`
        );
        $('#result-patient-address-district').html(
            `${patientResource.address[0].district}`
        );
        $('#result-patient-address-line').html(
            `${patientResource.address[0].line[0]}`
        );
        $('#result-patient-address-country').html(
            `${patientResource.address[0].country}`
        );
        let extension = null;
        for (index in patientResource.address[0].extension) {
            extension = patientResource.address[0].extension[index];
            if (extension.url.includes('village')) {
                $('#result-patient-address-village').html(
                    `${extension.valueString}`
                );
            } else if (extension.url.includes('neighborhood')) {
                $('#result-patient-address-neighborhood').html(
                    `${extension.valueString}`
                );
            } else if (extension.url.includes('section')) {
                $('#result-patient-address-section').html(
                    `${extension.valueString}`
                );
            } else if (extension.url.includes('lane')) {
                $('#result-patient-address-lane').html(
                    `${extension.valueString}`
                );
            } else if (extension.url.includes('alley')) {
                $('#result-patient-address-alley').html(
                    `${extension.valueString}`
                );
            } else if (extension.url.includes('number')) {
                $('#result-patient-address-number').html(
                    `${extension.valueString}`
                );
            } else if (extension.url.includes('floor')) {
                $('#result-patient-address-floor').html(
                    `${extension.valueString}`
                );
            } else if (extension.url.includes('room')) {
                $('#result-patient-address-room').html(
                    `${extension.valueString}`
                );
            }
        }

        $('#result-patient-address-martial').html(
            `${patientResource.maritalStatus.coding[0].code}(${patientResource.maritalStatus.coding[0].system})`
        );

        $('#result-patient-contact-name').html(
            patientResource.contact[0].name.text
        );
        $('#result-patient-contact-relationship').html(
            `${patientResource.contact[0].relationship[0].coding[0].code}(${patientResource.contact[0].relationship[0].coding[0].system})`
        );
        $('#result-patient-contact-phone').html(
            patientResource.contact[0].telecom[0].system
        );
        $('#result-patient-contact-mobile').html(
            patientResource.contact[0].telecom[0].value
        );
        $('#result-patient-contact-period').html(
            `${patientResource.contact[0].telecom[0].period.start}~${patientResource.contact[0].telecom[0].period.end}`
        );
        $('#result-patient-communication').html(
            patientResource.communication[0].language.coding[0].code
        );
        $('#result-patient-managing-organization').html(
            patientResource.managingOrganization.reference
        );

        $('#result-patient-photo').attr(
            'src',
            `data:${patientResource.photo[0].contentType};base64, ${patientResource.photo[0].data}`
        );

        $('#search-result-card').removeClass('d-none');
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        return false;
    });
}

async function doGenerateOrganizationRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage) {
    await $.ajax({
        url: `/track1/2024/source/Organization`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track2_server,
            oauth_token_info: oauthServerEndpoint['track#1'],
            oauth_level: $('#source-token-level :selected').val(),
            patient_payload: payload,
        }),
    }).done((data) => {
        let jsonData = data.json;
        let organizationResource = jsonData;
        if (data.status !== 200 && data.status !== 201) {
            errorMessage['text'] = `error; HTTP status code: ${data.status}`;
            Swal.fire(errorMessage);

            return false;
        }

        $('#result-organization-id').val(organizationResource.id);
        localStorage.setItem('created_organization_id', organizationResource.id);

        $('#result-prn-name').html(organizationResource.name);

        $('#result-prn-identifier').html(
            `${organizationResource.identifier[0].type.coding[0].code} (${organizationResource.identifier[0].type.coding[0].system})`
        );

        $('#result-prn-number').html(
            `${organizationResource.identifier[0].value} (${organizationResource.identifier[0].system})`
        );

        $('#result-patient-prn-coding').html(
            `${organizationResource.type[0].coding[0].code} (${organizationResource.type[0].coding[0].system})`
        );

        $('#result-phone').html(
            `${organizationResource.telecom[0].system}`
        );
        $('#result-phone-number').html(
            `${organizationResource.telecom[0].value}`
        );

        $('#search-result-card').removeClass('d-none');
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        return false;
    });
}

async function doGeneratePractitionerRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage) {
    await $.ajax({
        url: `/track1/2024/source/Practitioner`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track2_server,
            oauth_token_info: oauthServerEndpoint['track#1'],
            oauth_level: $('#source-token-level :selected').val(),
            patient_payload: payload,
        }),
    }).done((data) => {
        let jsonData = data.json;
        let practitionerResource = jsonData;
        if (data.status !== 200 && data.status !== 201) {
            errorMessage['text'] = `error; HTTP status code: ${data.status}`;
            Swal.fire(errorMessage);

            return false;
        }

        $('#result-practitioner-id').html(practitionerResource.id);
        localStorage.setItem('created_practitioner_id', practitionerResource.id);

        let identifiers = practitionerResource.identifier;
        let identifierHtml = '';
        identifierHtml += `<li>識別碼型別: <span name="result-practitioner-identifier" class="text-primary">${identifiers[0].type.coding[0].system}#${identifiers[0].type.coding[0].code}</span></li>`;
        identifierHtml += `<li>身份證字號: <span name="result-practitioner-identifier" class="text-primary">${identifiers[0].value}</span></li>`;

        $('#result-practitioner-identifier1').html(identifierHtml);

        identifierHtml = '';
        identifierHtml += `<li>識別碼型別: <span name="result-practitioner-identifier" class="text-primary">${identifiers[1].type.coding[0].system}#${identifiers[1].type.coding[0].code}</span></li>`;
        identifierHtml += `<li>員工編號: <span name="result-practitioner-identifier" class="text-primary">${identifiers[1].value}</span></li>`;

        $('#result-practitioner-identifier2').html(identifierHtml);

        $('#result-practitioner-active').html(practitionerResource.active);

        $('#result-practitioner-name').html(
            `${practitionerResource.name[0].text} ${practitionerResource.name[0].family}, ${practitionerResource.name[0].given[0]}`
        );

        let mappingGender = {
            'male': '男性',
            'female': '女性',
        };
        $('#result-practitioner-gender').html(mappingGender[practitionerResource.gender]);

        $('#result-practitioner-birth-date').html(practitionerResource.birthDate);

        $('#result-practitioner-phone').html(practitionerResource.telecom[0].system);
        $('#result-practitioner-mobile').html(practitionerResource.telecom[0].value);
        $('#result-practitioner-phone-period').html(
            `${practitionerResource.telecom[0].period.start}至${practitionerResource.telecom[0].period.end}`
        );

        $('#result-practitioner-address').html(
            `(${practitionerResource.address[0]._postalCode.extension[0].valueCodeableConcept.coding[0].code})${practitionerResource.address[0].text}`
        );
        $('#result-practitioner-postal').html(
            `${practitionerResource.address[0]._postalCode.extension[0].valueCodeableConcept.coding[0].code} (${practitionerResource.address[0]._postalCode.extension[0].valueCodeableConcept.coding[0].system})`
        );
        $('#result-practitioner-district').html(practitionerResource.address[0].district);
        $('#result-practitioner-city').html(practitionerResource.address[0].city);
        $('#result-practitioner-road').html(practitionerResource.address[0].line[0]);
        $('#result-practitioner-number').html(
            practitionerResource.address[0].extension[0].valueString
        );

        $('#result-practitioner-country').html(practitionerResource.address[0].country);

        $('#result-practitioner-qualification').html(
            `${practitionerResource.qualification[0].code.coding[0].display} (${practitionerResource.qualification[0].code.coding[0].system}#${practitionerResource.qualification[0].code.coding[0].code})`
        );
        $('#result-practitioner-qualification-start').html(
            practitionerResource.qualification[0].period.start
        );

        $('#result-practitioner-photo').attr(
            'src',
            `data:${practitionerResource.photo[0].contentType};base64, ${practitionerResource.photo[0].data}`
        );

        $('#search-result-card').removeClass('d-none');

    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        return false;
    });
}

async function doGeneratePractitionerRoleRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage) {
    await $.ajax({
        url: `/track1/2024/source/PractitionerRole`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track2_server,
            oauth_token_info: oauthServerEndpoint['track#1'],
            oauth_level: $('#source-token-level :selected').val(),
            patient_payload: payload,
        }),
    }).done((data) => {
        let jsonData = data.json;
        let practitionerRoleResource = jsonData;
        if (data.status !== 200 && data.status !== 201) {
            errorMessage['text'] = `error; HTTP status code: ${data.status}`;
            Swal.fire(errorMessage);

            return false;
        }

        $('#result-practitioner-role-id').html(practitionerRoleResource.id);
        localStorage.setItem('created_practitioner_id', practitionerRoleResource.id);

        let identifiers = practitionerRoleResource.identifier;
        let identifierHtml = '';
        identifierHtml += `<li>識別碼型別: <span name="result-practitioner-role-identifier" class="text-primary">${identifiers[0].type.coding[0].system}#${identifiers[0].type.coding[0].code}</span></li>`;
        identifierHtml += `<li>員工編號: <span name="result-practitioner-identifier" class="text-primary">${identifiers[0].value}</span></li>`;

        $('#result-practitioner-role-identifier1').html(identifierHtml);

        $('#result-practitioner-role-active').html(practitionerRoleResource.active);

        $('#result-practitioner-role-business').html(
            `${practitionerRoleResource.period.start} ~ ${practitionerRoleResource.period.end}`
        );

        $('#result-practitioner').html(
            `${practitionerRoleResource.practitioner.reference} "${practitionerRoleResource.practitioner.display}"`
        );

        $('#result-practitioner-role-location').html(
            `${practitionerRoleResource.location[0].reference} "${practitionerRoleResource.location[0].display}"`
        );

        $('#result-practitioner-role').html(
            `${practitionerRoleResource.code[0].coding[0].display} (${practitionerRoleResource.code[0].coding[0].system}#${practitionerRoleResource.code[0].coding[0].code})`
        );

        $('#result-practitioner-role-profession').html(
            `${practitionerRoleResource.specialty[0].coding[0].display} (${practitionerRoleResource.specialty[0].coding[0].system}#${practitionerRoleResource.code[0].coding[0].code})`
        );

        $('#result-practitioner-role-phone').html(
            `${practitionerRoleResource.telecom[0].system}`
        );
        $('#result-practitioner-role-phone-number').html(
            `(${practitionerRoleResource.telecom[0].use}) ${practitionerRoleResource.telecom[0].value}`
        );

        let daysOfWeek = practitionerRoleResource.availableTime[0].daysOfWeek;
        let mappingWeeks = {
            'mon': '一',
            'tue': '二',
            'wed': '三',
            'thu': '四',
            'fri': '五',
            'sat': '六',
            'sun': '日',
        };
        $('#result-practitioner-role-business-contact').html(
            `週${mappingWeeks[daysOfWeek[0]]} ~ 週${mappingWeeks[daysOfWeek[daysOfWeek.length-1]]}，${practitionerRoleResource.availableTime[0].availableStartTime}-${practitionerRoleResource.availableTime[0].availableEndTime}`
        );

        $('#result-practitioner-role-message').html(
            practitionerRoleResource.availabilityExceptions
        );

        $('#result-practitioner-role-unavailable').html(
            `${practitionerRoleResource.notAvailable[0].during.start} ~ ${practitionerRoleResource.notAvailable[0].during.end}`
        );

        $('#result-practitioner-role-unavailable-reason').html(
            practitionerRoleResource.notAvailable[0].description
        );

        $('#search-result-card').removeClass('d-none');
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        return false;
    });
}

async function doGenerateEncounterRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage) {
    await $.ajax({
        url: `/track1/2024/source/Encounter`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track2_server,
            oauth_token_info: oauthServerEndpoint['track#1'],
            oauth_level: $('#source-token-level :selected').val(),
            patient_payload: payload,
        }),
    }).done((data) => {
        let jsonData = data.json;
        let encounterResource = jsonData;
        if (data.status !== 200 && data.status !== 201) {
            errorMessage['text'] = `error; HTTP status code: ${data.status}`;
            Swal.fire(errorMessage);

            return false;
        }

        $('#result-encounter-id').html(encounterResource.id);
        localStorage.setItem('created_encounter_id', encounterResource.id);

        $('#result-encounter-identifier').html(
            encounterResource.identifier[0].value
        );

        $('#result-encounter-type').html(
            encounterResource.status
        );

        $('#result-encounter-class').html(
            `${encounterResource.class.code} (${encounterResource.class.system})`
        );

        $('#result-encounter-category').html(
            `${encounterResource.type[0].coding[0].code} (${encounterResource.type[0].coding[0].system})`
        );

        $('#result-encounter-service-type').html(
            `${encounterResource.serviceType.text}(${encounterResource.serviceType.coding[0].display}) (${encounterResource.serviceType.coding[0].system}#${encounterResource.serviceType.coding[0].code})`
        );

        $('#result-encounter-subject').html(
            `${encounterResource.subject.reference}`
        );

        $('#result-encounter-hos').html(
            `${encounterResource.hospitalization.dischargeDisposition.coding[0].code}(${encounterResource.hospitalization.dischargeDisposition.coding[0].system})`
        );

        $('#result-encounter-location').html(
            `${encounterResource.location[0].location.reference}`
        );

        $('#result-encounter-participant-performer').html(
            `${encounterResource.participant[0].type[0].coding[0].code} (${encounterResource.participant[0].type[0].coding[0].system})`
        );

        $('#result-encounter-participant-period').html(
            `${encounterResource.participant[0].period.start} --> ${encounterResource.participant[0].period.end}`
        );

        $('#result-encounter-participant').html(
            `${encounterResource.participant[0].individual.reference}`
        );

        $('#result-encounter-hos-period').html(
            `${encounterResource.period.start} --> ${encounterResource.period.end}`
        );

        $('#result-encounter-reason').html(
            `${encounterResource.reasonCode[0].coding[0].display} (${encounterResource.reasonCode[0].coding[0].system}#${encounterResource.reasonCode[0].coding[0].code})`
        );

        $('#search-result-card').removeClass('d-none');
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        return false;
    });
}

async function doGenerateAllergyIntoleranceRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage) {
    await $.ajax({
        url: `/track1/2024/source/AllergyIntolerance`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track2_server,
            oauth_token_info: oauthServerEndpoint['track#1'],
            oauth_level: $('#source-token-level :selected').val(),
            patient_payload: payload,
        }),
    }).done((data) => {
        let jsonData = data.json;
        let allergyResource = jsonData;
        if (data.status !== 200 && data.status !== 201) {
            errorMessage['text'] = `error; HTTP status code: ${data.status}`;
            Swal.fire(errorMessage);

            return false;
        }

        $('#result-allergy-id').html(allergyResource.id);
        localStorage.setItem('created_allergy_id', allergyResource.id);

        $('#result-allergy-status').html(allergyResource.clinicalStatus.text);

        $('#result-allergy-verification-status').html(allergyResource.verificationStatus.text);

        $('#result-allergy-type').html(allergyResource.type);

        $('#result-allergy-category').html(allergyResource.category[0]);

        $('#result-allergy-risk').html(`${allergyResource.criticality} risk`);

        $('#result-allergy-identify').html(
            `${allergyResource.code.text}(${allergyResource.code.coding[0].display})`
        );

        $('#result-allergy-identified-datetime').html(allergyResource.onsetDateTime);

        $('#result-allergy-patient').html(
            `${allergyResource.patient.reference} "${allergyResource.patient.display}"`
        );

        $('#result-allergy-recorder').html(
            `${allergyResource.recorder.reference} "${allergyResource.recorder.display}"`
        );

        $('#result-allergy-recorder-datetime').html(allergyResource.recordedDate);

        $('#result-allergy-practitioner').html(
            `${allergyResource.asserter.reference} "${allergyResource.asserter.display}"`
        );

        $('#result-allergy-last-occurrence').html(allergyResource.lastOccurrence);

        $('#result-allergy-med').html(
            `${allergyResource.reaction[0].substance.text} (${allergyResource.reaction[0].substance.coding[0].system}#${allergyResource.reaction[0].substance.coding[0].code})`
        );

        $('#result-allergy-clinical').html(
            `${allergyResource.reaction[0].manifestation[0].coding[0].display} (${allergyResource.reaction[0].manifestation[0].coding[0].system}#${allergyResource.reaction[0].manifestation[0].coding[0].code})`
        );

        $('#result-allergy-description').html(
            `${allergyResource.reaction[0].description}`
        );

        $('#result-allergy-sev').html(
            `${allergyResource.reaction[0].severity}`
        );

        $('#result-allergy-mainfest').html(
            `${allergyResource.reaction[0].exposureRoute.text} (${allergyResource.reaction[0].exposureRoute.coding[0].display}) (${allergyResource.reaction[0].exposureRoute.coding[0].system}#${allergyResource.reaction[0].exposureRoute.coding[0].code})`
        );

        $('#result-allergy-note').html(
            `${allergyResource.reaction[0].note[0].text}`
        );

        $('#search-result-card').removeClass('d-none');
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        return false;
    });
}

async function doGenerateConditionRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage) {
    await $.ajax({
        url: `/track1/2024/source/Condition`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track2_server,
            oauth_token_info: oauthServerEndpoint['track#1'],
            oauth_level: $('#source-token-level :selected').val(),
            patient_payload: payload,
        }),
    }).done((data) => {
        let jsonData = data.json;
        let conditionResource = jsonData;
        if (data.status !== 200 && data.status !== 201) {
            errorMessage['text'] = `error; HTTP status code: ${data.status}`;
            Swal.fire(errorMessage);

            return false;
        }

        $('#result-condition-id').html(conditionResource.id);
        localStorage.setItem('created_condition_id', conditionResource.id);

        $('#result-condition-clinical').html(
            `${conditionResource.clinicalStatus.coding[0].code} (${conditionResource.clinicalStatus.coding[0].system})`
        );

        $('#result-condition-verification-status').html(
            `${conditionResource.verificationStatus.coding[0].code} (${conditionResource.verificationStatus.coding[0].system})`
        );

        $('#result-condition-diagnosis').html(
            `${conditionResource.category[0].coding[0].code} (${conditionResource.category[0].coding[0].system})`
        );

        $('#result-condition-code').html(
            `${conditionResource.severity.coding[0].code} (${conditionResource.severity.coding[0].system})`
        );

        $('#result-condition-message').html(
            `${conditionResource.code.text} (${conditionResource.code.coding[0].system}#${conditionResource.code.coding[0].code})`
        );

        $('#result-condition-patient').html(
            `${conditionResource.subject.reference}`
        );

        $('#result-condition-onset-datetime').html(
            `${conditionResource.onsetDateTime}`
        );

        $('#result-condition-abatement-datetime').html(
            `${conditionResource.abatementDateTime}`
        );

        $('#result-condition-asserter').html(
            `${conditionResource.asserter.reference}`
        );

        $('#search-result-card').removeClass('d-none');
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        return false;
    });
}

async function doGenerateDiagnosticReportRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage) {
    await $.ajax({
        url: `/track1/2024/source/DiagnosticReport`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track2_server,
            oauth_token_info: oauthServerEndpoint['track#1'],
            oauth_level: $('#source-token-level :selected').val(),
            patient_payload: payload,
        }),
    }).done((data) => {
        let jsonData = data.json;
        let diagnosticReportResource = jsonData;
        if (data.status !== 200 && data.status !== 201) {
            errorMessage['text'] = `error; HTTP status code: ${data.status}`;
            Swal.fire(errorMessage);

            return false;
        }

        $('#result-report-id').html(diagnosticReportResource.id);
        localStorage.setItem('created_report_id', diagnosticReportResource.id);

        $('#result-report-status').html(
            `${diagnosticReportResource.status} (DiagnosticReportStatus)`
        );

        $('#result-report-category').html(
            `${diagnosticReportResource.category[0].text} (${diagnosticReportResource.category[0].coding[0].system}#${diagnosticReportResource.category[0].coding[0].code})`
        );

        $('#result-report-patient').html(
            `${diagnosticReportResource.subject.reference}`
        );

        $('#result-report-effective').html(
            `${diagnosticReportResource.effectiveDateTime}`
        );

        $('#result-report-issued').html(
            `${diagnosticReportResource.issued}`
        );

        $('#result-report-code').html(
            `${diagnosticReportResource.code.text} (${diagnosticReportResource.code.coding[0].system}#${diagnosticReportResource.code.coding[0].code})`
        );

        $('#result-report-report').html(
            `${diagnosticReportResource.result[0].reference}`
        );

        $('#result-report-practitioner').html(
            `${diagnosticReportResource.performer[0].reference}`
        );

        $('#search-result-card').removeClass('d-none');
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        return false;
    });
}

async function doGenerateDocumentReferenceRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage) {
    await $.ajax({
        url: `/track1/2024/source/DocumentReference`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track2_server,
            oauth_token_info: oauthServerEndpoint['track#1'],
            oauth_level: $('#source-token-level :selected').val(),
            patient_payload: payload,
        }),
    }).done((data) => {
        let jsonData = data.json;
        let documentReferenceResource = jsonData;
        if (data.status !== 200 && data.status !== 201) {
            errorMessage['text'] = `error; HTTP status code: ${data.status}`;
            Swal.fire(errorMessage);

            return false;
        }

        $('#result-document-id').html(documentReferenceResource.id);
        localStorage.setItem('created_document_id', documentReferenceResource.id);

        $('#result-document-status').html(
            `${documentReferenceResource.status} (DocumentReferenceStatus)`
        );

        $('#result-document-type').html(
            `${documentReferenceResource.type.text}(${documentReferenceResource.type.coding[0].display}) ${documentReferenceResource.type.coding[0].system}#${documentReferenceResource.type.coding[0].code}`
        );

        $('#result-document-patient').html(
            `${documentReferenceResource.subject.reference}`
        );

        $('#result-document-date').html(
            `${documentReferenceResource.date}`
        );

        $('#result-document-practitioner').html(
            `${documentReferenceResource.author[0].reference}`
        );

        $('#result-document-organization').html(
            `${documentReferenceResource.custodian.reference}`
        );

        $('#result-document-content-file-type').html(
            `${documentReferenceResource.content[0].attachment.contentType}`
        );

        $('#result-document-content-file').html(
            `${documentReferenceResource.content[0].attachment.url} (${documentReferenceResource.content[0].attachment.title})`
        );

        $('#search-result-card').removeClass('d-none');
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        return false;
    });
}

async function doGenerateImagingStudyRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage) {
    await $.ajax({
        url: `/track1/2024/source/ImagingStudy`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track2_server,
            oauth_token_info: oauthServerEndpoint['track#1'],
            oauth_level: $('#source-token-level :selected').val(),
            patient_payload: payload,
        }),
    }).done((data) => {
        let jsonData = data.json;
        let ImagingStudyResource = jsonData;
        if (data.status !== 200 && data.status !== 201) {
            errorMessage['text'] = `error; HTTP status code: ${data.status}`;
            Swal.fire(errorMessage);

            return false;
        }

        $('#result-imaging-id').html(ImagingStudyResource.id);
        localStorage.setItem('created_imaging_study_id', ImagingStudyResource.id);

        $('#result-imaging-status').html(
            `${ImagingStudyResource.status} (ImagingStudyStatus)`
        );

        $('#result-imaging-identifier').html(
            `${ImagingStudyResource.identifier[0].value} (${ImagingStudyResource.identifier[0].use})`
        );

        $('#result-imaging-start').html(
            `${ImagingStudyResource.started}`
        );

        $('#result-imaging-patient').html(
            `${ImagingStudyResource.subject.reference}`
        );

        $('#result-imaging-encounter').html(
            `${ImagingStudyResource.encounter.reference}`
        );

        $('#result-imaging-series').html(
            `${ImagingStudyResource.numberOfSeries}`
        );

        $('#result-imaging-instances').html(
            `${ImagingStudyResource.numberOfInstances}`
        );

        $('#result-imaging-procedure').html(
            `${ImagingStudyResource.procedureReference.reference}`
        );

        $('#result-imaging-procedure-code').html(
            `${ImagingStudyResource.procedureCode[0].coding[0].display} (${ImagingStudyResource.procedureCode[0].coding[0].system}#${ImagingStudyResource.procedureCode[0].coding[0].code})`
        );

        $('#result-imaging-dicom-uid').html(
            `${ImagingStudyResource.series[0].uid}`
        );

        $('#result-imaging-device').html(
            `${ImagingStudyResource.series[0].modality.system}#${ImagingStudyResource.series[0].modality.code}`
        );

        $('#result-imaging-body-site').html(
            `${ImagingStudyResource.series[0].bodySite.display} (${ImagingStudyResource.series[0].bodySite.system}#${ImagingStudyResource.series[0].bodySite.code})`
        );

        $('#result-imaging-body-practitioner').html(
            `${ImagingStudyResource.series[0].performer[0].actor.reference}`
        );

        $('#result-imaging-body-sop-uid').html(
            `${ImagingStudyResource.series[0].instance[0].uid}`
        );

        $('#result-imaging-body-sop-class').html(
            `${ImagingStudyResource.series[0].instance[0].sopClass.code}`
        );

        $('#search-result-card').removeClass('d-none');
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        return false;
    })
}
