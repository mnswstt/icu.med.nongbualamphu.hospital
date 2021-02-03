import pymongo

client = pymongo.MongoClient("192.168.1.4", 27020)
db = client.icu_room
icu_floor3 = db['icu-floor-3']
#patient_list = db.patient_list
#doct_on_shift = db.doct_on_shift