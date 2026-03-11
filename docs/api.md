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

### `protected_process(data: str, token: str = "", secret: str = "") -> dict`
Processes data with authentication required.

**Parameters:**
- `data` (str): Input string to process.
- `token` (str): Authentication token.
- `secret` (str): Signing secret key for token verification.

**Returns:**
- Processed result if authenticated, otherwise `{"error": "Unauthorized", "status": 401}`.

## Authentication

### `create_token(user_id: str, secret: str) -> str`
Creates a signed authentication token.

**Parameters:**
- `user_id` (str): User identifier.
- `secret` (str): Signing secret key.

**Returns:**
- Hex-encoded HMAC token string.

### `verify_token(token: str, secret: str) -> dict`
Verifies and decodes an authentication token.

**Parameters:**
- `token` (str): The token string to verify.
- `secret` (str): Signing secret key.

**Returns:**
- `{"user_id": <str>, "is_valid": <bool>}`

### `require_auth(func)`
Decorator that enforces authentication on a handler.

Wraps functions to require valid authentication tokens. Expects `token` and `secret` keyword arguments when calling the wrapped function.

**Returns:**
- Original function result if authenticated, otherwise `{"error": "Unauthorized", "status": 401}`.