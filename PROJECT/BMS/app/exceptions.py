"""
Custom exceptions for Account operations in Banking Management System.

Defines clear exception hierarchy for domain-specific errors.
"""

class AccountException(Exception):
    """Base exception for Account operations."""

class AccountNotFoundError(AccountException):
    """Raised when an Account is not found."""

class AccountAlreadyExistError(AccountException):
    """Raised when trying to create an Account that already exists."""

class DatabaseError(AccountException):
    """General database operation error."""
