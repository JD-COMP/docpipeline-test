"""Tests for app module."""

from src.app import health, process


def test_health():
    assert health() == {"status": "ok"}


def test_process():
    result = process("hello")
    assert result == {"result": "HELLO", "length": 5}
