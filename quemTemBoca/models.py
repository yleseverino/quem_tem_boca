from pydantic import BaseModel, validator, Field, condecimal, HttpUrl
from datetime import datetime
from typing import List
from werkzeug.security import check_password_hash, generate_password_hash


class User(BaseModel):
    id: int
    nome: str
    email: str
    hash_password: str

    def check_password_hash_user(self, input_password):
        return check_password_hash(self.hash_password, input_password)


class Prato(BaseModel):
    id: int = Field(...)
    nome: str = Field(...)
    descricao: str = Field(...)
    preco: condecimal( decimal_places=2, gt=0)
    criado_em: datetime = datetime.now()
    img_url : HttpUrl

    @validator('nome')
    def nome_menor_que_255(cls, v):
        if len(v) > 255:
            raise ValueError('O numero de caracteres no nome não pode ser maior que 255') 
        return v
    
    @validator('descricao')
    def descricao_menor_que_1000(cls, v):
        if len(v) > 1000:
            raise ValueError('O numero de caracteres da desc não pode ser maior que 1000') 
        return v

class Restaurante(BaseModel):
    id: int = Field(...)
    nome: str = Field(...)
    telefone: str = Field(...)
    descricao: str = Field(...)
    criado_em: datetime = datetime.now()

    pratos: List[Prato] = None

    logo_url : HttpUrl
    background_url : HttpUrl

    "A pontuação deve ser maior que 0, ter 2 casas decimais e ser menor que 5"
    pontuacao: condecimal(decimal_places=2, ge=0, le=5)

    "O preco de entrega deve ser menor or igual 100 reais e maior que 0 reais"
    preco_entrega: condecimal( decimal_places=2, ge=0, le=100)
    
    @validator('nome')
    def nome_menor_que_255(cls, v):
        if len(v) > 255:
            raise ValueError('O numero de caracteres no nome não pode ser maior que 255') 
        return v
    
    @validator('descricao')
    def descricao_menor_que_1000(cls, v):
        if len(v) > 1000:
            raise ValueError('O numero de caracteres no nome não pode ser maior que 255') 
        return v



    