from pydantic import BaseModel
from .employe_entity import EmployeEntity
from datetime import datetime
class SaleEntity(BaseModel):
    id:str = ""
    employe:EmployeEntity = None
    listArticle:list
    dateTime:str = datetime.now().__str__()
    isCredit:bool = False
    payClient:float
    changeClient:float

    def getTotal(self) -> float:
        total = 0
        for article in self.listArticle:
            total += article.amountArticle * article.priceUniArticle
        return total
