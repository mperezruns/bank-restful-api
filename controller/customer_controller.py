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
        return customer_service.get_customer_by_id(customer_id)
    except CustomerNotFoundError as e:
        return {
                    "message": str(e)
                }, 404
