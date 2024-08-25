async function doGenerateRequest(trackServerEndpoint, oauthServerEndpoint, patientPayload, errorMessage, roleType='source') {
    await $.ajax({
        url: `/track13/2024/${roleType}/Patient`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track1_server,
            oauth_token_info: oauthServerEndpoint['track#13'],
            oauth_level: $(`#${roleType}-token-level :selected`).val(),
            patient_payload: patientPayload,
        }),
    }).done((data) => {
        let jsonData = data.json;
        if (jsonData.total === 0) {
            errorMessage['text'] = '尚未找到任何筆數！';
            Swal.fire(errorMessage);
            return false;
        }
        let patientResource = jsonData;
        if (jsonData.entry) {
            patientResource = jsonData.entry[0].resource;
        }

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

        $('#result-patient-id').html(patientResource.id);
        localStorage.setItem('created_patient_id', patientResource.id);

        let identifiers = patientResource.identifier;
        let identifierHtml = '';
        identifierHtml += `<li>病患識別碼型別: <span name="result-patient-identifier" class="text-primary">${identifiers[0].type.coding[0].system}#${identifiers[0].type.coding[0].code}</span></li>`;
        identifierHtml += `<li>身份證字號: <span name="result-patient-identifier" class="text-primary">${identifiers[0].value}</span></li>`;

        $('#result-patient-identifier1').html(identifierHtml);

        $('#result-patient-active').html(patientResource.active);
        $('#result-patient-name').html(`${patientResource.name[0].text}`);

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

        $('#search-result-card').removeClass('d-none');

        $('p[name="result-text"]').each((_, element) => {
            let htmlContent = $(element).html();
            if (patientPayload.patient_type === 'patient') {
                htmlContent = htmlContent.replace(/會員/g, '病人');
            } else {
                htmlContent = htmlContent.replace(/病人/g, '會員');
            }
            $(element).html(htmlContent);
        });
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        $('button[name="generate-btn"]').each((_, element) => {
            $(element).removeAttr('disabled');
        });

        return false;
    });
}

async function doGenerateOrganizationRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage, roleType='source') {
    await $.ajax({
        url: `/track13/2024/${roleType}/Organization`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track1_server,
            oauth_token_info: oauthServerEndpoint['track#13'],
            oauth_level: $(`#${roleType}-token-level :selected`).val(),
            patient_payload: payload,
        }),
    }).done((data) => {
        let jsonData = data.json;
        if (jsonData.total === 0) {
            errorMessage['text'] = '尚未找到任何筆數！';
            Swal.fire(errorMessage);
            return false;
        }
        let organizationResource = jsonData;
        if (jsonData.entry) {
            organizationResource = jsonData.entry[0].resource;
        }

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

        $('#result-organization-id').html(organizationResource.id);
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

async function doGeneratePractitionerRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage, roleType='source') {
    await $.ajax({
        url: `/track13/2024/${roleType}/Practitioner`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track1_server,
            oauth_token_info: oauthServerEndpoint['track#13'],
            oauth_level: $(`#${roleType}-token-level :selected`).val(),
            patient_payload: payload,
        }),
    }).done((data) => {
        let jsonData = data.json;
        if (jsonData.total === 0) {
            errorMessage['text'] = '尚未找到任何筆數！';
            Swal.fire(errorMessage);
            return false;
        }
        let practitionerResource = jsonData;
        if (jsonData.entry) {
            practitionerResource = jsonData.entry[0].resource;
        }

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

        $('#result-practitioner-id').html(practitionerResource.id);
        localStorage.setItem('created_practitioner_id', practitionerResource.id);

        let identifiers = practitionerResource.identifier;
        let identifierHtml = '';
        identifierHtml += `<li>識別碼型別: <span name="result-practitioner-identifier" class="text-primary">${identifiers[0].type.coding[0].system}#${identifiers[0].type.coding[0].code}</span></li>`;
        identifierHtml += `<li>員工編號: <span name="result-practitioner-identifier" class="text-primary">${identifiers[0].value}</span></li>`;

        $('#result-practitioner-identifier2').html(identifierHtml);

        $('#result-practitioner-active').html(practitionerResource.active);

        $('#result-practitioner-name').html(
            `${practitionerResource.name[0].text}`
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
