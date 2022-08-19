from dao.customer_dao import CustomerDao
from exception.invalid_parameter import InvalidParameterError
from exception.customer_not_found import CustomerNotFoundError

class CustomerService:
    def __init__(self):
        self.customer_dao = CustomerDao()

        # Get a list of Customer objects from the DAO layer
        # convert the Customer objects into dictionaries
        # return a list of dictionaries that each represent the users
    def get_all_customers(self):
        list_of_customers_objs = self.customer_dao.get_all_customers()

        list_of_customer_dictionaries = []
        for customer_obj in list_of_customers_objs:
            list_of_customer_dictionaries.append(customer_obj.to_dict())

        return list_of_customer_dictionaries

    def get_customer_by_id(self, customer_id):
        customer_obj = self.customer_dao.get_customer_by_id(customer_id)

        if not customer_obj:
            raise CustomerNotFoundError(f"Customer with id {customer_id} was not found")

        return customer_obj.to_dict()