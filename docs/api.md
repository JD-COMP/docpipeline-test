# API Reference

## Functions

### `health(verbose: bool = False) -> dict`
Returns service health status.

**Parameters:**
- `verbose` (bool): If True, include version and uptime info. Defaults to False.

**Returns:**
- `{"status": "ok"}` or `{"status": "ok", "version": "2.0.0", "uptime_seconds": <int>}` when verbose is True

### `process(data: str, normalize: bool = True) -> dict`
Processes input data by converting to uppercase.

**Parameters:**
- `data` (str): Input string to process.
- `normalize` (bool): If True, strip whitespace before processing. Defaults to True.

**Returns:**
- `{"result": "<uppercase>", "length": <int>, "normalized": <bool>}`

### `validate(data: str, strict: bool = False) -> dict`
Validates input data against schema rules.

**Parameters:**
- `data` (str): Input string to validate.
- `strict` (bool): If True, enforce minimum length of 5 characters. Defaults to False.

**Returns:**
- `{"is_valid": <bool>, "errors": [<str>]}`

### `batch_process(items: list[str], normalize: bool = True) -> list[dict]`
Processes multiple items in batch.

**Parameters:**
- `items` (list[str]): List of strings to process.
- `normalize` (bool): Apply normalization to each item. Defaults to True.

**Returns:**
- List of processed result dictionaries (same format as `process` return value)

### `protected_process(data: str) -> dict`
Processes data with authentication required. Uses the `@require_auth` decorator to enforce authentication.

**Parameters:**
- `data` (str): Input string to process.

**Returns:**
- Processed result if authenticated, otherwise `{"error": "Unauthorized", "status": 401}`.

## Authentication

### `AuthMiddleware(secret_key: str)`
Middleware for handling JWT authentication. Initialize with a secret key to enable token verification across the application.

**Parameters:**
- `secret_key` (str): Signing secret key for JWT tokens.

### `create_api_key(user_id: str) -> str`
Creates a new API key for the specified user.

**Parameters:**
- `user_id` (str): User identifier.

**Returns:**
- API key string.

### `require_auth(func)`
Decorator that enforces authentication on a handler. Wraps functions to require valid JWT authentication tokens managed by `AuthMiddleware`.

**Returns:**
- Original function result if authenticated, otherwise `{"error": "Unauthorized", "status": 401}`.

### `login(username: str, password: str) -> dict`
Authenticates user and returns JWT token.

**Endpoint:** `POST /api/auth/login`

**Parameters:**
- `username` (str): User's username.
- `password` (str): User's password.

**Returns:**
- `{"token": "placeholder"}`

### `refresh_token(token: str) -> dict`
Refreshes an expiring JWT token.

**Endpoint:** `POST /api/auth/refresh`

**Parameters:**
- `token` (str): The current JWT token to refresh.

**Returns:**
- `{"token": "refreshed_placeholder"}`

### `get_current_user(token: str) -> dict`
Gets current authenticated user profile.

**Endpoint:** `GET /api/auth/me`

**Parameters:**
- `token` (str): Valid JWT token.

**Returns:**
- `{"user": "placeholder"}`