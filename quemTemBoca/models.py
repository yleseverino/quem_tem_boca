from pydantic import BaseModel, validator, Field, condecimal, HttpUrl
from datetime import datetime

class Restaurante(BaseModel):
    id: int = Field(...)
    nome: str = Field(...)
    descricao: str = Field(...)
    criado_em: datetime = datetime.now()

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

    