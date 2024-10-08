async function doGenerateRequest(trackServerEndpoint, oauthServerEndpoint, patientPayload, errorMessage, roleType='source') {
    await $.ajax({
        url: `/track1/2024/${roleType}/Patient`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track1_server,
            oauth_token_info: oauthServerEndpoint['track#1'],
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
            $('#result-card-header').html(`總共查到${jsonData.total || jsonData.entry.length}筆資料，顯示第1筆資料`);
            $('#result-search-entries').text(JSON.stringify(jsonData.entry));

            let entryOptions = '';
            for (let index=0; index<jsonData.entry.length; index++) {
                entryOptions += `
                    <option value=${index}>${index+1}</option>
                `;
            }
            $('#entries-counter').html(entryOptions);
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

        try {
            let identifiers = patientResource.identifier;
            let identifierHtml = '';
            identifierHtml += `<li>病患識別碼型別: <span name="result-patient-identifier" class="text-primary">${identifiers[0].type.coding[0].system}#${identifiers[0].type.coding[0].code}</span></li>`;
            identifierHtml += `<li>身份證字號: <span name="result-patient-identifier" class="text-primary">${identifiers[0].value}</span></li>`;

            $('#result-patient-identifier1').html(identifierHtml);

            identifierHtml = '';
            identifierHtml += `<li>病患識別碼型別: <span name="result-patient-identifier" class="text-primary">${identifiers[1].type.coding[0].system}#${identifiers[1].type.coding[0].code}</span></li>`;
            identifierHtml += `<li>病歷號: <span name="result-patient-identifier" class="text-primary">${identifiers[1].value}</span></li>`;

            $('#result-patient-identifier2').html(identifierHtml);
        } catch {
            $('#result-patient-identifier1').html('無');
            $('#result-patient-identifier2').html('無');
        }

        $('#result-patient-active').html(patientResource.active);

        try {
            $('#result-patient-name').html(`${patientResource.name[0].text} ${patientResource.name[0].family}, ${patientResource.name[0].given[0]}`);
        } catch {
            $('#result-patient-name').html('');
        }

        let genderMapping = {
            'male': '男性',
            'female': '女性',
        };
        $('#result-patient-gender').html(genderMapping[patientResource.gender]);

        $('#result-patient-birth-date').html(patientResource.birthDate);

        try {
            $('#result-patient-age').html(
                `[extension: ${patientResource.extension[0].url}]: ${patientResource.extension[0].valueAge.value}`
            );
        } catch {
            $('#result-patient-age').html('無');
        }

        try {
            $('#result-patient-nationality').html(
                `[extension: ${patientResource.extension[1].url}]: ${patientResource.extension[1].extension[0].valueCodeableConcept.coding[0].code}`
            );
        } catch {
            $('#result-patient-nationality').html('無');
        }

        try {
            $('#result-patient-phone').html(
                `${patientResource.telecom[0].system}`
            )
        } catch {
            $('#result-patient-phone').html('');
        }

        try {
            $('#result-patient-mobile').html(
                `${patientResource.telecom[0].value}`
            )
        } catch {
            $('#result-patient-mobile').html('無');
        }

        try {
            $('#result-patient-period').html(
                `${patientResource.telecom[0].period.start}~${patientResource.telecom[0].period.end}`
            )
        } catch {
            $('#result-patient-period').html('無');
        }

        try {
            $('#result-patient-address').html(
                `(${patientResource.address[0]._postalCode.extension[0].valueCodeableConcept.coding[0].code})${patientResource.address[0].text}`
            );
            $('#result-patient-address-postal').html(
                `${patientResource.address[0]._postalCode.extension[0].valueCodeableConcept.coding[0].code}`
            );
            $('#result-patient-address-city').html(
                `${patientResource.address[0].district}`
            );
            $('#result-patient-address-district').html(
                `${patientResource.address[0].city}`
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
        } catch {
            $('#result-patient-address').html('');
            $('#result-patient-address-postal').html('');
            $('#result-patient-address-city').html('');
            $('#result-patient-address-district').html('');
            $('#result-patient-address-line').html('');
            $('#result-patient-address-country').html('');
        }

        try {
            $('#result-patient-address-martial').html(
                `${patientResource.maritalStatus.coding[0].code}(${patientResource.maritalStatus.coding[0].system})`
            );
        } catch {
            $('#result-patient-address-martial').html('無');
        }

        try {
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
        } catch {
            $('#result-patient-contact-name').html('');
            $('#result-patient-contact-relationship').html('');
            $('#result-patient-contact-phone').html('');
            $('#result-patient-contact-mobile').html('');
            $('#result-patient-contact-period').html('');
        }

        try {
            $('#result-patient-communication').html(
                patientResource.communication[0].language.coding[0].code
            );
        } catch {
            $('#result-patient-communication').html('');
        }

        try {
            $('#result-patient-managing-organization').html(
                patientResource.managingOrganization.reference
            );
        } catch {
            $('#result-patient-managing-organization').html('');
        }

        try {
            $('#result-patient-photo').attr(
                'src',
                `data:${patientResource.photo[0].contentType};base64, ${patientResource.photo[0].data}`
            );
        } catch {
            $('#result-patient-photo').attr('src', '');
        }

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

async function doGenerateOrganizationRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage, roleType='source') {
    await $.ajax({
        url: `/track1/2024/${roleType}/Organization`,
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
        if (jsonData.total === 0) {
            errorMessage['text'] = '尚未找到任何筆數！';
            Swal.fire(errorMessage);
            return false;
        }
        let organizationResource = jsonData;
        if (jsonData.entry) {
            organizationResource = jsonData.entry[0].resource;
            $('#result-card-header').html(`總共查到${jsonData.total || jsonData.entry.length}筆資料，顯示第1筆資料`);
            $('#result-search-entries').text(JSON.stringify(jsonData.entry));

            let entryOptions = '';
            for (let index=0; index<jsonData.entry.length; index++) {
                entryOptions += `
                    <option value=${index}>${index+1}</option>
                `;
            }
            $('#entries-counter').html(entryOptions);
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

        try {
            $('#result-prn-identifier').html(
                `${organizationResource.identifier[0].type.coding[0].code} (${organizationResource.identifier[0].type.coding[0].system})`
            );
        } catch {
            $('#result-prn-identifier').html('無');
        }

        $('#result-prn-number').html(
            `${organizationResource.identifier[0].value} (${organizationResource.identifier[0].system})`
        );

        $('#result-patient-prn-coding').html(
            `${organizationResource.type[0].coding[0].code} (${organizationResource.type[0].coding[0].system})`
        );

        if (organizationResource.telecom) {
            $('#result-phone').html(
                `${organizationResource.telecom[0].system}`
            );
            $('#result-phone-number').html(
                `${organizationResource.telecom[0].value}`
            );
        } else {
            $('#result-phone').html('無');
            $('#result-phone-number').html('無');
        }

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
        url: `/track1/2024/${roleType}/Practitioner`,
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
        if (jsonData.total === 0) {
            errorMessage['text'] = '尚未找到任何筆數！';
            Swal.fire(errorMessage);
            return false;
        }
        let practitionerResource = jsonData;
        if (jsonData.entry) {
            practitionerResource = jsonData.entry[0].resource;
            $('#result-card-header').html(`總共查到${jsonData.total || jsonData.entry.length}筆資料，顯示第1筆資料`);
            $('#result-search-entries').text(JSON.stringify(jsonData.entry));

            let entryOptions = '';
            for (let index=0; index<jsonData.entry.length; index++) {
                entryOptions += `
                    <option value=${index}>${index+1}</option>
                `;
            }
            $('#entries-counter').html(entryOptions);
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

        try {
            $('#result-practitioner-address').html(
                `(${practitionerResource.address[0]._postalCode.extension[0].valueCodeableConcept.coding[0].code})${practitionerResource.address[0].text}`
            );
            $('#result-practitioner-postal').html(
                `${practitionerResource.address[0]._postalCode.extension[0].valueCodeableConcept.coding[0].code} (${practitionerResource.address[0]._postalCode.extension[0].valueCodeableConcept.coding[0].system})`
            );
        } catch {
            $('#result-practitioner-address').html('');
            $('#result-practitioner-postal').html('');
        }

        $('#result-practitioner-district').html(practitionerResource.address[0].district);
        $('#result-practitioner-city').html(practitionerResource.address[0].city);
        $('#result-practitioner-road').html(practitionerResource.address[0].line[0]);

        try {
            $('#result-practitioner-number').html(
                practitionerResource.address[0].extension[0].valueString
            );
        } catch {
            $('#result-practitioner-number').html('');
        }

        $('#result-practitioner-country').html(practitionerResource.address[0].country);

        try {
            $('#result-practitioner-qualification').html(
                `${practitionerResource.qualification[0].code.coding[0].display} (${practitionerResource.qualification[0].code.coding[0].system}#${practitionerResource.qualification[0].code.coding[0].code})`
            );
        } catch {
            $('#result-practitioner-qualification').html('');
        }

        try {
            $('#result-practitioner-qualification-start').html(
                practitionerResource.qualification[0].period.start
            );
        } catch {
            $('#result-practitioner-qualification-start').html('');
        }

        try {
            $('#result-practitioner-photo').attr(
                'src',
                `data:${practitionerResource.photo[0].contentType};base64, ${practitionerResource.photo[0].data}`
            );
        } catch {
            $('#result-practitioner-photo').attr('src', '');
        }

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

async function doGeneratePractitionerRoleRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage, roleType='source') {
    await $.ajax({
        url: `/track1/2024/${roleType}/PractitionerRole`,
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
        if (jsonData.total === 0) {
            errorMessage['text'] = '尚未找到任何筆數！';
            Swal.fire(errorMessage);
            return false;
        }
        let practitionerRoleResource = jsonData;
        if (jsonData.entry) {
            practitionerRoleResource = jsonData.entry[0].resource;
            $('#result-card-header').html(`總共查到${jsonData.total || jsonData.entry.length}筆資料，顯示第1筆資料`);
            $('#result-search-entries').text(JSON.stringify(jsonData.entry));

            let entryOptions = '';
            for (let index=0; index<jsonData.entry.length; index++) {
                entryOptions += `
                    <option value=${index}>${index+1}</option>
                `;
            }
            $('#entries-counter').html(entryOptions);
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

        $('#result-practitioner-role-id').html(practitionerRoleResource.id);
        localStorage.setItem('created_practitioner_id', practitionerRoleResource.id);

        try {
            let identifiers = practitionerRoleResource.identifier;
            let identifierHtml = '';
            identifierHtml += `<li>識別碼型別: <span name="result-practitioner-role-identifier" class="text-primary">${identifiers[0].type.coding[0].system}#${identifiers[0].type.coding[0].code}</span></li>`;
            identifierHtml += `<li>員工編號: <span name="result-practitioner-identifier" class="text-primary">${identifiers[0].value}</span></li>`;

            $('#result-practitioner-role-identifier1').html(identifierHtml);
        } catch {
            $('#result-practitioner-role-identifier1').html('無');
        }

        $('#result-practitioner-role-active').html(practitionerRoleResource.active);

        $('#result-practitioner-role-business').html(
            `${practitionerRoleResource.period.start} ~ ${practitionerRoleResource.period.end}`
        );

        $('#result-practitioner').html(
            `${practitionerRoleResource.practitioner.reference} "${practitionerRoleResource.practitioner.display}"`
        );

        try {
            $('#result-practitioner-role-location').html(
                `${practitionerRoleResource.location[0].reference} "${practitionerRoleResource.location[0].display}"`
            );
        } catch {
            $('#result-practitioner-role-location').html('');
        }

        try {
            $('#result-practitioner-role').html(
                `${practitionerRoleResource.code[0].coding[0].display} (${practitionerRoleResource.code[0].coding[0].system}#${practitionerRoleResource.code[0].coding[0].code})`
            );
        } catch {
            $('#result-practitioner-role').html('');
        }

        try {
            $('#result-practitioner-role-profession').html(
                `${practitionerRoleResource.specialty[0].coding[0].display} (${practitionerRoleResource.specialty[0].coding[0].system}#${practitionerRoleResource.code[0].coding[0].code})`
            );
        } catch {
            $('#result-practitioner-role-profession').html('');
        }

        try {
            $('#result-practitioner-role-phone').html(
                `${practitionerRoleResource.telecom[0].system}`
            );
        } catch {
            $('#result-practitioner-role-phone').html('');
        }

        try {
            $('#result-practitioner-role-phone-number').html(
                `(${practitionerRoleResource.telecom[0].use}) ${practitionerRoleResource.telecom[0].value}`
            );
        } catch {
            $('#result-practitioner-role-phone-number').html('');
        }

        try {
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
        } catch {
            $('#result-practitioner-role-business-contact').html('');
        }

        try {
            $('#result-practitioner-role-message').html(
                practitionerRoleResource.availabilityExceptions
            );
        } catch {
            $('#result-practitioner-role-message').html('');
        }

        try {
            $('#result-practitioner-role-unavailable').html(
                `${practitionerRoleResource.notAvailable[0].during.start} ~ ${practitionerRoleResource.notAvailable[0].during.end}`
            );
        } catch {
            $('#result-practitioner-role-unavailable').html('');
        }

        try {
            $('#result-practitioner-role-unavailable-reason').html(
                practitionerRoleResource.notAvailable[0].description
            );
        } catch {
            $('#result-practitioner-role-unavailable-reason').html('');
        }

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

async function doGenerateEncounterRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage, roleType='source') {
    await $.ajax({
        url: `/track1/2024/${roleType}/Encounter`,
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
        if (jsonData.total === 0) {
            errorMessage['text'] = '尚未找到任何筆數！';
            Swal.fire(errorMessage);
            return false;
        }
        let encounterResource = jsonData;
        if (jsonData.entry) {
            encounterResource = jsonData.entry[0].resource;
            $('#result-card-header').html(`總共查到${jsonData.total || jsonData.entry.length}筆資料，顯示第1筆資料`);
            $('#result-search-entries').text(JSON.stringify(jsonData.entry));

            let entryOptions = '';
            for (let index=0; index<jsonData.entry.length; index++) {
                entryOptions += `
                    <option value=${index}>${index+1}</option>
                `;
            }
            $('#entries-counter').html(entryOptions);
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

        $('#result-encounter-id').html(encounterResource.id);
        localStorage.setItem('created_encounter_id', encounterResource.id);

        if (encounterResource.identifier) {
            $('#result-encounter-identifier').html(
                encounterResource.identifier[0].value
            );
        } else {
            $('#result-encounter-identifier').html('無');
        }

        $('#result-encounter-type').html(
            encounterResource.status
        );

        $('#result-encounter-class').html(
            `${encounterResource.class.code} (${encounterResource.class.system})`
        );

        if (encounterResource.type) {
            $('#result-encounter-category').html(
                `${encounterResource.type[0].coding[0].code} (${encounterResource.type[0].coding[0].system})`
            );
        } else {
            $('#result-encounter-category').html('無');
        }

        if (encounterResource.serviceType) {
            $('#result-encounter-service-type').html(
                `${encounterResource.serviceType.text}(${encounterResource.serviceType.coding[0].display}) (${encounterResource.serviceType.coding[0].system}#${encounterResource.serviceType.coding[0].code})`
            );
        } else {
            $('#result-encounter-service-type').html('無');
        }

        $('#result-encounter-subject').html(
            `${encounterResource.subject.reference}`
        );

        try {
            $('#result-encounter-hos').html(
                `${encounterResource.hospitalization.dischargeDisposition.coding[0].code}(${encounterResource.hospitalization.dischargeDisposition.coding[0].system})`
            );
        } catch {
            $('#result-encounter-hos').html('');
        }

        if (encounterResource.location) {
            $('#result-encounter-location').html(
                `${encounterResource.location[0].location.reference}`
            );
        } else {
            $('#result-encounter-location').html('');
        }

        try {
            $('#result-encounter-participant-performer').html(
                `${encounterResource.participant[0].type[0].coding[0].code} (${encounterResource.participant[0].type[0].coding[0].system})`
            );
        } catch {
            $('#result-encounter-participant-performer').html('');
        }

        try {
            $('#result-encounter-participant-period').html(
                `${encounterResource.participant[0].period.start} --> ${encounterResource.participant[0].period.end}`
            );
        } catch {
            $('#result-encounter-participant-period').html('');
        }

        try {
            $('#result-encounter-participant').html(
                `${encounterResource.participant[0].individual.reference}`
            );
        } catch {
            $('#result-encounter-participant').html('');
        }

        try {
            $('#result-encounter-hos-period').html(
                `${encounterResource.period.start} --> ${encounterResource.period.end}`
            );
        } catch {
            $('#result-encounter-hos-period').html('');
        }

        try {
            $('#result-encounter-reason').html(
                `${encounterResource.reasonCode[0].coding[0].display} (${encounterResource.reasonCode[0].coding[0].system}#${encounterResource.reasonCode[0].coding[0].code})`
            );
        } catch {
            $('#result-encounter-reason').html('');
        }

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

async function doGenerateAllergyIntoleranceRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage, roleType='source') {
    await $.ajax({
        url: `/track1/2024/${roleType}/AllergyIntolerance`,
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
        if (jsonData.total === 0) {
            errorMessage['text'] = '尚未找到任何筆數！';
            Swal.fire(errorMessage);
            return false;
        }
        let allergyResource = jsonData;
        if (jsonData.entry) {
            allergyResource = jsonData.entry[0].resource;
            $('#result-card-header').html(`總共查到${jsonData.total }筆資料，顯示第1筆資料`);
            $('#result-search-entries').text(JSON.stringify(jsonData.entry));

            let entryOptions = '';
            for (let index=0; index<jsonData.entry.length; index++) {
                entryOptions += `
                    <option value=${index}>${index+1}</option>
                `;
            }
            $('#entries-counter').html(entryOptions);
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

        if (allergyResource.recorder) {
            $('#result-allergy-recorder').html(
                `${allergyResource.recorder.reference} "${allergyResource.recorder.display}"`
            );
        } else {
            $('#result-allergy-recorder').html('無');
        }

        $('#result-allergy-recorder-datetime').html(allergyResource.recordedDate);

        if (allergyResource.asserter) {
            $('#result-allergy-practitioner').html(
                `${allergyResource.asserter.reference} "${allergyResource.asserter.display}"`
            );
        } else {
            $('#result-allergy-practitioner').html('無');
        }

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

        if (allergyResource.reaction[0].exposureRoute) {
            $('#result-allergy-mainfest').html(
                `${allergyResource.reaction[0].exposureRoute.text} (${allergyResource.reaction[0].exposureRoute.coding[0].display}) (${allergyResource.reaction[0].exposureRoute.coding[0].system}#${allergyResource.reaction[0].exposureRoute.coding[0].code})`
            );
        } else {
            $('#result-allergy-mainfest').html('');
        }

        $('#result-allergy-note').html(
            `${allergyResource.reaction[0].note[0].text}`
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

async function doGenerateConditionRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage, roleType='source') {
    await $.ajax({
        url: `/track1/2024/${roleType}/Condition`,
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
        if (jsonData.total === 0) {
            errorMessage['text'] = '尚未找到任何筆數！';
            Swal.fire(errorMessage);
            return false;
        }
        let conditionResource = jsonData;
        if (jsonData.entry) {
            conditionResource = jsonData.entry[0].resource;
            $('#result-card-header').html(`總共查到${jsonData.total || jsonData.entry.length}筆資料，顯示第1筆資料`);
            $('#result-search-entries').text(JSON.stringify(jsonData.entry));

            let entryOptions = '';
            for (let index=0; index<jsonData.entry.length; index++) {
                entryOptions += `
                    <option value=${index}>${index+1}</option>
                `;
            }
            $('#entries-counter').html(entryOptions);
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

        $('#result-condition-id').html(conditionResource.id);
        localStorage.setItem('created_condition_id', conditionResource.id);

        $('#result-condition-clinical').html(
            `${conditionResource.clinicalStatus.coding[0].code} (${conditionResource.clinicalStatus.coding[0].system})`
        );

        if (conditionResource.verificationStatus) {
            $('#result-condition-verification-status').html(
                `${conditionResource.verificationStatus.coding[0].code} (${conditionResource.verificationStatus.coding[0].system})`
            );
        } else {
            $('#result-condition-verification-status').html('無');
        }

        $('#result-condition-diagnosis').html(
            `${conditionResource.category[0].coding[0].code} (${conditionResource.category[0].coding[0].system})`
        );

        if (conditionResource.severity) {
            $('#result-condition-code').html(
                `${conditionResource.severity.coding[0].code} (${conditionResource.severity.coding[0].system})`
            );
        } else {
            $('#result-condition-code').html('無');
        }

        $('#result-condition-message').html(
            `${conditionResource.code.text} (${conditionResource.code.coding[0].system}#${conditionResource.code.coding[0].code})`
        );

        $('#result-condition-patient').html(
            `${conditionResource.subject.reference}`
        );

        $('#result-condition-onset-datetime').html(
            `${conditionResource.onsetDateTime || '無'}`
        );

        $('#result-condition-abatement-datetime').html(
            `${conditionResource.abatementDateTime || '無'}`
        );

        $('#result-condition-asserter').html(
            `${conditionResource.asserter.reference}`
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

async function doGenerateDiagnosticReportRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage, roleType='source') {
    await $.ajax({
        url: `/track1/2024/${roleType}/DiagnosticReport`,
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
        if (jsonData.total === 0) {
            errorMessage['text'] = '尚未找到任何筆數！';
            Swal.fire(errorMessage);
            return false;
        }
        let diagnosticReportResource = jsonData;
        if (jsonData.entry) {
            diagnosticReportResource = jsonData.entry[0].resource;
            $('#result-card-header').html(`總共查到${jsonData.total || jsonData.entry.length}筆資料，顯示第1筆資料`);
            $('#result-search-entries').text(JSON.stringify(jsonData.entry));

            let entryOptions = '';
            for (let index=0; index<jsonData.entry.length; index++) {
                entryOptions += `
                    <option value=${index}>${index+1}</option>
                `;
            }
            $('#entries-counter').html(entryOptions);
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

        $('button[name="generate-btn"]').each((_, element) => {
            $(element).removeAttr('disabled');
        });

        return false;
    });
}

async function doGenerateDocumentReferenceRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage, roleType='source') {
    await $.ajax({
        url: `/track1/2024/${roleType}/DocumentReference`,
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
        if (jsonData.total === 0) {
            errorMessage['text'] = '尚未找到任何筆數！';
            Swal.fire(errorMessage);
            return false;
        }
        let documentReferenceResource = jsonData;
        if (jsonData.entry) {
            documentReferenceResource = jsonData.entry[0].resource;
            $('#result-card-header').html(`總共查到${jsonData.total || jsonData.entry.length}筆資料，顯示第1筆資料`);
            $('#result-search-entries').text(JSON.stringify(jsonData.entry));

            let entryOptions = '';
            for (let index=0; index<jsonData.entry.length; index++) {
                entryOptions += `
                    <option value=${index}>${index+1}</option>
                `;
            }
            $('#entries-counter').html(entryOptions);
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

        try {
            $('#result-document-practitioner').html(
                `${documentReferenceResource.author[0].reference}`
            );
        } catch {
            $('#result-document-practitioner').html('');
        }

        try {
            $('#result-document-organization').html(
                `${documentReferenceResource.custodian.reference}`
            );
        } catch {
            $('#result-document-organization').html('');
        }

        try {
            $('#result-document-content-file-type').html(
                `${documentReferenceResource.content[0].attachment.contentType}`
            );
        } catch {
            $('#result-document-content-file-type').html('');
        }

        try {
            $('#result-document-content-file').html(
                `${documentReferenceResource.content[0].attachment.url} (${documentReferenceResource.content[0].attachment.title})`
            );
        } catch {
            $('#result-document-content-file').html('');
        }

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

async function doGenerateImagingStudyRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage, roleType='source') {
    await $.ajax({
        url: `/track1/2024/${roleType}/ImagingStudy`,
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
        if (jsonData.total === 0) {
            errorMessage['text'] = '尚未找到任何筆數！';
            Swal.fire(errorMessage);
            return false;
        }
        let ImagingStudyResource = jsonData;
        if (jsonData.entry) {
            ImagingStudyResource = jsonData.entry[0].resource;
            $('#result-card-header').html(`總共查到${jsonData.total || jsonData.entry.length}筆資料，顯示第1筆資料`);
            $('#result-search-entries').text(JSON.stringify(jsonData.entry));

            let entryOptions = '';
            for (let index=0; index<jsonData.entry.length; index++) {
                entryOptions += `
                    <option value=${index}>${index+1}</option>
                `;
            }
            $('#entries-counter').html(entryOptions);
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

        $('#result-imaging-id').html(ImagingStudyResource.id);
        localStorage.setItem('created_imaging_study_id', ImagingStudyResource.id);

        $('#result-imaging-status').html(
            `${ImagingStudyResource.status} (ImagingStudyStatus)`
        );

        if (ImagingStudyResource.identifier) {
            $('#result-imaging-identifier').html(
                `${ImagingStudyResource.identifier[0].value} (${ImagingStudyResource.identifier[0].use})`
            );
        } else {
            $('#result-imaging-identifier').html('無identifier');
        }

        $('#result-imaging-start').html(
            `${ImagingStudyResource.started}`
        );

        $('#result-imaging-patient').html(
            `${ImagingStudyResource.subject.reference}`
        );

        try {
            $('#result-imaging-encounter').html(
                `${ImagingStudyResource.encounter.reference}`
            );
        } catch {
            $('#result-imaging-encounter').html('');
        }

        $('#result-imaging-series').html(
            `${ImagingStudyResource.numberOfSeries || '無'}`
        );

        $('#result-imaging-instances').html(
            `${ImagingStudyResource.numberOfInstances || '無'}`
        );

        if (ImagingStudyResource.procedureReference) {
            $('#result-imaging-procedure').html(
                `${ImagingStudyResource.procedureReference.reference}`
            );
        } else {
            $('#result-imaging-procedure').html('無');
        }

        if (ImagingStudyResource.procedureCode && ImagingStudyResource.procedureCode[0].coding) {
            $('#result-imaging-procedure-code').html(
                `${ImagingStudyResource.procedureCode[0].coding[0].display} (${ImagingStudyResource.procedureCode[0].coding[0].system}#${ImagingStudyResource.procedureCode[0].coding[0].code})`
            );
        }
        else {
            $('#result-imaging-procedure-code').html('無');
        }

        if (ImagingStudyResource.series && ImagingStudyResource.series[0].performer) {
            $('#result-imaging-dicom-uid').html(
                `${ImagingStudyResource.series[0].uid}`
            );

            $('#result-imaging-device').html(
                `${ImagingStudyResource.series[0].modality.system}#${ImagingStudyResource.series[0].modality.code}`
            );

            $('#result-imaging-body-site').html(
                `${ImagingStudyResource.series[0].bodySite.display} (${ImagingStudyResource.series[0].bodySite.system}#${ImagingStudyResource.series[0].bodySite.code})`
            );

            try {
                $('#result-imaging-body-practitioner').html(
                    `${ImagingStudyResource.series[0].performer[0].actor.reference}`
                );
            } catch {
                $('#result-imaging-body-practitioner').html('');
            }

            try {
                $('#result-imaging-body-sop-uid').html(
                    `${ImagingStudyResource.series[0].instance[0].uid}`
                );
            } catch {
                $('#result-imaging-body-sop-uid').html('');
            }

            try {
                $('#result-imaging-body-sop-class').html(
                    `${ImagingStudyResource.series[0].instance[0].sopClass.code}`
                );
            } catch {
                $('#result-imaging-body-sop-class').html('');
            }
        } else {
            $('#result-imaging-dicom-uid').html('無');

            $('#result-imaging-device').html('無');

            $('#result-imaging-body-site').html('無');

            $('#result-imaging-body-practitioner').html('無');

            $('#result-imaging-body-sop-uid').html('無');

            $('#result-imaging-body-sop-class').html('無');
        }

        $('#search-result-card').removeClass('d-none');
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        $('button[name="generate-btn"]').each((_, element) => {
            $(element).removeAttr('disabled');
        });

        return false;
    })
}
