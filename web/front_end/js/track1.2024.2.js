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
