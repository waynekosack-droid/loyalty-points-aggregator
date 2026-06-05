# Flutter App - Loyalty Points Aggregator

Flutter mobile application for the loyalty points aggregator.

## Project Structure

```
flutter_app/
├── lib/
│   ├── main.dart               # App entry point
│   ├── config/
│   │   ├── theme.dart
│   │   ├── constants.dart
│   │   └── api_config.dart
│   ├── models/                 # Data models
│   │   ├── user.dart
│   │   ├── loyalty_card.dart
│   │   ├── points.dart
│   │   └── store.dart
│   ├── providers/              # State management
│   │   ├── auth_provider.dart
│   │   ├── card_provider.dart
│   │   ├── points_provider.dart
│   │   └── store_provider.dart
│   ├── services/               # API and local services
│   │   ├── api_service.dart
│   │   ├── auth_service.dart
│   │   ├── card_service.dart
│   │   ├── barcode_service.dart
│   │   └── storage_service.dart
│   ├── screens/
│   │   ├── auth/
│   │   │   ├── login_screen.dart
│   │   │   ├── register_screen.dart
│   │   │   └── forgot_password_screen.dart
│   │   ├── home/
│   │   │   ├── home_screen.dart
│   │   │   └── points_overview_screen.dart
│   │   ├── cards/
│   │   │   ├── cards_list_screen.dart
│   │   │   ├── add_card_screen.dart
│   │   │   └── card_detail_screen.dart
│   │   ├── barcode/
│   │   │   ├── barcode_screen.dart
│   │   │   └── scan_barcode_screen.dart
│   │   └── settings/
│   │       └── settings_screen.dart
│   ├── widgets/                # Reusable widgets
│   │   ├── common/
│   │   │   ├── custom_app_bar.dart
│   │   │   ├── custom_button.dart
│   │   │   └── loading_spinner.dart
│   │   ├── cards/
│   │   │   ├── loyalty_card_widget.dart
│   │   │   └── points_display_widget.dart
│   │   └── barcode/
│   │       ├── qr_code_widget.dart
│   │       └── barcode_widget.dart
│   ├── utils/
│   │   ├── validators.dart
│   │   ├── formatters.dart
│   │   ├── exceptions.dart
│   │   └── logger.dart
│   └── routes/
│       └── app_routes.dart
├── pubspec.yaml
├── pubspec.lock
├── .gitignore
└── README.md
```

## Dependencies

Key packages in `pubspec.yaml`:
- `provider` - State management
- `dio` - HTTP client
- `get_it` - Service locator
- `flutter_secure_storage` - Secure local storage
- `qr_flutter` - QR code generation
- `mobile_scanner` - Barcode scanning
- `intl` - Internationalization
- `crypto` - Encryption utilities

## Installation

```bash
flutter pub get
```

## Running the App

```bash
flutter run
```

## Building for Release

```bash
flutter build apk        # Android
flutter build ios        # iOS
```
