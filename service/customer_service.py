from dao.customer_dao import CustomerDao
from exception.invalid_parameter import InvalidParameterError
from exception.customer_not_found import CustomerNotFoundError
from utility.contains_letter import containsLetter
from utility.contains_num import containsNumber
from utility.contains_space import containsSpace
from utility.contains_spec_char import containsSpecChar


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

    # Get Customer object from the DAO layer and convert into a dictionary
    def get_customer_by_id(self, customer_id):
        customer_obj = self.customer_dao.get_customer_by_id(customer_id)

        if not customer_obj:
            raise CustomerNotFoundError(f"Customer with id {customer_id} was not found")

        return customer_obj.to_dict()

    def add_customer(self, customer_object):
        if " " in customer_object.username:
            raise InvalidParameterError("Username cannot contain space")

        if len(customer_object.username) < 6:
            raise  InvalidParameterError("Username must be at least 6 characters")

        added_customer_object = self.customer_dao.add_customer(customer_object)
        return added_customer_object.to_dict()