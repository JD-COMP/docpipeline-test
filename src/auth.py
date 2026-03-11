"""Authentication and authorization module."""

import hashlib
import hmac
import time

# Token expiry in seconds
TOKEN_EXPIRY = 3600


def create_token(user_id: str, secret: str) -> str:
    """Create a signed authentication token.

    Args:
        user_id: User identifier.
        secret: Signing secret key.

    Returns:
        Hex-encoded HMAC token.
    """
    timestamp = str(int(time.time()))
    payload = f"{user_id}:{timestamp}"
    signature = hmac.new(secret.encode(), payload.encode(), hashlib.sha256).hexdigest()
    return f"{payload}:{signature}"


def verify_token(token: str, secret: str) -> dict:
    """Verify and decode an authentication token.

    Args:
        token: The token string to verify.
        secret: Signing secret key.

    Returns:
        Dict with user_id and is_valid flag.
    """
    try:
        user_id, timestamp, signature = token.rsplit(":", 2)
        expected = hmac.new(
            secret.encode(), f"{user_id}:{timestamp}".encode(), hashlib.sha256
        ).hexdigest()
        is_valid = hmac.compare_digest(signature, expected)
        is_expired = (time.time() - int(timestamp)) > TOKEN_EXPIRY
        return {"user_id": user_id, "is_valid": is_valid and not is_expired}
    except (ValueError, TypeError):
        return {"user_id": "", "is_valid": False}


def require_auth(func):
    """Decorator that enforces authentication on a handler."""
    def wrapper(*args, token: str = "", secret: str = "", **kwargs):
        result = verify_token(token, secret)
        if not result["is_valid"]:
            return {"error": "Unauthorized", "status": 401}
        return func(*args, **kwargs)
    return wrapper
