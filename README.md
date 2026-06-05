# Loyalty Points Aggregator

A unified mobile application and backend service that aggregates loyalty points from multiple retailers into a single app with one barcode.

## 🎯 Overview

This project consolidates loyalty programs from major retailers (Starbucks, Target, McDonald's, Canadian Tire, gas stations, PC Points, and more) into one convenient Flutter mobile app. Users can:

- Link all their loyalty cards to one account
- Generate a unified QR/barcode for redemptions
- Track all points across multiple stores in real-time
- Sync points automatically across devices

## 📁 Project Structure

```
loyalty-points-aggregator/
├── flutter_app/              # Flutter mobile application
│   ├── lib/
│   ├── pubspec.yaml
│   └── ...
├── backend/                  # Python FastAPI server
│   ├── app/
│   ├── requirements.txt
│   ├── .env
│   └── ...
├── docs/                     # Documentation
├── .gitignore
├── LICENSE
└── README.md
```

## 🚀 Features (MVP)

### Authentication
- User registration and login
- JWT-based token authentication
- Secure password handling

### Loyalty Card Management
- Link multiple store loyalty accounts
- Store encrypted card credentials
- Manual card addition via card number/phone

### Points Tracking
- Real-time points balance display
- Historical points transaction logs
- Multi-store aggregated view

### Unified Barcode
- Generate QR code from aggregated account
- Store-specific barcode generation
- Barcode sharing capabilities

### Store Integrations
- **Starbucks** - API integration
- **Target** - Account linking
- **McDonald's** - Account linking
- **Canadian Tire** - Account linking
- **Gas Stations** - Generic integration
- **PC Points** - Account linking
- Extensible framework for additional stores

## 🛠️ Tech Stack

### Frontend
- **Flutter** - Cross-platform mobile (iOS/Android)
- **Provider** or **Riverpod** - State management
- **Dio** - HTTP client
- **QR Flutter** - QR code generation
- **Camera** - Barcode scanning

### Backend
- **Python 3.9+**
- **FastAPI** - Web framework
- **PostgreSQL** - Database
- **SQLAlchemy** - ORM
- **Pydantic** - Data validation
- **JWT** - Authentication
- **Redis** - Caching/sessions

## 📋 Prerequisites

### Backend
- Python 3.9+
- PostgreSQL 12+
- Redis (optional, for caching)

### Frontend
- Flutter SDK 3.0+
- Android Studio or Xcode
- iOS/Android emulators or devices

## 🔧 Installation & Setup

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env` file:
```
DATABASE_URL=postgresql://user:password@localhost/loyalty_db
SECRET_KEY=your-secret-key-here
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24
REDIS_URL=redis://localhost:6379
```

Run migrations and start server:
```bash
python -m alembic upgrade head
uvicorn app.main:app --reload
```

### Flutter Setup

```bash
cd flutter_app
flutter pub get
flutter run
```

## 📚 API Documentation

Once the backend is running, visit: `http://localhost:8000/docs`

### Key Endpoints

- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/login` - User login
- `GET /api/v1/cards` - List user's linked cards
- `POST /api/v1/cards` - Link new loyalty card
- `GET /api/v1/points` - Get aggregated points
- `POST /api/v1/barcode/generate` - Generate unified barcode
- `GET /api/v1/stores` - List supported stores

## 🔐 Security Considerations

- All passwords hashed with bcrypt
- Sensitive card data encrypted at rest
- JWT tokens with expiration
- HTTPS required in production
- Rate limiting on authentication endpoints
- Input validation on all endpoints

## 📈 Development Roadmap

### Phase 1 (MVP)
- [x] Project setup
- [ ] User authentication system
- [ ] Database schema
- [ ] Backend API structure
- [ ] Flutter UI framework
- [ ] 2-3 store integrations

### Phase 2
- [ ] Remaining store integrations
- [ ] Mobile app refinement
- [ ] Points history analytics
- [ ] Notifications for promotions

### Phase 3
- [ ] Web dashboard
- [ ] Advanced analytics
- [ ] Partner integrations
- [ ] Premium features

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Status**: Under Active Development 🚧
