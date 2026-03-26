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