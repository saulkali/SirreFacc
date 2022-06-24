from pydantic import BaseModel,validator
from datetime import datetime

class EmployeEntity(BaseModel):
    id:str = ""
    photoUrl:str = ""
    firstName:str = ""
    lastName:str = ""
    password:str = ""
    phone:str = ""
    address:str = ""
    cp:int = 0
    email:str = ""
    rfc:str = ""
    dateTime:str = datetime.now().__str__()
    permissions:int = 0
    listPay:str = ""

    @validator("firstName")
    def firstNameValidate(cls,text):
        if text.__len__() > 0:
            return text
        raise ValueError("el nombre del empleado no puede estar vacio...")
    
    @validator("lastName")
    def lastNameValidate(cls,text):
        if text.__len__() > 0:
            return text
        raise ValueError("el apellido del empleado no puede estar vacio...")
    
    @validator("email")
    def emailValidate(cls,text):
        if "@" not in text:
            raise ValueError("La direccion del correo no es valida...")
        if text.__len__() <= 0:
            raise ValueError("el correo del empleado no puede estar vacio...")
    
        return text
    
    @validator("rfc")
    def rfcValidate(cls,text):
        if text.__len__()>0:
            return text
        raise ValueError("el rfc del empleado no puede ir vacio...")
    
    @validator("password")
    def passwordValidate(cls,text):
        if text.__len__() > 2:
            return text
        raise ValueError("la contraseña no puede ser menor de 3 caracteres...")