import json
import os


class CustomerService:
    @staticmethod
    def get_customers():
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "../data", "customers.json")
        
        with open(file_path, "r") as f:
            customers = json.load(f)
        
        return customers