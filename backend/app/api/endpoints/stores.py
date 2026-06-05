from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.schemas.user import StoreResponse
from app.models.store import Store

router = APIRouter(prefix="/stores", tags=["stores"])


@router.get("/", response_model=List[StoreResponse])
def list_stores(db: Session = Depends(get_db)):
    """List all supported stores"""
    stores = db.query(Store).all()
    return stores


@router.get("/{store_id}", response_model=StoreResponse)
def get_store(store_id: int, db: Session = Depends(get_db)):
    """Get details for a specific store"""
    store = db.query(Store).filter(Store.id == store_id).first()
    
    if not store:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Store not found"
        )
    
    return store


@router.post("/", response_model=StoreResponse, status_code=status.HTTP_201_CREATED)
def create_store(store_data: StoreResponse, db: Session = Depends(get_db)):
    """Create a new store (admin only)"""
    # Check if store already exists
    existing_store = db.query(Store).filter(
        (Store.code == store_data.code) | (Store.name == store_data.name)
    ).first()
    
    if existing_store:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Store with this code or name already exists"
        )
    
    new_store = Store(
        name=store_data.name,
        code=store_data.code,
        icon_url=store_data.icon_url,
        website=store_data.website
    )
    
    db.add(new_store)
    db.commit()
    db.refresh(new_store)
    
    return new_store
