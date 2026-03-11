"""Tests for auth module."""

from src.auth import create_token, verify_token


def test_create_and_verify():
    token = create_token("user1", "secret123")
    result = verify_token(token, "secret123")
    assert result["is_valid"] is True
    assert result["user_id"] == "user1"


def test_invalid_secret():
    token = create_token("user1", "secret123")
    result = verify_token(token, "wrong-secret")
    assert result["is_valid"] is False
