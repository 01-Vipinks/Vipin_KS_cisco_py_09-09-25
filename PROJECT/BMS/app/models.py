from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Account(db.Model):
    __tablename__ = "accounts"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    number = db.Column(db.String(50), nullable=False)
    balance = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Account id={self.id} name={self.name} number={self.number} balance={self.balance}>'  
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "number": self.number,
            "balance": self.balance
        }
