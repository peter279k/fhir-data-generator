async function doGenerateLocationRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage) {
    await $.ajax({
        url: `/track1/2024/source/Location`,
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
        let locationResource = jsonData;
        if (data.status !== 200 && data.status !== 201) {
            errorMessage['text'] = `error; HTTP status code: ${data.status}`;
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

        return false;
    });
}

async function doGenerateMediaRequest(trackServerEndpoint, oauthServerEndpoint, payload, errorMessage) {
    await $.ajax({
        url: `/track1/2024/source/Media`,
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
        let mediaResource = jsonData;
        if (data.status !== 200 && data.status !== 201) {
            errorMessage['text'] = `error; HTTP status code: ${data.status}`;
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

        return false;
    });
}
