async function loadMartialStatus() {
    await $.ajax({
        url: '/front_end/assets/json/CodeSystem-v3-MaritalStatus.json',
        method: 'GET',
        headers: {'Content-Type': 'application/json'},
    }).done((data) => {
        let jsonData = data;
        $('#patient-martial-status-coding').val(JSON.stringify(jsonData.concept));
    }).fail((error) => {
        console.log(error);
    });
}

async function loadRelationshipCoding() {
    await $.ajax({
        url: '/front_end/assets/json/CodeSystem-v3-RoleCode.json',
        method: 'GET',
        headers: {'Content-Type': 'application/json'},
    }).done((data) => {
        let jsonData = data;
        $('#contact-relationship-coding').val(JSON.stringify(jsonData.concept));
    }).fail((error) => {
        console.log(error);
    });
}
