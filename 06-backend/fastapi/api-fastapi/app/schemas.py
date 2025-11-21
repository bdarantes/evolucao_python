from pydantic import BaseModel

class ItemBase(BaseModel):
    nome: str
    descricao: str | None = None

class ItemCreate(ItemBase):
    pass 

class ItemResponse(ItemBase):
    id: int

    class Config:
        orm_mode = True