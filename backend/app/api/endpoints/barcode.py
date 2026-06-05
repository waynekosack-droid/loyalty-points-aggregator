from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Dict
from app.db.session import get_db
from app.models.card import LoyaltyCard
from app.models.user import User
from app.utils.encryption import decrypt_data
import qrcode
import io
import base64

router = APIRouter(prefix="/barcode", tags=["barcode"])


@router.post("/generate/{user_id}")
def generate_barcode(user_id: int, db: Session = Depends(get_db)):
    """Generate a unified QR barcode for the user"""
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Create QR code data with user ID and email
    qr_data = f"LOYALTY:{user_id}:{user.email}"
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert to base64
    img_buffer = io.BytesIO()
    img.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.getvalue()).decode()
    
    return {
        "user_id": user_id,
        "qr_code": img_base64,
        "format": "base64",
        "data": qr_data
    }


@router.post("/generate/store/{card_id}")
def generate_store_barcode(card_id: int, db: Session = Depends(get_db)):
    """Generate a store-specific barcode"""
    card = db.query(LoyaltyCard).filter(LoyaltyCard.id == card_id).first()
    
    if not card:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Card not found"
        )
    
    # Decrypt card number
    try:
        card_number = decrypt_data(card.card_number)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to decrypt card data"
        )
    
    # Create QR code data with store and card info
    qr_data = f"STORE:{card.store_id}:{card_number}"
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert to base64
    img_buffer = io.BytesIO()
    img.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.getvalue()).decode()
    
    return {
        "card_id": card_id,
        "store_id": card.store_id,
        "qr_code": img_base64,
        "format": "base64"
    }
