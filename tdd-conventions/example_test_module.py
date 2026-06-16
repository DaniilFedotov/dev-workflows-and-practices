"""
Пример tests/billing/test_greeting.py — не копировать слепо.
"""

from __future__ import annotations

import pytest

# from my_package.billing.greeting import greet, normalize_name


def greet(name: str) -> str:
    raise NotImplementedError


def normalize_name(name: str) -> str:
    raise NotImplementedError


def test_greet_includes_name():
    name = "Ada"

    message = greet(name)

    assert message == "Hello, Ada!"


def test_normalize_name_strips_whitespace():
    raw = "  Ada  "

    result = normalize_name(raw)

    assert result == "Ada"


def test_greet_rejects_empty_name():
    with pytest.raises(ValueError, match="name must not be empty"):
        greet("")
