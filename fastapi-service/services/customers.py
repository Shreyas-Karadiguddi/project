from config import session
from model import Customer


class CustomerService:
    @staticmethod
    def get_customers(page=1, limit=10):
        offset    = (page - 1) * limit
        total     = session.query(Customer).count()
        customers = session.query(Customer).offset(offset).limit(limit).all()

        res = [{
            "customer_id":     c.customer_id,
            "first_name":      c.first_name,
            "last_name":       c.last_name,
            "email":           c.email,
            "phone":           c.phone,
            "address":         c.address,
            "date_of_birth":   str(c.date_of_birth),
            "account_balance": float(c.account_balance),
            "created_at":      str(c.created_at)
        } for c in customers]

        return {
            "data":  res,
            "total": total,
            "page":  page,
            "limit": limit
        }
    
    @staticmethod
    def get_customer_by_id(customer_id: str):
        customer = session.query(Customer).filter(Customer.customer_id == customer_id).first()
        
        if not customer:
            return None

        return {
            "customer_id":     customer.customer_id,
            "first_name":      customer.first_name,
            "last_name":       customer.last_name,
            "email":           customer.email,
            "phone":           customer.phone,
            "address":         customer.address,
            "date_of_birth":   str(customer.date_of_birth),
            "account_balance": float(customer.account_balance),
            "created_at":      str(customer.created_at)
        }
    
    @staticmethod
    def create_customer(data):
        customer = Customer(**data)
        session.add(customer)
        session.commit()