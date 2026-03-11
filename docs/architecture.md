# Architecture

## Overview
Simple request-processing service with modular design.

## Module Structure
```
src/
├── app.py — Core request handlers
├── auth.py — Authentication and authorization
├── config.py — Application configuration
└── cli.py — Command-line interface
```

## Configuration
The `src/config.py` module provides:
- `APP_NAME`: Application name (default: "docpipeline-test")
- `APP_VERSION`: Application version (default: "2.0.0")
- `DEBUG`: Debug mode flag (default: False)
- `MAX_BATCH_SIZE`: Maximum items per batch (default: 500)
- `TOKEN_EXPIRY`: Token expiration time in seconds (default: 3600)
- `LOG_LEVEL`: Logging level (default: "INFO")
- `ALLOWED_ORIGINS`: CORS allowed origins (default: ["*"])

## Authentication
The `src/auth.py` module provides token-based authentication:
- `create_token(user_id, secret)`: Creates a signed HMAC token with timestamp
- `verify_token(token, secret)`: Verifies token signature and expiration, returns dict with `user_id` and `is_valid`
- `require_auth`: Decorator to enforce authentication on handlers

## Dependencies
- Python 3.11+
- No external dependencies (stdlib only)