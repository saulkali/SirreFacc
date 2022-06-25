from pydantic import BaseModel
from .employe_entity import EmployeEntity
from datetime import date, datetime
class SaleEntity(BaseModel):
    id:str = ""
    employe:EmployeEntity = None
    listArticle:list
    dateTime:str = datetime.now().__str__()
    isCredit:bool = False
