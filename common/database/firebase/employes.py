from common.firebase.firebase import FireBase

from common.entities.employe_entity import EmployeEntity
from common.firebase import constants as firebaseConstants


firebase = FireBase()

def saveEmploye(employeEntity:EmployeEntity):
    '''create new employe firebase'''
    key = firebase.db.child(firebaseConstants.referenceEmploye).push().key
    employeEntity.id = key
    firebase.db.child(firebaseConstants.referenceEmploye).child(key).set(employeEntity.dict())

def updateEmploye(employeEntity:EmployeEntity):
    firebase.db.child(firebaseConstants.referenceEmploye).child(employeEntity.id).update(employeEntity.dict())

def deleteEmploye(employeEntity:EmployeEntity):
    firebase.db.child(firebaseConstants.referenceEmploye).child(employeEntity.id).delete()

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

def loginEmploye(email:str,password:str)->bool:
    employeJson = firebase.db.child(firebaseConstants.referenceEmploye).order_by_child("email").equal_to(email).limit_to_first(1).get().popitem()
    if employeJson is not None:
        key,value = employeJson
        employeEntity = EmployeEntity.parse_obj(value)
        if employeEntity.password.__eq__(password):
            return True
        return False
    return False