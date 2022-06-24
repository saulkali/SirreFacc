from pydantic import BaseModel, validator
from datetime import datetime

class ArticleEntity(BaseModel):
    id:str
    photoUrl:str = ""
    name:str
    description:str = ""
    price:float = 0.0
    amount:float = 0.0
    dateTime:str = datetime.now().__str__()
    offSale:float = 0.0
    shelf:str = ""
    methodShopping:str = ""
    category:str = ""
    vertical:str = ""
    horizontal:str = ""

    @validator("id")
    def idValidate(cls,text):
        if "$" in text:
            raise ValueError("los codigo no pueden tener el caracter --> $ <--")
        if text.__len__() > 0:
            return text
        raise ValueError("El id del articulo no puede estar vacio...")
     
    @validator("name")
    def nameValidate(cls,text):
        if text.__len__() > 0:
            return text
        raise ValueError("El nombre del articulo no puede estar vacio...")
    
    #@validator("methodShopping")
    #def methodShopingValidate(cls,text):
    #    if text.__len__() > 0:
    #        return text
    #    raise ValueError("el modo de venta no puede estar vacio...")
    