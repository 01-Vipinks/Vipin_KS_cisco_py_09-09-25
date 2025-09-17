"""
Database model definitions for Banking Management System.

Defines ORM models representing the database tables.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Account(db.Model):
    """
    Account model representing a bank account record.

    Attributes:
        id (int): Primary key account ID.
        name (str): Account holder's name.
        number (str): Account number.
        balance (float): Account balance.
    """
    __tablename__ = "accounts"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    number = db.Column(db.String(50), nullable=False)
    balance = db.Column(db.Float, nullable=False)

    def __repr__(self):
        """
        Return human-readable representation of the Account instance.
        """
        return (
            f'<Account id={self.id} name={self.name} number={self.number} '
            f'balance={self.balance}>'
        )

    def to_dict(self):
        """
        Convert Account instance into a dictionary.

        Returns:
            dict: Account attributes as a dictionary.
        """
        return {
            "id": self.id,
            "name": self.name,
            "number": self.number,
            "balance": self.balance
        }
