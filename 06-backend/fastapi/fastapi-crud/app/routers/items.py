from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/items", tags=["Items"])

@router.post("/", response_model=schemas.ItemResponse)
def create_item(data: schemas.ItemCreate, db: Session= Depends(get_db)):
    novo = models.Item(**data.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/", response_model=list[schemas.ItemResponse])
def list_items(db:Session = Depends(get_db)):
    return db.query(models.Item).all()

@router.get("/{item_id}", response_model=schemas.ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter_by(id=item_id).first()
    if not item:
        raise HTTPException(404, "Item não encontrado")
    return item

@router.put("/{item_id}", response_model=schemas.ItemResponse)
def update_item(item_id: int, data: schemas.ItemCreate, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter_by(id=item_id).first()
    if not item:
        raise HTTPException(404, "Item não encontrado")
    
    item.nome = data.nome
    item.descricao = data.descricao
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter_by(id=item_id).first()
    if not item:
        raise HTTPException(404, "Item não encontrado")
    
    db.delete(item)
    db.commit()
    return {"message": "Item deletado"}