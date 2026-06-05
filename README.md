
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
