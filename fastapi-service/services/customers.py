from config import session
from model import Customer


class CustomerService:
    @staticmethod
    def get_customers():
        customers = session.query(Customer).all()
        res = [{
            "customer_id": c.customer_id,
            "first_name": c.first_name,
            "last_name": c.last_name,
            "email": c.email,
            "phone": c.phone,
            "address": c.address,
            "date_of_birth": c.date_of_birth,
            "account_balance": c.account_balance,
            "created_at": c.created_at
        } for c in customers]
        
        return res
    
    @staticmethod
    def create_customer(data):
        customer = Customer(**data)
        session.add(customer)
        session.commit()