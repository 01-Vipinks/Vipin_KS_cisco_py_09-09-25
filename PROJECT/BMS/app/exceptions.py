class AccountException(Exception):
    """Base exception for Account operations."""
    pass

class AccountNotFoundError(AccountException):
    """Raised when an Account is not found."""
    pass

class AccountAlreadyExistError(AccountException):
    """Raised when trying to create an Account that already exists."""
    pass

class DatabaseError(AccountException):
    """General database operation error."""
    pass
