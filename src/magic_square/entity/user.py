"""User entity for ECB domain layer."""

from __future__ import annotations

from dataclasses import dataclass
import re

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


@dataclass(slots=True)
class User:
    """Represents a domain user with simple identity and status rules.

    Attributes:
        user_id: Positive unique identifier.
        username: Display name that cannot be blank.
        email: Contact email in basic valid format.
        is_active: User active status.
    """

    user_id: int
    username: str
    email: str
    is_active: bool = True

    def __post_init__(self) -> None:
        """Validates invariants after initialization."""
        self._validate_user_id(self.user_id)
        self.username = self._normalize_username(self.username)
        self.email = self._normalize_email(self.email)

    @classmethod
    def create(cls, user_id: int, username: str, email: str) -> User:
        """Creates an active user with validated values.

        Args:
            user_id: Positive user identifier.
            username: Non-empty username.
            email: User email address.

        Returns:
            A validated active User instance.
        """
        return cls(user_id=user_id, username=username, email=email, is_active=True)

    def rename(self, new_username: str) -> None:
        """Updates username with validation.

        Args:
            new_username: New non-empty username.
        """
        self.username = self._normalize_username(new_username)

    def change_email(self, new_email: str) -> None:
        """Updates email with validation.

        Args:
            new_email: New email address.
        """
        self.email = self._normalize_email(new_email)

    def deactivate(self) -> None:
        """Marks this user as inactive."""
        self.is_active = False

    @staticmethod
    def _validate_user_id(user_id: int) -> None:
        if user_id <= 0:
            raise ValueError("user_id must be a positive integer.")

    @staticmethod
    def _normalize_username(username: str) -> str:
        normalized = username.strip()
        if not normalized:
            raise ValueError("username must not be blank.")
        return normalized

    @staticmethod
    def _normalize_email(email: str) -> str:
        normalized = email.strip().lower()
        if not EMAIL_PATTERN.match(normalized):
            raise ValueError("email must be a valid address.")
        return normalized
