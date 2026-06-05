from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/loyalty_db"
    
    # JWT
    SECRET_KEY: str = "your-super-secret-key-change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # API
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Loyalty Points Aggregator"
    DEBUG: bool = True
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:8100", "http://localhost:3000"]
    
    # Store API Keys
    STARBUCKS_API_KEY: str = ""
    TARGET_API_KEY: str = ""
    MCDONALDS_API_KEY: str = ""
    CANADIAN_TIRE_API_KEY: str = ""
    PC_POINTS_API_KEY: str = ""
    
    # Encryption
    ENCRYPTION_KEY: str = "your-encryption-key-for-sensitive-data"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
