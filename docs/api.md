# API Reference

## Functions

### `health(verbose: bool = False) -> dict`
Returns service health status.

**Parameters:**
- `verbose` (bool): If True, include version and uptime info.

**Returns:**
- `{"status": "ok"}` (default)
- `{"status": "ok", "version": "2.0.0", "uptime_seconds": <int>}` (when verbose is True)

### `process(data: str, normalize: bool = True) -> dict`
Processes input data by converting to uppercase.

**Parameters:**
- `data` (str): Input string to process.
- `normalize` (bool): If True, strip whitespace before processing.

**Returns:** `{"result": "<uppercase>", "length": <int>, "normalized": <bool>}`

### `validate(data: str, strict: bool = False) -> dict`
Validates input data against schema rules.

**Parameters:**
- `data` (str): Input string to validate.
- `strict` (bool): If True, enforce minimum length of 5 characters.

**Returns:** `{"is_valid": <bool>, "errors": [<str>]}`

### `batch_process(items: list[str], normalize: bool = True) -> list[dict]`
Processes multiple items in batch.

**Parameters:**
- `items` (list[str]): List of strings to process.
- `normalize` (bool): Apply normalization to each item.

**Returns:** List of processed results, each containing `{"result": "<uppercase>", "length": <int>, "normalized": <bool>}`.

### `protected_process(data: str) -> dict`
Processes data with authentication required.

**Parameters:**
- `data` (str): Input string to process.

**Returns:** Processed result (requires valid auth token).

**Authentication:** Requires valid token via `require_auth` decorator.

## Authentication

### `create_token(user_id: str, secret: str) -> str`
Creates a signed authentication token.

**Parameters:**
- `user_id` (str): User identifier.
- `secret` (str): Signing secret key.

**Returns:** Hex-encoded HMAC token string.

### `verify_token(token: str, secret: str) -> dict`
Verifies and decodes an authentication token.

**Parameters:**
- `token` (str): The token string to verify.
- `secret` (str): Signing secret key.

**Returns:** `{"user_id": <str>, "is_valid": <bool>}`