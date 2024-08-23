async function doGenerateLocationRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage, roleType='source') {
    await $.ajax({
        url: `/track1/2024/${roleType}/Location`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track1_server,
            oauth_token_info: oauthServerEndpoint['track#1'],
            oauth_level: $(`#${roleType}-token-level :selected`).val(),
            patient_payload: payload,
        }),
    }).done((data) => {
        let jsonData = data.json;
        let locationResource = jsonData;
        if (data.status !== 200 && data.status !== 201) {
            let htmlErrorMessage = `
                <p>error; HTTP status code: ${data.status}</p>
            `;
            for (let index=0; index<jsonData.issue.length; index++) {
                htmlErrorMessage += `<p class="text-danger">${jsonData.issue[index].severity}; ${jsonData.issue[index].diagnostics}</p>`;
            }
            errorMessage['html'] = htmlErrorMessage;

            Swal.fire(errorMessage);

            return false;
        }

        $('#result-location-id').html(locationResource.id);
        localStorage.setItem('created_location_id', locationResource.id);

        $('#result-location-status').html(
            locationResource.status
        );

        $('#result-location-name').html(
            locationResource.name
        );

        $('#result-location-kind').html(
            locationResource.mode
        );

        $('#result-location-type').html(
            `${locationResource.type[0].coding[0].display} (${locationResource.type[0].coding[0].system}#${locationResource.type[0].coding[0].code})`
        );

        $('#result-location-info').html(
            `${locationResource.description}`
        );

        $('#result-location-organization').html(
            `${locationResource.managingOrganization.reference}`
        );

        $('#result-location-phone').html(
            `${locationResource.telecom[0].system} (ContactPointSystem)`
        );

        $('#result-location-phone-number').html(
            `${locationResource.telecom[0].value} (${locationResource.telecom[0].use})`
        );

        $('#result-location-address').html(
            `${locationResource.address.text} (${locationResource.address.use})`
        );

        let daysOfWeekMapping = {
            'mon': '週一',
            'tue': '週二',
            'wed': '週三',
            'thu': '週四',
            'fri': '週五',
            'sat': '週六',
            'sun': '週日',
        };
        let weekString = '';
        let daysOfWeek = locationResource.hoursOfOperation[0].daysOfWeek;
        for (index in daysOfWeek) {
            weekString += daysOfWeekMapping[daysOfWeek[index]] + '、';
        }

        let allDay = locationResource.hoursOfOperation[0].allDay;
        if (allDay) {
            allDay = '全天';
        } else {
            allDay = '非全天';
        }

        $('#result-location-operation').html(
            `${weekString.substring(0, weekString.length-1)}，${allDay}`
        );

        $('#search-result-card').removeClass('d-none');
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        $('button[name="generate-btn"]').each((_, element) => {
            $(element).removeAttr('disabled');
        });

        return false;
    });
}

async function doGenerateMediaRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage, roleType='source') {
    await $.ajax({
        url: `/track1/2024/${roleType}/Media`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track1_server,
            oauth_token_info: oauthServerEndpoint['track#1'],
            oauth_level: $(`#${roleType}-token-level :selected`).val(),
            patient_payload: payload,
        }),
    }).done((data) => {
        let jsonData = data.json;
        let mediaResource = jsonData;
        if (data.status !== 200 && data.status !== 201) {
            let htmlErrorMessage = `
                <p>error; HTTP status code: ${data.status}</p>
            `;
            for (let index=0; index<jsonData.issue.length; index++) {
                htmlErrorMessage += `<p class="text-danger">${jsonData.issue[index].severity}; ${jsonData.issue[index].diagnostics}</p>`;
            }
            errorMessage['html'] = htmlErrorMessage;

            Swal.fire(errorMessage);

            return false;
        }

        $('#result-media-id').html(mediaResource.id);
        localStorage.setItem('created_media_id', mediaResource.id);

        $('#result-media-status').html(
            `${mediaResource.status} (EventStatus)`
        );

        $('#result-media-type').html(
            `${mediaResource.type.coding[0].code} (${mediaResource.type.coding[0].system})`
        );

        $('#result-media-patient').html(
            `${mediaResource.subject.reference} "${mediaResource.subject.display}"`
        );

        $('#result-media-view').html(
            `${mediaResource.view.text} (${mediaResource.view.coding[0].system}#${mediaResource.view.coding[0].code})`
        );

        $('#result-media-created').html(
            `${mediaResource.createdDateTime}`
        );

        $('#result-media-issued').html(
            `${mediaResource.issued}`
        );

        $('#result-media-practitioner').html(
            `${mediaResource.operator.reference}`
        );

        $('#result-media-reason').html(
            `${mediaResource.reasonCode[0].coding[0].display} (${mediaResource.reasonCode[0].coding[0].system}#${mediaResource.reasonCode[0].coding[0].code})`
        );

        $('#result-media-body').html(
            `${mediaResource.bodySite.coding[0].display} (${mediaResource.bodySite.coding[0].system}#${mediaResource.bodySite.coding[0].code})`
        );

        $('#result-media-device').html(mediaResource.deviceName);

        $('#result-media-file-id').html(mediaResource.content.id);
        $('#result-media-file-type').html(mediaResource.content.contentType);
        $('#result-media-width').html(mediaResource.width);
        $('#result-media-height').html(mediaResource.height);
        $('#result-media-base64').html(
            `(base64 data - ${atob(mediaResource.content.data).length} bytes)`
        );
        $('#result-media-file-created').html(mediaResource.content.creation);
        $('#result-media-note').html(mediaResource.note[0].text);

        $('#search-result-card').removeClass('d-none');
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        $('button[name="generate-btn"]').each((_, element) => {
            $(element).removeAttr('disabled');
        });

        return false;
    });
}

async function doGenerateMedicationRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage, roleType='source') {
    await $.ajax({
        url: `/track1/2024/${roleType}/Medication`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track1_server,
            oauth_token_info: oauthServerEndpoint['track#1'],
            oauth_level: $(`#${roleType}-token-level :selected`).val(),
            patient_payload: payload,
        }),
    }).done((data) => {
        let jsonData = data.json;
        let medicationResource = jsonData;
        if (data.status !== 200 && data.status !== 201) {
            let htmlErrorMessage = `
                <p>error; HTTP status code: ${data.status}</p>
            `;
            for (let index=0; index<jsonData.issue.length; index++) {
                htmlErrorMessage += `<p class="text-danger">${jsonData.issue[index].severity}; ${jsonData.issue[index].diagnostics}</p>`;
            }
            errorMessage['html'] = htmlErrorMessage;

            Swal.fire(errorMessage);

            return false;
        }

        $('#result-medication-id').html(medicationResource.id);
        localStorage.setItem('created_medication_id', medicationResource.id);

        $('#result-medication-med').html(
            `${medicationResource.code.text} (${medicationResource.code.coding[0].system}#${medicationResource.code.coding[0].code})`
        );

        $('#result-medication-form').html(
            `${medicationResource.form.text} (${medicationResource.form.coding[0].system}#${medicationResource.form.coding[0].code})`
        );

        $('#search-result-card').removeClass('d-none');
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        $('button[name="generate-btn"]').each((_, element) => {
            $(element).removeAttr('disabled');
        });

        return false;
    });
}

async function doGenerateMedicationRequestRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage, roleType='source') {
    await $.ajax({
        url: `/track1/2024/${roleType}/MedicationRequest`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track1_server,
            oauth_token_info: oauthServerEndpoint['track#1'],
            oauth_level: $(`#${roleType}-token-level :selected`).val(),
            patient_payload: payload,
        }),
    }).done((data) => {
        let jsonData = data.json;
        let medicationRequestResource = jsonData;
        if (data.status !== 200 && data.status !== 201) {
            let htmlErrorMessage = `
                <p>error; HTTP status code: ${data.status}</p>
            `;
            for (let index=0; index<jsonData.issue.length; index++) {
                htmlErrorMessage += `<p class="text-danger">${jsonData.issue[index].severity}; ${jsonData.issue[index].diagnostics}</p>`;
            }
            errorMessage['html'] = htmlErrorMessage;

            Swal.fire(errorMessage);

            return false;
        }

        $('#result-medication-request-id').html(medicationRequestResource.id);
        localStorage.setItem('created_medication_request_id', medicationRequestResource.id);

        $('#result-medication-request-identifier').html(
            `${medicationRequestResource.identifier[0].value} (${medicationRequestResource.identifier[0].system})`
        );

        $('#result-medication-request-status').html(
            `${medicationRequestResource.status} (${medicationRequestResource.statusReason.coding[0].system}#${medicationRequestResource.statusReason.coding[0].code})`
        );

        $('#result-medication-request-intent').html(
            `${medicationRequestResource.intent} (medicationRequest Intent)`
        );

        $('#result-medication-request-category').html(
            `${medicationRequestResource.category[0].coding[0].code} (${medicationRequestResource.category[0].coding[0].system}#${medicationRequestResource.category[0].coding[0].code})`
        );

        $('#result-medication-request-med').html(
            `${medicationRequestResource.medicationReference.reference}`
        );

        $('#result-medication-request-patient').html(
            `${medicationRequestResource.subject.reference}`
        );

        $('#result-medication-request-encounter').html(
            `${medicationRequestResource.encounter.reference}`
        );

        $('#result-medication-request-datetime').html(
            `${medicationRequestResource.authoredOn}`
        );

        $('#result-medication-request-requester').html(
            `${medicationRequestResource.requester.reference}`
        );

        $('#result-medication-request-reason').html(
            `${medicationRequestResource.reasonReference[0].reference}`
        );

        $('#result-medication-dosage-text').html(
            `${medicationRequestResource.dosageInstruction[0].text}`
        );

        $('#result-medication-dosage-timing').html(
            `${medicationRequestResource.dosageInstruction[0].timing.code.text} (${medicationRequestResource.dosageInstruction[0].timing.code.coding[0].system}#${medicationRequestResource.dosageInstruction[0].timing.code.coding[0].code})`
        );

        $('#result-medication-dosage-route').html(
            `${medicationRequestResource.dosageInstruction[0].route.coding[0].code} (${medicationRequestResource.dosageInstruction[0].route.coding[0].system})`
        );

        $('#result-medication-dosage-rate').html(
            `${medicationRequestResource.dosageInstruction[0].doseAndRate[0].type.coding[0].code} (${medicationRequestResource.dosageInstruction[0].doseAndRate[0].type.coding[0].system})`
        );

        $('#result-medication-request-period').html(
            `${medicationRequestResource.dispenseRequest.validityPeriod.start} --> ${medicationRequestResource.dispenseRequest.validityPeriod.end}`
        );

        $('#search-result-card').removeClass('d-none');
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        $('button[name="generate-btn"]').each((_, element) => {
            $(element).removeAttr('disabled');
        });

        return false;
    });
}

async function doGenerateMedicationDispenseRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage, roleType='source') {
    await $.ajax({
        url: `/track1/2024/${roleType}/MedicationDispense`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track1_server,
            oauth_token_info: oauthServerEndpoint['track#1'],
            oauth_level: $(`#${roleType}-token-level :selected`).val(),
            patient_payload: payload,
        }),
    }).done((data) => {
        let jsonData = data.json;
        let medicationDispenseResource = jsonData;
        if (data.status !== 200 && data.status !== 201) {
            let htmlErrorMessage = `
                <p>error; HTTP status code: ${data.status}</p>
            `;
            for (let index=0; index<jsonData.issue.length; index++) {
                htmlErrorMessage += `<p class="text-danger">${jsonData.issue[index].severity}; ${jsonData.issue[index].diagnostics}</p>`;
            }
            errorMessage['html'] = htmlErrorMessage;

            Swal.fire(errorMessage);

            return false;
        }

        $('#result-medication-dispense-id').html(medicationDispenseResource.id);
        localStorage.setItem('created_medication_dispense_id', medicationDispenseResource.id);

        $('#result-medication-dispense-status').html(
            `${medicationDispenseResource.status} (MedicationDispense Status Codes)`
        );

        $('#result-medication-dispense-category').html(
            `${medicationDispenseResource.category.coding[0].code} (${medicationDispenseResource.category.coding[0].system})`
        );

        $('#result-medication-dispense-type').html(
            `${medicationDispenseResource.type.coding[0].display} (${medicationDispenseResource.type.coding[0].system}#${medicationDispenseResource.type.coding[0].code})`
        );

        $('#result-medication-dispense-med').html(
            `${medicationDispenseResource.medicationReference.reference}`
        );

        $('#result-medication-dispense-patient').html(
            `${medicationDispenseResource.subject.reference}`
        );

        $('#result-medication-dispense-encounter').html(
            `${medicationDispenseResource.context.reference}`
        );

        $('#result-medication-dispense-practitioner').html(
            `${medicationDispenseResource.performer[0].actor.reference}`
        );

        $('#result-medication-dispense-value').html(
            `${medicationDispenseResource.quantity.value} ${medicationDispenseResource.quantity.unit} (${medicationDispenseResource.quantity.system}#${medicationDispenseResource.quantity.code})`
        );

        $('#result-medication-dispense-day').html(
            `${medicationDispenseResource.daysSupply.value} 天`
        );

        $('#result-medication-dispense-text').html(
            `${medicationDispenseResource.dosageInstruction[0].text}`
        );

        $('#result-medication-dispense-prepared').html(
            `${medicationDispenseResource.whenPrepared}`
        );

        $('#result-medication-dispense-hand-over').html(
            `${medicationDispenseResource.whenHandedOver}`
        );

        let mappingReplacement = {
            'true': '是',
            'false': '否',
        }
        $('#result-medication-dispense-replace').html(
            `${mappingReplacement[String(medicationDispenseResource.substitution.wasSubstituted)]}`
        );

        $('#result-medication-dispense-diff').html(
            `${medicationDispenseResource.substitution.type.coding[0].display} (${medicationDispenseResource.substitution.type.coding[0].system}#${medicationDispenseResource.substitution.type.coding[0].display})`
        );

        $('#result-medication-dispense-replace-reason').html(
            `${medicationDispenseResource.substitution.reason[0].coding[0].display} (${medicationDispenseResource.substitution.reason[0].coding[0].system}#${medicationDispenseResource.substitution.reason[0].coding[0].code})`
        );

        $('#search-result-card').removeClass('d-none');
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        $('button[name="generate-btn"]').each((_, element) => {
            $(element).removeAttr('disabled');
        });

        return false;
    });
}

async function doGenerateMedicationStatementRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage, roleType='source') {
    await $.ajax({
        url: `/track1/2024/${roleType}/MedicationStatement`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track1_server,
            oauth_token_info: oauthServerEndpoint['track#1'],
            oauth_level: $(`#${roleType}-token-level :selected`).val(),
            patient_payload: payload,
        }),
    }).done((data) => {
        let jsonData = data.json;
        let medicationStatementResource = jsonData;
        if (data.status !== 200 && data.status !== 201) {
            let htmlErrorMessage = `
                <p>error; HTTP status code: ${data.status}</p>
            `;
            for (let index=0; index<jsonData.issue.length; index++) {
                htmlErrorMessage += `<p class="text-danger">${jsonData.issue[index].severity}; ${jsonData.issue[index].diagnostics}</p>`;
            }
            errorMessage['html'] = htmlErrorMessage;

            Swal.fire(errorMessage);

            return false;
        }

        $('#result-medication-statement-id').html(medicationStatementResource.id);
        localStorage.setItem('created_medication_statement_id', medicationStatementResource.id);

        $('#result-medication-statement-status').html(
            `${medicationStatementResource.status} (Medication Status Codes)`
        );

        $('#result-medication-statement-category').html(
            `${medicationStatementResource.category.text} (${medicationStatementResource.category.coding[0].system}#${medicationStatementResource.category.coding[0].code})`
        );

        $('#result-medication-statement-med').html(
            `${medicationStatementResource.medicationCodeableConcept.text}(${medicationStatementResource.medicationCodeableConcept.coding[0].display}) (${medicationStatementResource.medicationCodeableConcept.coding[0].system}#${medicationStatementResource.medicationCodeableConcept.coding[0].code})`
        );

        $('#result-medication-statement-patient').html(
            `${medicationStatementResource.subject.reference}`
        );

        $('#result-medication-statement-use-datetime').html(
            `${medicationStatementResource.effectiveDateTime}`
        );

        $('#result-medication-statement-asserted').html(
            `${medicationStatementResource.dateAsserted}`
        );

        $('#result-medication-statement-use-reason').html(
            `${medicationStatementResource.reasonCode[0].text}(${medicationStatementResource.reasonCode[0].coding[0].display}) (${medicationStatementResource.reasonCode[0].coding[0].system}#${medicationStatementResource.reasonCode[0].coding[0].code})`
        );

        $('#result-medication-statement-freq').html(
            `${medicationStatementResource.dosage[0].text} (${medicationStatementResource.dosage[0].timing.repeat.frequency} per ${medicationStatementResource.dosage[0].timing.repeat.period} days)`
        );

        $('#result-medication-statement-use-approach').html(
            `${medicationStatementResource.dosage[0].route.text}(${medicationStatementResource.dosage[0].route.coding[0].display}) (${medicationStatementResource.dosage[0].route.coding[0].system}#${medicationStatementResource.dosage[0].route.coding[0].code})`
        );

        $('#result-medication-statement-note').html(
            `${medicationStatementResource.note[0].text}`
        );

        $('#search-result-card').removeClass('d-none');
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        $('button[name="generate-btn"]').each((_, element) => {
            $(element).removeAttr('disabled');
        });

        return false;
    });
}

async function doGenerateProcedureRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage, roleType='source') {
    await $.ajax({
        url: `/track1/2024/${roleType}/Procedure`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track1_server,
            oauth_token_info: oauthServerEndpoint['track#1'],
            oauth_level: $(`#${roleType}-token-level :selected`).val(),
            patient_payload: payload,
        }),
    }).done((data) => {
        let jsonData = data.json;
        let procedureResource = jsonData;
        if (data.status !== 200 && data.status !== 201) {
            let htmlErrorMessage = `
                <p>error; HTTP status code: ${data.status}</p>
            `;
            for (let index=0; index<jsonData.issue.length; index++) {
                htmlErrorMessage += `<p class="text-danger">${jsonData.issue[index].severity}; ${jsonData.issue[index].diagnostics}</p>`;
            }
            errorMessage['html'] = htmlErrorMessage;

            Swal.fire(errorMessage);

            return false;
        }

        $('#result-procedure-id').html(procedureResource.id);
        localStorage.setItem('created_procedure_id', procedureResource.id);

        $('#result-procedure-status').html(
            `${procedureResource.status}`
        );

        $('#result-procedure-coding').html(
            `${procedureResource.code.text} (${procedureResource.code.coding[0].system}#${procedureResource.code.coding[0].code})`
        );

        $('#result-procedure-patient').html(
            `${procedureResource.subject.reference}`
        );

        $('#result-procedure-performed-date').html(
            `${procedureResource.performedDateTime}`
        );

        $('#result-procedure-performed-asserter').html(
            `${procedureResource.asserter.reference}`
        );

        $('#result-procedure-performed-body-site').html(
            `${procedureResource.bodySite[0].coding[0].code} (${procedureResource.bodySite[0].coding[0].system})`
        );

        $('#result-procedure-practitioner').html(
            `${procedureResource.performer[0].actor.reference}`
        );

        $('#result-procedure-practitioner-org').html(
            `${procedureResource.performer[0].onBehalfOf.reference}`
        );

        $('#search-result-card').removeClass('d-none');
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        $('button[name="generate-btn"]').each((_, element) => {
            $(element).removeAttr('disabled');
        });

        return false;
    });
}

async function doGenerateSpecimenRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage, roleType='source') {
    await $.ajax({
        url: `/track1/2024/${roleType}/Specimen`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track1_server,
            oauth_token_info: oauthServerEndpoint['track#1'],
            oauth_level: $(`#${roleType}-token-level :selected`).val(),
            patient_payload: payload,
        }),
    }).done((data) => {
        let jsonData = data.json;
        let specimenResource = jsonData;
        if (data.status !== 200 && data.status !== 201) {
            let htmlErrorMessage = `
                <p>error; HTTP status code: ${data.status}</p>
            `;
            for (let index=0; index<jsonData.issue.length; index++) {
                htmlErrorMessage += `<p class="text-danger">${jsonData.issue[index].severity}; ${jsonData.issue[index].diagnostics}</p>`;
            }
            errorMessage['html'] = htmlErrorMessage;

            Swal.fire(errorMessage);

            return false;
        }

        $('#result-specimen-id').html(specimenResource.id);
        localStorage.setItem('created_specimen_id', specimenResource.id);

        $('#result-specimen-status').html(
            `${specimenResource.status} (SpecimenStatus)`
        );

        $('#result-specimen-identifier').html(
            `${specimenResource.identifier[0].value} (${specimenResource.identifier[0].system})`
        );

        $('#result-specimen-lab').html(
            `${specimenResource.accessionIdentifier.value}`
        );

        $('#result-specimen-type').html(
            `${specimenResource.type.coding[0].display} (${specimenResource.type.coding[0].system}#${specimenResource.type.coding[0].code})`
        );

        $('#result-specimen-patient').html(
            `${specimenResource.subject.reference} "${specimenResource.subject.display}"`
        );

        $('#result-specimen-clinical').html(
            `${specimenResource.collection.fastingStatusCodeableConcept.coding[0].display} (${specimenResource.collection.fastingStatusCodeableConcept.coding[0].system}#${specimenResource.collection.fastingStatusCodeableConcept.coding[0].code})`
        );

        $('#result-specimen-collector').html(
            `${specimenResource.collection.collector.reference} "${specimenResource.collection.collector.display}"`
        );

        $('#result-specimen-received-datetime').html(
            `${specimenResource.receivedTime}`
        );

        $('#result-specimen-collected-datetime').html(
            `${specimenResource.collection.collectedDateTime}`
        );

        $('#result-specimen-collected-approach').html(
            `${specimenResource.collection.method.coding[0].display} (${specimenResource.collection.method.coding[0].system}#${specimenResource.collection.method.coding[0].code})`
        );

        $('#result-specimen-collected-body-site').html(
            `${specimenResource.collection.bodySite.text} (${specimenResource.collection.bodySite.coding[0].system}#${specimenResource.collection.bodySite.coding[0].code})`
        );

        $('#result-specimen-collected-value').html(
            `${specimenResource.collection.quantity.value} ${specimenResource.collection.quantity.unit} (${specimenResource.collection.quantity.system}#${specimenResource.collection.quantity.code})`
        );

        let processingSteps = '';
        for (let index=0; index<specimenResource.processing.length; index++) {
            processingSteps += `
                <li>處理步驟(${index+1}): <span class="text-primary">${specimenResource.processing[index].description} (${specimenResource.processing[index].procedure.coding[0].system}#${specimenResource.processing[index].procedure.coding[0].code})</span></li>
                <li>檢體處理的日期時間(${index+1}): <span class="text-primary">${specimenResource.processing[index].timeDateTime}</span></li>`;
        }

        $('#processing-steps').html(processingSteps);

        let containerInfo = '';
        for (let index=0; index<specimenResource.container.length; index++) {
            containerInfo += `
                <ul class="card-text">
                    <li>容器類別: <span class="text-primary">${specimenResource.container[index].type.coding[0].display} (${specimenResource.container[index].type.coding[0].system}#${specimenResource.container[index].type.coding[0].code})</span></li>
                    <li>容器說明: <span class="text-primary">${specimenResource.container[index].description}</span></li>
                    <li>容器的大小: <span class="text-primary">${specimenResource.container[index].capacity.value} ${specimenResource.container[index].capacity.unit} (${specimenResource.container[index].capacity.system}#${specimenResource.container[index].capacity.code})</span></li>
                    <li>容器檢體量: <span class="text-primary">${specimenResource.container[index].specimenQuantity.value} ${specimenResource.container[index].specimenQuantity.unit} (${specimenResource.container[index].specimenQuantity.system}#${specimenResource.container[index].specimenQuantity.code})</span></li>
                </ul>
            `;
        }

        $('#containers').html(containerInfo);

        $('#result-specimen-note').html(
            `${specimenResource.note[0].text}`
        );

        $('#search-result-card').removeClass('d-none');
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        $('button[name="generate-btn"]').each((_, element) => {
            $(element).removeAttr('disabled');
        });

        return false;
    });
}

async function doGenerateObservationVitalBloodPressureRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage, roleType='source') {
    await $.ajax({
        url: `/track1/2024/${roleType}/ObservationVital`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track1_server,
            oauth_token_info: oauthServerEndpoint['track#1'],
            oauth_level: $(`#${roleType}-token-level :selected`).val(),
            patient_payload: payload,
        }),
    }).done((data) => {
        let jsonData = data.json;
        let observationResource = jsonData;
        if (data.status !== 200 && data.status !== 201) {
            let htmlErrorMessage = `
                <p>error; HTTP status code: ${data.status}</p>
            `;
            for (let index=0; index<jsonData.issue.length; index++) {
                htmlErrorMessage += `<p class="text-danger">${jsonData.issue[index].severity}; ${jsonData.issue[index].diagnostics}</p>`;
            }
            errorMessage['html'] = htmlErrorMessage;

            Swal.fire(errorMessage);

            return false;
        }

        $('#result-observation-id').html(observationResource.id);
        localStorage.setItem('created_observation_vital_id', observationResource.id);

        $('#result-observation-status').html(
            `${observationResource.status}`
        );

        $('#result-observation-category').html(
            `${observationResource.category[0].coding[0].display} (${observationResource.category[0].coding[0].system}#${observationResource.category[0].coding[0].code})`
        );

        $('#result-observation-item').html(
            `${observationResource.code.text} (${observationResource.code.coding[0].system}#${observationResource.code.coding[0].code})`
        );

        $('#result-observation-patient').html(
            `${observationResource.subject.reference}`
        );

        $('#result-observation-performer').html(
            `${observationResource.performer[0].reference}`
        );

        $('#result-observation-effective-date').html(
            `${observationResource.effectiveDateTime}`
        );

        let observationResult = '';
        for (let index=0; index<observationResource.component.length; index++) {
            observationResult += `
                <ul class="card-text">
                    <li">檢驗項目: <span class="text-primary">${observationResource.component[index].code.coding[0].display} (${observationResource.component[index].code.coding[0].system}#${observationResource.component[index].code.coding[0].code})</span></li>
                    <li>檢驗值: <span class="text-primary">${observationResource.component[index].valueQuantity.value} ${observationResource.component[index].valueQuantity.unit} (${observationResource.component[index].valueQuantity.system}#${observationResource.component[index].valueQuantity.code})</span></li>
                </ul>
            `;
        }

        $('#observation-result').html(observationResult);

        $('#search-result-card').removeClass('d-none');
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        $('button[name="generate-btn"]').each((_, element) => {
            $(element).removeAttr('disabled');
        });

        return false;
    });
}

async function doGenerateObservationLabReportRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage, roleType='source') {
    await $.ajax({
        url: `/track1/2024/${roleType}/ObservationLabReport`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track1_server,
            oauth_token_info: oauthServerEndpoint['track#1'],
            oauth_level: $(`#${roleType}-token-level :selected`).val(),
            patient_payload: payload,
        }),
    }).done((data) => {
        let jsonData = data.json;
        let observationResource = jsonData;
        if (data.status !== 200 && data.status !== 201) {
            let htmlErrorMessage = `
                <p>error; HTTP status code: ${data.status}</p>
            `;
            for (let index=0; index<jsonData.issue.length; index++) {
                htmlErrorMessage += `<p class="text-danger">${jsonData.issue[index].severity}; ${jsonData.issue[index].diagnostics}</p>`;
            }
            errorMessage['html'] = htmlErrorMessage;

            Swal.fire(errorMessage);

            return false;
        }

        $('#result-observation-id').html(observationResource.id);
        localStorage.setItem('created_observation_lab_id', observationResource.id);

        $('#result-observation-status').html(
            `${observationResource.status}`
        );

        $('#result-observation-category').html(
            `${observationResource.category[0].coding[0].code} (${observationResource.category[0].coding[0].system})`
        );

        $('#result-observation-item').html(
            `${observationResource.code.text} (${observationResource.code.coding[0].system}#${observationResource.code.coding[0].code})`
        );

        $('#result-observation-patient').html(
            `${observationResource.subject.reference}`
        );

        $('#result-observation-performer').html(
            `${observationResource.performer[0].reference}`
        );

        $('#result-observation-effective-date').html(
            `${observationResource.effectiveDateTime}`
        );

        $('#result-observation-value').html(
            `${observationResource.valueQuantity.value} ${observationResource.valueQuantity.unit}`
        );

        $('#search-result-card').removeClass('d-none');
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        $('button[name="generate-btn"]').each((_, element) => {
            $(element).removeAttr('disabled');
        });

        return false;
    });
}
