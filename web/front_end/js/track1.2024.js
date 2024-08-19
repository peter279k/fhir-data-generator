async function doGenerateRequest(trackServerEndpoint, oauthServerEndpoint, patientPayload, errorMessage) {
    await $.ajax({
        url: `/track1/2024/source/Patient`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track2_server,
            oauth_token_info: oauthServerEndpoint['track#2'],
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
            oauth_token_info: oauthServerEndpoint['track#2'],
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
