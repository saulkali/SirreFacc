from common.firebase.firebase import FireBase

from common.entities.employe_entity import EmployeEntity
from common.firebase import constants as firebaseConstants


firebase = FireBase()

def saveEmploye(employeEntity:EmployeEntity):
    '''create new employe firebase'''
    key = firebase.db.child(firebaseConstants.referenceEmploye).push().key
    employeEntity.id = key
    firebase.db.child(firebaseConstants.referenceEmploye).child(key).set(employeEntity.dict())

def getAllEmployes() -> list:
    '''get all employes firebase'''
    listEmployes = []
    employesJson = firebase.db.child(firebaseConstants.referenceEmploye).get()
    if employesJson != None:
        for key,value in employesJson.items():
            employeEntity = EmployeEntity.parse_obj(value)
            employeEntity.id = key
            listEmployes.append(employeEntity)
    return listEmployes
