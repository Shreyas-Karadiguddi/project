from api.customers.endpoint import namespace as customers_namespace
from flask import Flask
from flask_cors import CORS
from flask_restx import Api

PORT = 5001
app = Flask(__name__)

CORS(app)

api = Api(app, version='1.0', title='Customer API', description='A simple Customer API', prefix='/api')

api.add_namespace(customers_namespace)

if __name__ == "__main__":
    print("FLASK IS RUNNING")
    app.run(port=PORT, host="0.0.0.0", debug=True)

