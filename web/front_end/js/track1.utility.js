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
