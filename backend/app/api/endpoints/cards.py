from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.schemas.user import CardAdd, CardResponse
from app.models.card import LoyaltyCard
from app.models.store import Store
from app.utils.encryption import encrypt_data, decrypt_data

router = APIRouter(prefix="/cards", tags=["cards"])


@router.get("/", response_model=List[CardResponse])
def list_cards(user_id: int, db: Session = Depends(get_db)):
    """List all loyalty cards for a user"""
    cards = db.query(LoyaltyCard).filter(LoyaltyCard.user_id == user_id).all()
    return cards


@router.post("/", response_model=CardResponse, status_code=status.HTTP_201_CREATED)
def add_card(user_id: int, card_data: CardAdd, db: Session = Depends(get_db)):
    """Add a new loyalty card"""
    # Verify store exists
    store = db.query(Store).filter(Store.id == card_data.store_id).first()
    if not store:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Store not found"
        )
    
    # Check if user already has this store's card
    existing_card = db.query(LoyaltyCard).filter(
        LoyaltyCard.user_id == user_id,
        LoyaltyCard.store_id == card_data.store_id
    ).first()
    
    if existing_card:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You already have a card for this store"
        )
    
    # Encrypt sensitive data
    encrypted_card_number = encrypt_data(card_data.card_number)
    encrypted_phone = encrypt_data(card_data.phone_number) if card_data.phone_number else None
    encrypted_email = encrypt_data(card_data.email) if card_data.email else None
    
    # Create new card
    new_card = LoyaltyCard(
        user_id=user_id,
        store_id=card_data.store_id,
        card_number=encrypted_card_number,
        phone_number=encrypted_phone,
        email=encrypted_email,
        nickname=card_data.nickname
    )
    
    db.add(new_card)
    db.commit()
    db.refresh(new_card)
    
    return new_card


@router.get("/{card_id}", response_model=CardResponse)
def get_card(card_id: int, db: Session = Depends(get_db)):
    """Get a specific loyalty card"""
    card = db.query(LoyaltyCard).filter(LoyaltyCard.id == card_id).first()
    
    if not card:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Card not found"
        )
    
    return card


@router.put("/{card_id}", response_model=CardResponse)
def update_card(card_id: int, card_data: CardAdd, db: Session = Depends(get_db)):
    """Update a loyalty card"""
    card = db.query(LoyaltyCard).filter(LoyaltyCard.id == card_id).first()
    
    if not card:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Card not found"
        )
    
    # Update encrypted data
    card.card_number = encrypt_data(card_data.card_number)
    card.phone_number = encrypt_data(card_data.phone_number) if card_data.phone_number else None
    card.email = encrypt_data(card_data.email) if card_data.email else None
    card.nickname = card_data.nickname
    
    db.commit()
    db.refresh(card)
    
    return card


@router.delete("/{card_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_card(card_id: int, db: Session = Depends(get_db)):
    """Delete a loyalty card"""
    card = db.query(LoyaltyCard).filter(LoyaltyCard.id == card_id).first()
    
    if not card:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Card not found"
        )
    
    db.delete(card)
    db.commit()
    
    return None
