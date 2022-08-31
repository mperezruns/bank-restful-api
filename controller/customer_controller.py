from flask import Blueprint, request

from service.customer_service import CustomerService
from model.customer import Customer
from exception.invalid_parameter import InvalidParameterError
from exception.customer_not_found import CustomerNotFoundError
from exception.customer_exists import CustomerAlreadyExistsError

cc = Blueprint('customer_controller', __name__)

# Instantiate a CustomerService Object
customer_service = CustomerService()

# FIRST ENDPOINT
@cc.route('/customers')
def get_all_customers():
    return {
        "customers": customer_service.get_all_customers()
    }

# SECOND ENDPOINT
@cc.route('/customers/<customer_id>')   # GET /customers/<customer_id>
def get_customer_by_id(customer_id):
    try:
        return customer_service.get_customer_by_id(customer_id)     # dictionary
    except CustomerNotFoundError as e:
        return {
                    "message": str(e)
                }, 404

# THIRD ENDPOINT
@cc.route('/customers', methods=['POST'])   # POST /customers (add a new customer to the table)
def add_customer():
    customer_json_dictionary = request.get_json()
    customer_object = Customer(None, customer_json_dictionary['customername'], customer_json_dictionary['first_name'],
                               customer_json_dictionary['last_name'], customer_json_dictionary['customer_phone'],
                               customer_json_dictionary['customer_city'], customer_json_dictionary['username'], None)

    try:
        return customer_service.add_customer(customer_object), 201
        # 201 created
    except InvalidParameterError as e:
        return {
            "message": str(e)
        }, 400