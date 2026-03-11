"""Core application module."""

from src.auth import require_auth


def health(verbose: bool = False) -> dict:
    """Return health status.

    Args:
        verbose: If True, include version and uptime info.

    Returns:
        Health status dict.
    """
    result = {"status": "ok"}
    if verbose:
        result["version"] = "2.0.0"
        result["uptime_seconds"] = 0  # placeholder
    return result


def process(data: str, normalize: bool = True) -> dict:
    """Process input data.

    Args:
        data: Input string to process.
        normalize: If True, strip whitespace before processing.

    Returns:
        Dict with processed result, length, and normalized flag.
    """
    if normalize:
        data = data.strip()
    return {"result": data.upper(), "length": len(data), "normalized": normalize}


def validate(data: str, strict: bool = False) -> dict:
    """Validate input data against schema rules.

    Args:
        data: Input string to validate.
        strict: If True, enforce minimum length.

    Returns:
        Validation result with is_valid and errors.
    """
    errors = []
    if not data:
        errors.append("Data must not be empty")
    if strict and len(data) < 5:
        errors.append("Data must be at least 5 characters in strict mode")
    return {"is_valid": len(errors) == 0, "errors": errors}


def batch_process(items: list[str], normalize: bool = True) -> list[dict]:
    """Process multiple items in batch.

    Args:
        items: List of strings to process.
        normalize: Apply normalization to each item.

    Returns:
        List of processed results.
    """
    return [process(item, normalize=normalize) for item in items]


@require_auth
def protected_process(data: str) -> dict:
    """Process data with authentication required.

    Args:
        data: Input string to process.

    Returns:
        Processed result (requires valid auth token).
    """
    return process(data)
