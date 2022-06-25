from common.firebase.firebase import FireBase
from common.firebase import constants as firebaseConstans
from common.entities.sale_entity import SaleEntity

firebase = FireBase()

def saveSale(saleEntity:SaleEntity)->bool:
    try:
        key = firebase.db.child(firebaseConstans.referenceSale).push().key
        saleEntity.id = key
        firebase.db.child(firebaseConstans.referenceSale).child(key).set(saleEntity.dict())
        return True
    except Exception as error:
        print(error)
        return False