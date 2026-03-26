from config import Base
from sqlalchemy import DECIMAL, TIMESTAMP, Column, Date, String, Text


class Customer(Base):
    __tablename__ = "customers"

    customer_id     = Column(String(50),   primary_key=True)
    first_name      = Column(String(100),  nullable=False)
    last_name       = Column(String(100),  nullable=False)
    email           = Column(String(255),  nullable=False)
    phone           = Column(String(20))
    address         = Column(Text)
    date_of_birth   = Column(Date)
    account_balance = Column(DECIMAL(15, 2))
    created_at      = Column(TIMESTAMP)

    def __init__  (self, customer_id, first_name, last_name, email, phone=None, address=None, date_of_birth=None, account_balance=0.00, created_at=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.date_of_birth = date_of_birth
        self.account_balance = account_balance
        self.created_at = created_at