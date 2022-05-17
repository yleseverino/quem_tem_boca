from pydantic import BaseModel, ValidationError, validator
from datetime import datetime


class Restaurante(BaseModel):
    nome: str
    descricao: str
    pontuacao: float

    @validator('pontuacao')
    def pontuacao_between_0_and_5(cls, v):
        if v > 5:
            raise ValueError('A pontuação de um restaurante não pode ser maior que 5') 
        elif v < 0:
            raise ValueError('A pontuação de um restaurante não pode ser menor que 0') 
        return v

    criado_em: datetime = datetime.now()