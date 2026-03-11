# Architecture

## Overview
Simple request-processing service with modular design.

## Module Structure
```
src/
├── app.py — Core request handlers
├── auth.py — Authentication and token management
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
The `src/auth.py` module provides token-based authentication using HMAC-SHA256 signatures:

- `create_token(user_id, secret)`: Creates a signed authentication token with timestamp
- `verify_token(token, secret)`: Verifies token signature and expiration, returns dict with `user_id` and `is_valid`
- `require_auth`: Decorator that enforces authentication on handlers, returns 401 error if invalid

Tokens expire after 3600 seconds (1 hour).

## Dependencies
- Python 3.11+
- No external dependencies (stdlib only)