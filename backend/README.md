# Backend - Loyalty Points Aggregator

Python FastAPI backend service for the loyalty points aggregator application.

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app initialization
│   ├── config.py               # Configuration settings
│   ├── dependencies.py         # Dependency injection
│   ├── models/                 # SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── card.py
│   │   ├── points.py
│   │   └── store.py
│   ├── schemas/                # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── card.py
│   │   ├── points.py
│   │   └── store.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── endpoints/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py         # Authentication endpoints
│   │   │   ├── cards.py        # Card management endpoints
│   │   │   ├── points.py       # Points endpoints
│   │   │   ├── barcode.py      # Barcode generation
│   │   │   └── stores.py       # Store management
│   │   └── v1.py               # API v1 router
│   ├── services/               # Business logic
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── card_service.py
│   │   ├── points_service.py
│   │   ├── barcode_service.py
│   │   └── store_integrations/
│   │       ├── __init__.py
│   │       ├── base.py         # Base store integration
│   │       ├── starbucks.py
│   │       ├── target.py
│   │       ├── mcdonalds.py
│   │       ├── canadian_tire.py
│   │       ├── pc_points.py
│   │       └── gas_stations.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py             # SQLAlchemy base
│   │   ├── session.py          # Database session
│   │   └── migrations/         # Alembic migrations
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── security.py         # Security utilities
│   │   ├── encryption.py       # Data encryption
│   │   └── validators.py       # Input validators
│   └── middleware/
│       ├── __init__.py
│       └── auth.py             # Authentication middleware
├── requirements.txt
├── .env.example
├── alembic.ini
├── main.py                     # Entry point
└── README.md
```

## Environment Variables

See `.env.example` for all required variables.

## Installation

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Visit `http://localhost:8000/docs` for interactive API documentation.
