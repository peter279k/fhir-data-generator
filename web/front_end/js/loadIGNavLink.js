function loadIGNavLink() {
    let resources = {
        'allergyintolerance.html': 'AllergyIntolerance',
        'condition.html': 'Condition',
        'diagnosticreport.html': 'DiagnosticReport',
        'documentreference.html': 'DocumentReference',
        'encounter.html': 'Encounter',
        'imagingstudy.html': 'ImagingStudy',
        'location.html': 'Location',
        'media.html': 'Media',
        'medicationdispense.html': 'MedicationDispense',
        'medication.html': 'Medication',
        'medicationrequest.html': 'MedicationRequest',
        'medicationstatement.html': 'MedicationStatement',
        'observation_vital.html': 'ObservationVital',
        'observation_lab_result.html': 'ObservationLab',
        'organization.html': 'Organization',
        'patient.html': 'Patient',
        'practitioner.html': 'Practitioner',
        'practitionerrole.html': 'PractitionerRole',
        'procedure.html': 'Procedure',
        'specimen.html': 'Specimen',
    };

    let navLinkContent = '<nav class="sb-sidenav-menu-nested nav">';
    let resourceName = null;
    for (key in resources) {
        resourceName = resources[key];
        navLinkContent += `<a class="nav-link" href="/front_end/2024/track1/${key}">${resourceName}</a>`;
    }
    navLinkContent += '</nav>';

    $('#collapseLayouts').html(navLinkContent);

    navLinkContent = '<nav class="sb-sidenav-menu-nested nav">';
    resourceName = null;
    resources = {
        'patient.html': 'Patient',
        'practitioner.html': 'Practitioner',
        'organization.html': 'Organization',
        'goal.html': 'Goal',
        'careplan.html': 'CarePlan',
        'observation_vital.html': 'Observation',
        'servicerequest.html': 'ServiceRequest',
    };
    for (key in resources) {
        resourceName = resources[key];
        navLinkContent += `<a class="nav-link" href="/front_end/2024/track13/${key}">${resourceName}</a>`;
    }

    $('#collapseLayouts3').html(navLinkContent);

    $('div.sb-sidenav-menu-heading').each((index, element) => {
        if ($(element).text().split(' ').length > 1 && index === 0) {
            $(element).text('系統設定');
        }
    });

    $('a.nav-link').each((index, element) => {
        if (index === 0 && $(element).text().includes('基本設定')) {
            $(element).after(
                `<div class="sb-sidenav-menu-heading">系統</div>
                    <a class="nav-link" href="/front_end/2024/log.html">
                        <div class="sb-nav-link-icon"><i class="fas fa-book"></i></div>
                        Resource log
                    </a>`
            );
        }
    });
}
