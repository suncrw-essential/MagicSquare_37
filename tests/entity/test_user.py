"""Entity tests for the User domain model."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from magic_square.entity.user import User


def test_user_create_initializes_fields() -> None:
    """Creates a user with valid required values."""
    # Arrange
    user_id = 1
    username = "alice"
    email = "alice@example.com"

    # Act
    user = User.create(user_id=user_id, username=username, email=email)

    # Assert
    assert user.user_id == user_id
    assert user.username == username
    assert user.email == email
    assert user.is_active is True


def test_user_create_raises_for_blank_username() -> None:
    """Rejects blank username values."""
    # Arrange
    user_id = 1
    username = "   "
    email = "alice@example.com"

    # Act / Assert
    with pytest.raises(ValueError, match="username"):
        User.create(user_id=user_id, username=username, email=email)


def test_user_create_raises_for_invalid_email() -> None:
    """Rejects invalid email format."""
    # Arrange
    user_id = 1
    username = "alice"
    email = "invalid-email"

    # Act / Assert
    with pytest.raises(ValueError, match="email"):
        User.create(user_id=user_id, username=username, email=email)


def test_user_rename_updates_username() -> None:
    """Updates username with a valid new value."""
    # Arrange
    user = User.create(user_id=1, username="alice", email="alice@example.com")
    new_username = "alice_new"

    # Act
    user.rename(new_username)

    # Assert
    assert user.username == new_username


def test_user_deactivate_sets_user_inactive() -> None:
    """Deactivates an active user."""
    # Arrange
    user = User.create(user_id=1, username="alice", email="alice@example.com")

    # Act
    user.deactivate()

    # Assert
    assert user.is_active is False
