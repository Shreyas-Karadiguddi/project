from flask_restx import Namespace, Resource
from services.customers import CustomerService

namespace = Namespace('customers', description='Customers related operations')

@namespace.route('/')
class CustomersResource(Resource):
    def get(self):
        return CustomerService.get_customers()