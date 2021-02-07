from datetime import datetime

def icu_f3(raw):
    patient = []
    for k in raw:
        if k[0] == 'p':
            patient.append(raw[k])
        else:
            doct.append(raw[k])
    
    return {
        "patient_list": patient,
        "caregiver_list": doct,
        "date": datetime.utcnow().isoformat()
    }