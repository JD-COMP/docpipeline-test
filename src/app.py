"""Core application module."""


def health():
    """Return health status."""
    return {"status": "ok"}


def process(data: str) -> dict:
    """Process input data.

    Args:
        data: Input string to process.

    Returns:
        Dict with uppercase result and length.
    """
    return {"result": data.upper(), "length": len(data)}
