import json
import os


class CustomerService:
    @staticmethod
    def get_customers(page=1, limit=10):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "../data", "customers.json")
        
        with open(file_path, "r") as f:
            customers = json.load(f)
        
        total = len(customers)
        start = (page - 1) * limit
        end   = start + limit

        return {
            "data":  customers[start:end],
            "total": total,
            "page":  page,
            "limit": limit
        }

    @staticmethod
    def get_customer_by_id(customer_id: int):
        base_dir  = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "../data", "customers.json")

        with open(file_path, "r") as f:
            customers = json.load(f)

        for customer in customers:
            if customer["customer_id"] == customer_id:
                return customer

        return None