from flask import request
from flask_restx import Namespace, Resource
from services.customers import CustomerService

namespace = Namespace('customers', description='Customers related operations')

@namespace.route('/')
class CustomersResource(Resource):
    def get(self):
        page  = request.args.get('page',  1,  type=int)
        limit = request.args.get('limit', 10, type=int)
        return CustomerService.get_customers(page=page, limit=limit)
    
@namespace.route('/<string:customer_id>')
class CustomerResource(Resource):
    def get(self, customer_id):
        customer = CustomerService.get_customer_by_id(int(customer_id))
        
        if not customer:
            return {"message": "Customer not found"}, 404

        return customer, 200


@namespace.route('/health')
class HealthResource(Resource):
    def get(self):
        return {"status": "ok"}, 200