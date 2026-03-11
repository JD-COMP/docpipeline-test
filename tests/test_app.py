"""Tests for app module."""

from src.app import health, process, validate, batch_process


def test_health():
    assert health() == {"status": "ok"}


def test_health_verbose():
    result = health(verbose=True)
    assert result["version"] == "2.0.0"


def test_process():
    result = process("hello")
    assert result == {"result": "HELLO", "length": 5, "normalized": True}


def test_process_no_normalize():
    result = process("  hello  ", normalize=False)
    assert result["length"] == 9


def test_validate():
    assert validate("hello")["is_valid"] is True
    assert validate("")["is_valid"] is False


def test_validate_strict():
    assert validate("hi", strict=True)["is_valid"] is False
    assert validate("hello", strict=True)["is_valid"] is True


def test_batch():
    results = batch_process(["a", "b"])
    assert len(results) == 2
