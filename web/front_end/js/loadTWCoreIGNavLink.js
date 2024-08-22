function loadTWCoreIGNavLink() {
    let resources = {
        'allergyintolerance.html': 'AllergyIntolerance',
        'composition.html': 'Composition',
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
        'observation_vital.html': 'Observation',
        'observation_lab_result.html': 'Observation',
        'organization.html': 'Organization',
        'patient.html': 'Patient',
        'practitioner.html': 'Practitioner',
        'practitionerrole.html': 'PractitionerRole',
        'procedure.html': 'Procedure',
        'specimen.html': 'Specimen',
    };

    let navLinkContent = '';
    let resourceName = null;
    for (key in resources) {
        resourceName = resources[key];
        navLinkContent += `<nav class="sb-sidenav-menu-nested nav">
            <a class="nav-link" href="/front_end/2024/track1/${key}">${resourceName}</a>
        </nav>`;
    }

    $('#collapseLayouts').html(navLinkContent);
}
