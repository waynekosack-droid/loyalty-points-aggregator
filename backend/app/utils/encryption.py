from cryptography.fernet import Fernet
from app.config import settings
import base64
import hashlib


def generate_encryption_key() -> str:
    """Generate a new encryption key"""
    return Fernet.generate_key().decode()


def _get_cipher():
    """Get cipher instance from config"""
    key = settings.ENCRYPTION_KEY.encode()
    if len(key) < 32:
        key = base64.urlsafe_b64encode(hashlib.sha256(key).digest())
    return Fernet(key)


def encrypt_data(data: str) -> str:
    """Encrypt sensitive data"""
    try:
        cipher = _get_cipher()
        encrypted = cipher.encrypt(data.encode())
        return encrypted.decode()
    except Exception as e:
        raise ValueError(f"Encryption failed: {str(e)}")


def decrypt_data(encrypted_data: str) -> str:
    """Decrypt sensitive data"""
    try:
        cipher = _get_cipher()
        decrypted = cipher.decrypt(encrypted_data.encode())
        return decrypted.decode()
    except Exception as e:
        raise ValueError(f"Decryption failed: {str(e)}")
