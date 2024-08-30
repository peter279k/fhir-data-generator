function extractAddress(address) {
    let addressExtension = [];
    for (let index=0; index<address.length; index++) {
        if (address[index] === '段') {
            addressExtension.push({
                'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-section',
                'valueString': `${address[index-1]}段`,
            });
        } else if (address[index] === '號') {
            let start = index-1;
            let number = '';
            while (!isNaN(address[start])) {
                number = address[start] + number;
                start -= 1;
            }
            addressExtension.push({
                'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-number',
                'valueString': `${number}號`,
            });
        } else if (address[index] === '里') {
            addressExtension.push(        {
                'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-village',
                'valueString': `${address[index-2]}${address[index-1]}里`,
            });
        } else if (address[index] === '鄰') {
            let start = index-1;
            let number = '';
            while (!isNaN(address[start])) {
                number = address[start] + number;
                start -= 1;
            }
            addressExtension.push({
                'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-neighborhood',
                'valueString': `${number}鄰`,
            });
        } else if (address[index] === '巷') {
            let start = index-1;
            let number = '';
            while (!isNaN(address[start])) {
                number = address[start] + number;
                start -= 1;
            }
            addressExtension.push({
                'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-lane',
                'valueString': `${number}巷`,
            });
        } else if (address[index] === '弄') {
            let start = index-1;
            let number = '';
            while (!isNaN(address[start])) {
                number = address[start] + number;
                start -= 1;
            }
            addressExtension.push({
                'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-alley',
                'valueString': `${number}弄`,
            });
        } else if (address[index] === '樓') {
            let start = index-1;
            let number = '';
            while (!isNaN(address[start])) {
                number = address[start] + number;
                start -= 1;
            }
            addressExtension.push({
                'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-floor',
                'valueString': `${number}樓`,
            });
        } else if (address[index] === '室') {
            let alphabets = 'abcdefghijklmnopqrstuvwxyz';
            let start = index-1;
            let number = '';
            while (!isNaN(address[start]) || alphabets.includes(address[start].toLowerCase())) {
                number = address[start] + number;
                start -= 1;
            }
            addressExtension.push({
                'url': 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-room',
                'valueString': `${number}室`,
            });
        }
    }

    return addressExtension;
}

async function loadCodeSystemModal() {
    let parsedUrl = new URL(location.href);
    let pathName = parsedUrl.pathname.toLowerCase();
    let tracks = ['track1'];
    let resources = [
        'Condition', 'DiagnosticReport', 'ImagingStudy', 'Medication',
        'MedicationRequest', 'MedicationStatement', 'observation_lab_result',
        'Organization', 'Procedure', 'Location', 'Practitioner', 'Patient',
    ];
    let resourceMappingCodeSystemJson = {
        'Condition': 'CodeSystem-icd-10-cm-2021-tw.json',
        'DiagnosticReport': 'CodeSystem-medical-service-payment-tw.json',
        'ImagingStudy': 'CodeSystem-icd-10-pcs-2021-tw.json',
        'Medication': 'CodeSystem-medication-fda-tw.json',
        'MedicationRequest': 'CodeSystem-medication-fda-tw.json',
        'MedicationStatement': 'CodeSystem-medication-nhi-tw.json',
        'observation_lab_result': 'CodeSystem-medical-service-payment-tw.json',
        'Organization': 'CodeSystem-organization-identifier-tw.json',
        'Procedure': 'CodeSystem-icd-10-pcs-2021-tw.json',
        'Location': 'tw_postal_1031225.json',
        'Practitioner': 'tw_postal_1031225.json',
        'Patient': 'tw_postal_1031225.json',
    };
    let resourceMappingCodeSystemLabel = {
        'Condition': '請輸入病情、問題或診斷識別代碼',
        'DiagnosticReport': '',
        'ImagingStudy': '',
        'Medication': '',
        'MedicationRequest': '',
        'MedicationStatement': '',
        'observation_lab_result': '',
        'Organization': '',
        'Procedure': '',
        'Location': '',
        'Practitioner': '',
        'Patient': '',
    };
    let codeSystemJson = '';
    let codeSystemLabel = '';

    let matched = false;
    for (let index in tracks) {
        if (pathName.includes(tracks[index])) {
            matched = true;
            break;
        }
    }

    if (!matched) {
        return false;
    }

    matched = false;
    let pathResource = '';
    for (let index in resources) {
        pathResource = pathName.split('/');
        pathResource = pathResource[pathResource.length-1].split('.');
        if (pathResource[0].toLowerCase() === resources[index].toLowerCase()) {
            matched = true;
            codeSystemJson = resourceMappingCodeSystemJson[resources[index]];
            codeSystemLabel = resourceMappingCodeSystemLabel[resources[index]];
            break;
        }
    }

    if (!matched) {
        return false;
    }

    await $.ajax({
        type: 'GET',
        url: `/front_end/assets/json/${codeSystemJson}`,
        headers: {'Accept': 'application/json'},
    }).done((data) => {
        let jsonData = data;
        let codeOptions = [];
        for (let index=0; index<jsonData.concept.length; index++) {
            codeOptions.push({
                code: jsonData.concept[index].code,
                display: jsonData.concept[index].display,
                label: `${jsonData.concept[index].display}(${jsonData.concept[index].code})`,
            });
        }
        localStorage.setItem('code_system', JSON.stringify(codeOptions));
        $('#source-form').after(
            `<div class="modal fade" id="coding-system-modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
                <div class="modal-dialog modal-lg">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h1 class="modal-title fs-5" id="staticBackdropLabel">代碼查詢</h1>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="關閉"></button>
                        </div>
                        <div class="modal-body">
                            <form id="code-system-form" role="form">
                                <div class="mb-3">
                                    <label for="for-code" class="form-label">${codeSystemLabel}</label>
                                    <input id="for-code" class="form-control autocomplete" type="text" aria-label="">
                                </div>
                            </form>
                        </div>
                        <div class="modal-footer justify-content-center">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">關閉</button>
                            <button type="button" id="use-code-btn" class="btn btn-primary">使用代碼</button>
                        </div>
                    </div>
                </div>
            </div>`
        );
    }).fail((error) => {
        errorMessage['text'] = `${error.status} ${error.statusText}`;
        Swal.fire(errorMessage);
    });

    $('#coding-system-btn').remove();
    $('#source-form').append(
        `<button id="coding-system-btn" type="button" class="btn btn-info" data-bs-toggle="modal" data-bs-target="#coding-system-modal">
            代碼查詢
        </button>
        `
    );

    $(document).on('click', '#coding-system-btn', (e) => {
        e.preventDefault();
        $('#for-code').val('');
    });

    return {
        items: JSON.parse(localStorage.getItem('code_system')),
        showAllSuggestions: false,
        suggestionsThreshold: 2,
        autoselectFirst: true,
        updateOnSelect: false,
        preventBrowserAutocomplete: true,
        valueField: 'label',
        labelField: 'label',
        searchFields: ['code', 'display'],
    };
}
