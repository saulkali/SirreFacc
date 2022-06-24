from pydantic import BaseModel

class ShoppingCardEntity(BaseModel):
    idArticle:str
    photoUrlArticle:str
    nameArticle:str
    amountArticle:float
    priceUniArticle:float
