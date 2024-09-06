async function doSubmitRequest(currentFormName, warningMessage, errorMessage, trackServerEndpoint, oauthServerEndpoint, searchParameters, type='consumer') {
    await $.ajax({
        url: `/track2/2024/${currentFormName}`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track2_server,
            oauth_token_info: oauthServerEndpoint['track#2'],
            oauth_level: (
                type === 'consumer' ? $('#token-level :selected').val() : $('#source-token-level :selected').val()
            ),
            search_parameters: searchParameters,
        }),
    }).done((data) => {
        let jsonData = data.json;
        if (data.status !== 200) {
            errorMessage['text'] = `error; HTTP status code: ${data.status}`;
            Swal.fire(errorMessage);

            return false;
        }
        if (jsonData.total < 1) {
            warningMessage['text'] = `使用查詢參數${searchParameters}未找到紀錄！`;
            Swal.fire(warningMessage);
            $('#search-result-card').addClass('d-none');
        } else {
            let patientResource = jsonData.entry[0].resource;
            $('#search-result-card').removeClass('d-none');
            if (type === 'consumer') {
                $('#result-card-header').text('查詢結果');
                $('button[name="delete-btn"]').addClass('d-none');
            }

            let prefix = '#result-patient-';
            $(`${prefix}id`).text(patientResource['id']);

            $('#meta-version').attr('patient_id', patientResource['id']);

            let identifiers = patientResource['identifier'];
            let identifier = null;
            let identifierHtml = '';
            let codingSystem = [];
            for (index in identifiers) {
                identifier = identifiers[index];
                if (identifier['type']) {
                    codingSystem = [
                        identifier['type']['coding'][0]['system'],
                        identifier['type']['coding'][0]['code'],
                    ];
                    identifierHtml += `<li>病患識別碼identifier: <span name="result-patient-identifier" class="text-primary">${identifier['value']}(代碼系統：${codingSystem[0]}, ${codingSystem[1] || '無提供'})</span></li>`;
                } else {
                    identifierHtml += `<li>病患識別碼identifier: <span name="result-patient-identifier" class="text-primary">${identifier['value']}</span></li>`;
                }
            }
            $(`${prefix}identifier`).html(identifierHtml);

            let active = patientResource.active;
            if (active === true) {
                active = '使用中';
            }
            if (active === false) {
                active = '未使用';
            }

            let gender = patientResource.gender;
            if (gender === 'male') {
                gender = '男性';
            }
            if (gender === 'female') {
                gender = '女性';
            }

            $(`${prefix}name`).text(`${patientResource.name[0].text}`);
            $(`${prefix}active`).text(`${active || '未填寫'}`);
            $(`${prefix}gender`).text(`${gender || '未填寫'}`);
            $(`${prefix}birth-date`).text(`${patientResource.birthDate || '未填寫'}`);

            if (patientResource.managingOrganization) {
                $(`${prefix}managing-organization`).text(`${patientResource.managingOrganization.reference}`);
            } else {
                $(`${prefix}managing-organization`).text('未填寫');
            }

            if (patientResource.communication) {
                $(`${prefix}communication`).text(`${patientResource.communication[0].language.coding[0].code}(代碼標籤：${patientResource.communication[0].language.coding[0].system})`);
            } else {
                $(`${prefix}communication`).text('未填寫');
            }

            if (patientResource.telecom) {
                $(`${prefix}telecom`).text(`${patientResource.telecom[0].value}(${patientResource.telecom[0].use})`);
            } else {
                $(`${prefix}telecom`).text('未填寫');
            }

            if (patientResource.address) {
                $(`${prefix}address`).text(`${patientResource.address[0].text}`);
            } else {
                $(`${prefix}address`).text('未填寫');
            }

            if (patientResource.contact) {
                $(`${prefix}contact`).text(`${patientResource.contact[0].name.text}(代碼系統：${patientResource.contact[0].relationship[0].coding[0].system}, ${patientResource.contact[0].relationship[0].coding[0].code})`);
            } else {
                $(`${prefix}contact`).text('未填寫');
            }

            if (patientResource.deceasedBoolean) {
                $(`${prefix}deceased`).text(`${patientResource.deceasedBoolean}`);
            } else {
                $(`${prefix}deceased`).text('未填寫');
            }

            if (patientResource.maritalStatus) {
                $(`${prefix}marital-status`).text(`${patientResource.maritalStatus.coding[0].code}(代碼系統：${patientResource.maritalStatus.coding[0].system})`);
            } else {
                $(`${prefix}marital-status`).text('未填寫');
            }

            if (patientResource.photo) {
                let patientPhoto = `data:${patientResource.photo[0].contentType};base64,${patientResource.photo[0].data}`;
                $(`${prefix}photo`).html(
                    `病患照片photo: <img src="${patientPhoto}" class="img-thumbnail" alt="result patient photo">`
                );
            } else {
                $(`${prefix}photo`).html('病患照片photo: <span class="text-primary">未填寫</span>');
            }

            let metaVersions = Number(patientResource.meta.versionId);
            let metaVersionOptions = '<option value="0">請選擇歷史紀錄版本</option>';
            for (let index=1; index<=metaVersions; index++) {
                metaVersionOptions += `<option value="${index}">版本${index}</option>`;
            }

            $('#result-meta-version-id').text(metaVersions);
            $('#meta-version').html(metaVersionOptions);
        }
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);
    });
}

async function doMetaVersionRequest(currentFormName, trackServerEndpoint, oauthServerEndpoint, searchParameters, errorMessage) {
    await $.ajax({
        url: `/track2/2024/${currentFormName}`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track2_server,
            oauth_token_info: oauthServerEndpoint['track#2'],
            oauth_level: $('#token-level :selected').val(),
            search_parameters: searchParameters,
        })
    }).done((data) => {
        let jsonData = data.json;
        if (data.status !== 200) {
            errorMessage['text'] = `error; HTTP status code: ${data.status}`;
            Swal.fire(errorMessage);

            return false;
        }

        let patientResource = jsonData;
        $('#search-result-card').removeClass('d-none');
        $('#result-card-header').text('查詢結果');
        $('button[name="delete-btn"]').addClass('d-none');

        let prefix = '#result-patient-';
        $(`${prefix}id`).text(patientResource['id']);

        let identifiers = patientResource['identifier'];
        let identifier = null;
        let identifierHtml = '';
        let codingSystem = [];
        for (index in identifiers) {
            identifier = identifiers[index];
            if (identifier['type']) {
                codingSystem = [
                    identifier['type']['coding'][0]['system'],
                    identifier['type']['coding'][0]['code'],
                ];
                identifierHtml += `<li>病患識別碼identifier: <span name="result-patient-identifier" class="text-primary">${identifier['value']}(代碼系統：${codingSystem[0]}, ${codingSystem[1] || '無提供'})</span></li>`;
            } else {
                identifierHtml += `<li>病患識別碼identifier: <span name="result-patient-identifier" class="text-primary">${identifier['value']}</span></li>`;
            }
        }
        $(`${prefix}identifier`).html(identifierHtml);

        let active = patientResource.active;
        if (active === true) {
            active = '使用中';
        }
        if (active === false) {
            active = '未使用';
        }

        let gender = patientResource.gender;
        if (gender === 'male') {
            gender = '男性';
        }
        if (gender === 'female') {
            gender = '女性';
        }

        $(`${prefix}name`).text(`${patientResource.name[0].text}`);
        $(`${prefix}active`).text(`${active || '未填寫'}`);
        $(`${prefix}gender`).text(`${gender || '未填寫'}`);
        $(`${prefix}birth-date`).text(`${patientResource.birthDate || '未填寫'}`);
        $('#result-meta-version-id').text(patientResource.meta.versionId);

        if (patientResource.managingOrganization) {
            $(`${prefix}managing-organization`).text(`${patientResource.managingOrganization.reference}`);
        } else {
            $(`${prefix}managing-organization`).text('未填寫');
        }

        if (patientResource.communication) {
            $(`${prefix}communication`).text(`${patientResource.communication[0].language.coding[0].code}(代碼標籤：${patientResource.communication[0].language.coding[0].system})`);
        } else {
            $(`${prefix}communication`).text('未填寫');
        }

        if (patientResource.telecom) {
            $(`${prefix}telecom`).text(`${patientResource.telecom[0].value}`);
        } else {
            $(`${prefix}telecom`).text('未填寫');
        }

        if (patientResource.address) {
            $(`${prefix}address`).text(`${patientResource.address[0].text}`);
        } else {
            $(`${prefix}address`).text('未填寫');
        }

        if (patientResource.contact) {
            $(`${prefix}contact`).text(`${patientResource.contact[0].name.text}(代碼系統：${patientResource.contact[0].relationship[0].coding[0].system}, ${patientResource.contact[0].relationship[0].coding[0].code})`);
        } else {
            $(`${prefix}contact`).text('未填寫');
        }

        if (patientResource.deceasedBoolean) {
            $(`${prefix}deceased`).text(`${patientResource.deceasedBoolean}`);
        } else {
            $(`${prefix}deceased`).text('未填寫');
        }

        if (patientResource.maritalStatus) {
            $(`${prefix}marital-status`).text(`${patientResource.maritalStatus.coding[0].code}(代碼系統：${patientResource.contact[0].relationship[0].coding[0].system})`);
        } else {
            $(`${prefix}marital-status`).text('未填寫');
        }

        if (patientResource.photo) {
            let patientPhoto = `data:${patientResource.photo[0].contentType};base64,${patientResource.photo[0].data}`;
            $(`${prefix}photo`).html(
                `病患照片photo: <img src="${patientPhoto}" class="img-thumbnail" alt="result patient photo">`
            );
        } else {
            $(`${prefix}photo`).html('病患照片photo: <span class="text-primary">未填寫</span>');
        }

    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);
    });
}

async function doGenerateRequest(currentFormName, trackServerEndpoint, oauthServerEndpoint, patientPayload, errorMessage) {
    if (patientPayload.id) {
        $('#result-card-header').text('更新結果');
        $('#result-search-parameters').text('更新資料，故無查詢參數');
    } else {
        $('#result-card-header').text('新增結果');
        $('#result-search-parameters').text('新增資料，故無查詢參數');
    }

    await $.ajax({
        url: `/track2/2024/source/${currentFormName}`,
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
        if (data.status !== 200 && data.status !== 201) {
            errorMessage['text'] = `error; HTTP status code: ${data.status}`;
            Swal.fire(errorMessage);

            return false;
        }

        let patientResource = jsonData;
        $('#search-result-card').removeClass('d-none');
        $('#meta-version-selector').addClass('d-none');
        $('button[name="delete-btn"]').removeClass('d-none');

        localStorage.setItem('created_patient_id', patientResource['id']);
        $('#put-patient-id').val(patientResource['id']);
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        return false;
    });
}

async function doDeleteRequest(currentFormName, trackServerEndpoint, oauthServerEndpoint, patientId, errorMessage, successMessage) {
    await $.ajax({
        url: `/track2/2024/delete_source/${currentFormName}`,
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        data: JSON.stringify({
            fhir_server: trackServerEndpoint.track2_server,
            oauth_token_info: oauthServerEndpoint['track#2'],
            oauth_level: $('#source-token-level :selected').val(),
            patient_id: patientId,
        }),
    }).done((data) => {
        let jsonData = data.json;
        if (data.status !== 200 && data.status !== 201) {
            errorMessage['text'] = `error; HTTP status code: ${data.status}`;
            Swal.fire(errorMessage);
            console.log(jsonData);

            return false;
        }

        successMessage['text'] = `Patient id：${patientId}已經刪除！`;
        Swal.fire(successMessage);
        $('#search-result-card').addClass('d-none');
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);

        return false;
    });
}
