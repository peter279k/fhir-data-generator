function loadObservationOptions() {
    let observationMapping = {
        '基礎生理量測': [{'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/ServiceRequest-sport', 'value': 'servicerequest', 'name': '服務請求'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/Condition-medical-history', 'value': 'condition', 'name': '病史'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/Condition-excercise-history', 'value': 'condition', 'name': '運動史'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/Goal-sport', 'value': 'goal', 'name': '運動目標'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/Careplan-sport', 'value': 'careplan', 'name': '運動計畫'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/TWCoreOrganization', 'value': 'organization', 'name': '醫院'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/TWCoreOrganization', 'value': 'organization', 'name': '場館'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/TWCorePractitioner', 'value': 'practitioner', 'name': '醫師'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/TWCorePractitioner', 'value': 'practitioner', 'name': '教練'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/TWCorePatient', 'value': 'patient', 'name': '病人'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/TWCorePatient', 'value': 'patient', 'name': '會員'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/Height-sport', 'value': 'height', 'name': '身高'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/Weight-sport', 'value': 'weight', 'name': '體重'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/Waist-sport', 'value': 'waist', 'name': '腰圍'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/BloodPressure-sport', 'value': 'bloodpressure', 'name': '血壓'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/SpO2-sport', 'value': 'spo2', 'name': '脈搏血氧飽和度'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/Glucose-sport', 'value': 'glucose', 'name': '血糖'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/HeartRate-sport', 'value': 'heartrate', 'name': '心率'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/RestingHeartRate-sport', 'value': 'restingheartrate', 'name': '安靜心率'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/MeanHeartRate-sport', 'value': 'meanheartrate', 'name': '平均心率'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/HRV-sport', 'value': 'heartratevariability', 'name': '心率變異性'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/BodyTemperature-sport', 'value': 'temperature', 'name': '體溫'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/RespiratoryRate-sport', 'value': 'respiratoryrate', 'name': '呼吸速率'}].slice(11),
        '身體組成分析儀': [{'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/TBW-sport', 'value': 'tbw', 'name': '身體總水分'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/ICW-sport', 'value': 'icw', 'name': '細胞內水分'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/ECW-sport', 'value': 'ecw', 'name': '細胞外水分'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/Protein-sport', 'value': 'protein', 'name': '蛋白質重'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/Mineral-sport', 'value': 'mineral', 'name': '礦物質重'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/BodyFatMass-sport', 'value': 'bodyfatmass', 'name': '體脂肪重'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/SMM-sport', 'value': 'smm', 'name': '骨骼肌重'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/SMI-sport', 'value': 'smi', 'name': '肌肉質量指數'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/BMI-sport', 'value': 'bmi', 'name': '身體質量指數'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/PBF-sport', 'value': 'bpf', 'name': '體脂率'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/BMR-sport', 'value': 'bmr', 'name': '基礎代謝率'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/FFM-sport', 'value': 'ffm', 'name': '去脂體重'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/VFI-sport', 'value': 'vfi', 'name': '內臟脂肪指數'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/VFA-sport', 'value': 'vfa', 'name': '內臟脂肪面積'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/WHR-sport', 'value': 'whr', 'name': '腰臀圍比'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/ObesityDegree-sport', 'value': 'obseitydegree', 'name': '肥胖度'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/BodyAge-sport', 'value': 'bodyage', 'name': '體內年齡'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/SLM-sport', 'value': 'slm', 'name': '肌肉量'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/BodyCellMass-sport', 'value': 'bodycellmass', 'name': '細胞量'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/BodyBoneMass-sport', 'value': 'bonemass', 'name': '推定骨量'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/ECWRatio-sport', 'value': 'ecwratio', 'name': '水腫指數'}],
        '穿戴裝置': [{'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/GaitCycle-sport', 'value': 'gaitcycle-l', 'name': '左腳步態週期'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/GaitCycle-sport', 'value': 'gaitcycle-r', 'name': '右腳步態週期'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/GaitType-sport', 'value': 'gaittype-l', 'name': '左腳步態分析'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/GaitType-sport', 'value': 'gaittype-r', 'name': '右腳步態分析'}],
        '運動項目': [{'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/Treadmill-sport', 'value': 'treadmill', 'name': '跑步機'}, {'profile_url': 'https://hapi.fhir.tw/fhir/StructureDefinition/WeightTraining-sport', 'value': 'weighttraining', 'name': '重量訓練'}],
    };

    return observationMapping;
}

async function loadObservationBasicInfo(observationMapping) {
    let exampleJsonMapping = {};
    let jsonUrl = '';
    for (key in observationMapping) {
        for (let index=0; index<observationMapping[key].length; index++) {
            jsonUrl = `/front_end/assets/json/physical_activity/observation-${observationMapping[key][index].value}-example.json`;
            await $.ajax({
                url: jsonUrl,
                method: 'GET',
                headers: {'Accept': 'application/json'},
            }).done((data) => {
                exampleJsonMapping[observationMapping[key][index].value] = data;
            });
        }
    }

    return exampleJsonMapping;
}

function loadCategoryAndCodeCoding(exampleJsonMapping) {
    let categoryMapping = {};
    let codeMapping = {};

    let exampleJson = {};
    for (key in exampleJsonMapping) {
        exampleJson = exampleJsonMapping[key];
        categoryMapping[key] = {
            system: exampleJson.category[0].coding[0].system,
            code: exampleJson.category[0].coding[0].code,
            display: exampleJson.category[0].coding[0].display,
        };
        codeMapping[key] = {
            system: exampleJson.code.coding[0].system,
            code: exampleJson.code.coding[0].code,
            display: exampleJson.code.coding[0].display,
            text: exampleJson.code.text,
        };
    }

    return {
        category_mapping: categoryMapping,
        code_mapping: codeMapping,
    };
}

function loadObservationValueQuantityForm(observationMapping) {
    let valueQuantityMapping = {};
    let mapping = {
        // [value, unit, code]
        '身高': [160, 'cm', 'cm'],
        '體重': [50, 'kg', 'kg'],
        '腰圍': [63, 'cm', 'cm'],
        '脈搏血氧飽和度': [38, '%', '%'],
        '血糖': [80, 'mg/dL', 'mg/dL'],
        '心率': [80, '/min', '/min'],
        '安靜心率': [50, '/min', '/min'],
        '平均心率': [75, '/min', '/min'],
        '心率變異性': [50, 'ms', 'ms'],
        '體溫': [36.5, 'C', 'Cel'],
        '呼吸速率': [15, 'min', '/min'],
        '身體總水分': [23.9, 'kg', 'kg'],
        '細胞內水分': [14.7, 'kg', 'kg'],
        '細胞外水分': [9.2, 'kg', 'kg'],
        '蛋白質重': [6.4, 'kg', 'kg'],
        '礦物質重': [2.3, 'kg', 'kg'],
        '體脂肪重': [14.3, 'kg', 'kg'],
        '骨骼肌重': [17.3, 'kg', 'kg'],
        '肌肉質量指數': [5.1, 'kg/m2', 'kg/m2'],
        '身體質量指數': [18.8, 'kg/m2', 'kg/m2'],
        '體脂率': [30.4, '%', '%'],
        '基礎代謝率': [1075, 'kcal', 'kcal'],
        '去脂體重': [32.6, 'kg', 'kg'],
        '內臟脂肪指數': [5, null, null],
        '內臟脂肪面積': [37, 'cm2', 'cm2'],
        '腰臀圍比': [0.79, null, null],
        '肥胖度': [-15, '%', '%'],
        '體內年齡': [26, null, null],
        '肌肉量': [30.9, 'kg', 'kg'],
        '細胞量': [23.5, 'kg', 'kg'],
        '推定骨量': [2.6, 'kg', 'kg'],
        '水腫指數': [0.384, null, null],
    };

    let leftRightMapping = {
        '左': [60, 40],
        '右': [58, 42],
    }

    let leftRightAnalysisMapping = {
        '左': [29, 0, 71],
        '右': [62, 38, 0],
    }

    let tempContents = '';

    for (key in observationMapping) {
        for (let index=0; index<observationMapping[key].length; index++) {
            if (observationMapping[key][index].name === '血壓') {
                valueQuantityMapping[observationMapping[key][index].value] = `
                <div class="mb-3">
                    <label for="value-quantity-coding1" class="form-label">請輸入收縮壓檢驗值代碼</label>
                    <input type="text" class="form-control" disabled="disabled" value="mm[Hg]" id="value-quantity-coding1">
                </div>
                <div class="mb-3">
                    <label for="value-quantity-unit1" class="form-label">請輸入收縮壓檢驗值單位</label>
                    <input type="text" class="form-control" disabled="disabled" value="mmHg" id="value-quantity-unit1">
                </div>
                <div class="mb-3">
                    <label for="value-quantity-value1" class="form-label">請輸入收縮壓檢驗值</label>
                    <input type="text" class="form-control" placeholder="110" id="value-quantity-value1">
                </div>
                <div class="mb-3">
                    <label for="value-quantity-coding2" class="form-label">請輸入舒張壓檢驗值代碼</label>
                    <input type="text" class="form-control" disabled="disabled" value="mm[Hg]" id="value-quantity-coding2">
                </div>
                <div class="mb-3">
                    <label for="value-quantity-unit2" class="form-label">請輸入舒張壓檢驗值單位</label>
                    <input type="text" class="form-control" disabled="disabled" value="mmHg" id="value-quantity-unit2">
                </div>
                <div class="mb-3">
                    <label for="value-quantity-value2" class="form-label">請輸入舒張壓檢驗值</label>
                    <input type="text" class="form-control" placeholder="56" id="value-quantity-value2">
                </div>
                `;
            } else if (Object.keys(mapping).includes(observationMapping[key][index].name)) {
                valueQuantityMapping[observationMapping[key][index].value] = `
                    <div class="mb-3">
                        <label for="value-quantity-coding1" class="form-label">請輸入檢驗值代碼</label>
                        <input type="text" class="form-control" disabled="disabled" value="${mapping[observationMapping[key][index].name][2]}" id="value-quantity-coding1">
                    </div>
                    <div class="mb-3">
                        <label for="value-quantity-unit1" class="form-label">請輸入檢驗值單位</label>
                        <input type="text" class="form-control" disabled="disabled" value="${mapping[observationMapping[key][index].name][1]}" id="value-quantity-unit1">
                    </div>
                    <div class="mb-3">
                        <label for="value-quantity-value1" class="form-label">請輸入檢驗值</label>
                        <input type="text" class="form-control" placeholder="${mapping[observationMapping[key][index].name][0]}" id="value-quantity-value1">
                    </div>
                    `;
                if (observationMapping[key][index].name === '身體總水分') {
                    valueQuantityMapping[observationMapping[key][index].value] += `
                    <div class="mb-3">
                        <label for="value-quantity-icw" class="fw-bold text-info form-label">請輸入ICW參照</label>
                        <input type="text" class="form-control" placeholder="Observation/ICW-example" id="value-quantity-icw">
                    </div>
                    <div class="mb-3">
                        <label for="value-quantity-ecw" class="fw-bold text-info form-label">請輸入ECW參照</label>
                        <input type="text" class="form-control" placeholder="Observation/ECW-example" id="value-quantity-ecw">
                    </div>
                    `;
                }
            } else if (observationMapping[key][index].name === '左腳步態週期' || observationMapping[key][index].name === '右腳步態週期') {
                valueQuantityMapping[observationMapping[key][index].value] = `
                <div class="mb-3">
                    <label for="value-quantity-value1" class="form-label">請輸入支撐期</label>
                    <input type="text" class="form-control" placeholder="${leftRightMapping[observationMapping[key][index].name[0]][0]}" id="value-quantity-value1">
                </div>
                <div class="mb-3">
                    <label for="value-quantity-coding1" class="form-label">請輸入支撐期代碼</label>
                    <input type="text" class="form-control" value="1" disabled="disabled" id="value-quantity-coding1">
                </div>
                <div class="mb-3">
                    <label for="value-quantity-unit1" class="form-label">請輸入支撐期單位</label>
                    <input type="text" class="form-control" value="%" disabled="disabled" id="value-quantity-unit1">
                </div>
                <div class="mb-3">
                    <label for="value-quantity-value2" class="form-label">請輸入擺動期</label>
                    <input type="text" class="form-control" placeholder="${leftRightMapping[observationMapping[key][index].name[0]][1]}" id="value-quantity-value2">
                </div>
                <div class="mb-3">
                    <label for="value-quantity-coding2" class="form-label">請輸入擺動期代碼</label>
                    <input type="text" class="form-control" value="2" disabled="disabled" id="value-quantity-coding2">
                </div>
                <div class="mb-3">
                    <label for="value-quantity-unit2" class="form-label">請輸入擺動期單位</label>
                    <input type="text" class="form-control" value="%" disabled="disabled" id="value-quantity-unit2">
                </div>
                `;
            } else if (observationMapping[key][index].name === '左腳步態分析' || observationMapping[key][index].name === '右腳步態分析') {
                valueQuantityMapping[observationMapping[key][index].value] = `
                <div class="mb-3">
                    <label for="value-quantity-value1" class="form-label">請輸入Gait normal值</label>
                    <input type="text" class="form-control" placeholder="${leftRightAnalysisMapping[observationMapping[key][index].name[0]][0]}" id="value-quantity-value1">
                </div>
                <div class="mb-3">
                    <label for="value-quantity-coding1" class="form-label">請輸入Gait normal代碼</label>
                    <input type="text" class="form-control" value="8117002" disabled="disabled" id="value-quantity-coding1">
                </div>
                <div class="mb-3">
                    <label for="value-quantity-unit1" class="form-label">請輸入Gait normal單位</label>
                    <input type="text" class="form-control" value="%" disabled="disabled" id="value-quantity-unit1">
                </div>

                <div class="mb-3">
                    <label for="value-quantity-value2" class="form-label">請輸入Medial rotation - action值</label>
                    <input type="text" class="form-control" placeholder="${leftRightAnalysisMapping[observationMapping[key][index].name[0]][1]}" id="value-quantity-value2">
                </div>
                <div class="mb-3">
                    <label for="value-quantity-coding2" class="form-label">請輸入Medial rotation - action代碼</label>
                    <input type="text" class="form-control" value="264739002" disabled="disabled" id="value-quantity-coding2">
                </div>
                <div class="mb-3">
                    <label for="value-quantity-unit2" class="form-label">請輸入Medial rotation - action單位</label>
                    <input type="text" class="form-control" value="%" disabled="disabled" id="value-quantity-unit2">
                </div>

                <div class="mb-3">
                    <label for="value-quantity-value3" class="form-label">請輸入Lateral rotation - action值</label>
                    <input type="text" class="form-control" placeholder="${leftRightAnalysisMapping[observationMapping[key][index].name[0]][2]}" id="value-quantity-value3">
                </div>
                <div class="mb-3">
                    <label for="value-quantity-coding3" class="form-label">請輸入Lateral rotation - action代碼</label>
                    <input type="text" class="form-control" value="264730003" disabled="disabled" id="value-quantity-coding3">
                </div>
                <div class="mb-3">
                    <label for="value-quantity-unit3" class="form-label">請輸入Lateral rotation - action單位</label>
                    <input type="text" class="form-control" value="%" disabled="disabled" id="value-quantity-unit3">
                </div>
                `;
            } else if (observationMapping[key][index].name === '跑步機') {
                let mapping = [
                    {
                        value: 30,
                        code: 'min',
                        coding: '55411-3',
                        display: 'Exercise duration',
                    },
                    {
                        value: 4,
                        code: 'km',
                        coding: '55412-1',
                        display: 'Exercise distance unspecified time',
                    },
                    {
                        value: 122.5,
                        code: 'kcal',
                        coding: '55421-2',
                        display: 'Calories burned Machine estimate',
                    },
                    {
                        value: 186,
                        code: '/min',
                        coding: '101692-2',
                        display: 'Maximum heart rate',
                    },
                    {
                        value: 155,
                        code: '/min',
                        coding: '103205-1',
                        display: 'Mean heart rate',
                    },
                    {
                        value: 2,
                        code: '%',
                        coding: '252140007',
                        display: 'Treadmill gradient achieved',
                    },
                    {
                        value: 8,
                        code: 'km/h',
                        coding: '252141006',
                        display: 'Treadmill speed achieved',
                    },
                ];
                tempContents = '';
                for (let index=1; index<=7; index++) {
                    tempContents += `
                    <div class="mb-3">
                        <label for="value-quantity-value${index}" class="form-label">請輸入${mapping[index-1].display}值</label>
                        <input type="text" class="form-control" placeholder="${mapping[index-1].value}" id="value-quantity-value${index}">
                    </div>
                    <div class="mb-3">
                        <label for="value-quantity-coding${index}" class="form-label">請輸入${mapping[index-1].display}代碼</label>
                        <input type="text" class="form-control" value="${mapping[index-1].coding}" disabled="disabled" id="value-quantity-coding${index}">
                    </div>
                    <div class="mb-3">
                        <label for="value-quantity-unit${index}" class="form-label">請輸入${mapping[index-1].display}單位</label>
                        <input type="text" class="form-control" value="${mapping[index-1].code}" disabled="disabled" id="value-quantity-unit${index}">
                    </div>
                    `;
                }

                valueQuantityMapping[observationMapping[key][index].value] = tempContents;

            } else if (observationMapping[key][index].name === '重量訓練') {
                valueQuantityMapping[observationMapping[key][index].value] = `
                <div class="mb-3">
                    <label for="value-quantity-value1" class="form-label">請輸入訓練重量值</label>
                    <input type="text" class="form-control" placeholder="50" id="value-quantity-value1">
                </div>
                <div class="mb-3">
                    <label for="value-quantity-coding1" class="form-label">請輸入訓練重量代碼</label>
                    <input type="text" class="form-control" value="training-wt" disabled="disabled" id="value-quantity-coding1">
                </div>
                <div class="mb-3">
                    <label for="value-quantity-unit1" class="form-label">請輸入訓練重量單位</label>
                    <input type="text" class="form-control" value="kg" disabled="disabled" id="value-quantity-unit1">
                </div>

                <div class="mb-3">
                    <label for="value-quantity-value2" class="form-label">請輸入訓練組數值</label>
                    <input type="text" class="form-control" placeholder="1" id="value-quantity-value2">
                </div>
                <div class="mb-3">
                    <label for="value-quantity-coding2" class="form-label">請輸入訓練組數代碼</label>
                    <input type="text" class="form-control" value="sets" disabled="disabled" id="value-quantity-coding2">
                </div>

                <div class="mb-3">
                    <label for="value-quantity-value3" class="form-label">請輸入Repetition count值</label>
                    <input type="text" class="form-control" placeholder="30" id="value-quantity-value3">
                </div>
                <div class="mb-3">
                    <label for="value-quantity-coding3" class="form-label">請輸入Repetition count代碼</label>
                    <input type="text" class="form-control" value="100298-9" disabled="disabled" id="value-quantity-coding3">
                </div>
                `;
            }
        }
    }

    return valueQuantityMapping;
}

function addBodySiteFields(observationBasicInfo) {
    let bodySitePayload = {};
    let bodySiteForm = [
        'gaitcycle-r', 'gaitcycle-l',
        'gaittype-l', 'gaittype-r',
    ];
    let selectedObservationOption = $('#observation-options :selected').val();
    let currentBasicInfo = observationBasicInfo[selectedObservationOption];

    if (bodySiteForm.includes(selectedObservationOption)) {
        bodySitePayload.body_site = {};
        bodySitePayload.body_site.coding = [
            {
                system: currentBasicInfo.bodySite.coding[0].system,
                code: currentBasicInfo.bodySite.coding[0].code,
                display: currentBasicInfo.bodySite.coding[0].display,
            },
        ];
    }

    return bodySitePayload;
}

function addValueCodeableConcept(observationBasicInfo) {
    let conceptForm = ['gaittype-l', 'gaittype-r', 'weighttraining'];
    let selectedObservationOption = $('#observation-options :selected').val();
    let currentBasicInfo = observationBasicInfo[selectedObservationOption];
    let conceptPayload = {};

    if (conceptForm.includes(selectedObservationOption)) {
        conceptPayload.value_codeable_concept = {
            coding: [{
                system: currentBasicInfo.valueCodeableConcept.coding[0].system,
                code: currentBasicInfo.valueCodeableConcept.coding[0].code,
                display: currentBasicInfo.valueCodeableConcept.coding[0].display,
            }],
        };
    }

    return conceptPayload;
}

function addHasMemberField() {
    let hasMemberForm = 'tbw';
    let selectedObservationOption = $('#observation-options :selected').val();
    let hasMemberPayload = {};
    let icw = $('#value-quantity-icw').val();
    let ecw = $('#value-quantity-ecw').val();

    if (icw === '') {
        icw = $('#value-quantity-icw').attr('placeholder');
    }
    if (ecw === '') {
        ecw = $('#value-quantity-ecw').attr('placeholder');
    }

    if (hasMemberForm === selectedObservationOption) {
        hasMemberPayload.has_member = [
            {
                reference: icw,
            },
            {
                reference: ecw,
            },
        ];
    }

    return hasMemberPayload;
}

function addValueQuantityFields(observationBasicInfo) {
    let valueQuantityPayload = {};
    let selectedObservationOption = $('#observation-options :selected').val();
    let currentBasicInfo = observationBasicInfo[selectedObservationOption];

    let componentForm = [
        'gaitcycle-r', 'gaitcycle-l', 'weighttraining',
        'gaittype-l', 'gaittype-r', 'treadmill', 'bloodpressure',
    ];
    let valueQuantitySystem = 'http://unitsofmeasure.org';
    let valueQu = {};

    if (componentForm.includes(selectedObservationOption)) {
        for (let index=0; index<currentBasicInfo.component.length; index++) {
            if (!valueQuantityPayload.component) {
                valueQuantityPayload.component = [];
            }

            let measuredValue = $(`#value-quantity-value${index+1}`).val();
            if (measuredValue === '') {
                measuredValue = $(`#value-quantity-value${index+1}`).attr('placeholder');
            }
            valueQu = {
                code: {
                    coding: [{
                        system: currentBasicInfo.component[index].code.coding[0].system,
                        code: currentBasicInfo.component[index].code.coding[0].code,
                        display: currentBasicInfo.component[index].code.coding[0].display,
                    }],
                },
                valueQuantity: {
                    value: Number(measuredValue),
                },
            };
            if (currentBasicInfo.component[index].valueQuantity.unit) {
                valueQu.valueQuantity.unit = currentBasicInfo.component[index].valueQuantity.unit;
                valueQu.valueQuantity.system = currentBasicInfo.component[index].valueQuantity.system;
                valueQu.valueQuantity.code = currentBasicInfo.component[index].valueQuantity.code;
            }
            valueQuantityPayload.component.push(valueQu);
        }
    } else {
        let measuredCoding = $('#value-quantity-coding1').val();
        let measuredUnit = $('#value-quantity-unit1').val();
        let measuredValue = $('#value-quantity-value1').val();
        if (measuredValue === '') {
            measuredValue = $('#value-quantity-value1').attr('placeholder');
        }
        valueQuantityPayload.value_quantity = {
            value: Number(measuredValue),
        };
        if (measuredCoding !== 'null') {
            valueQuantityPayload.value_quantity.unit = measuredUnit;
            valueQuantityPayload.value_quantity.system = valueQuantitySystem;
            valueQuantityPayload.value_quantity.code = measuredCoding;
        }
    }

    return valueQuantityPayload;
}
