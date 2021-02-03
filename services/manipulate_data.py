from datetime import datetime
def icu_f3(raw, doct_shift):
    patient = []
    doct = []
    for k in raw:
        if k[0] == 'p':
            patient.append(raw[k])
        else:
            doct.append(raw[k])
    
    return {
        "doct_shift": doct_shift,
        "patient_list": patient,
        "caregiver_list": doct,
        "date": datetime.utcnow().isoformat()
        }