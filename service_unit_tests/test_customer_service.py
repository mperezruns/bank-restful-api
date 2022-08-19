from dao.customer_dao import CustomerDao
from exception.invalid_parameter import InvalidParameterError
from exception.customer_not_found import CustomerNotFoundError
from model.customer import Customer
from service.customer_service import CustomerService
import pytest

def test_get_all_customers(mocker):
    # ARRANGE
    # MOCK METHOD FOR THE CUSTOMERDAO CLASS
    def mock_get_all_customers(self):
        return [Customer(1, 'Ruth Perez', 'Ruth', 'Perez', '1999-09-24', '626-833-4224', 'Azusa', 'ruthann777', True)]

    # ARRANGE
    mocker.patch('dao.customer_dao.CustomerDao.get_all_customers', mock_get_all_customers)

    customer_service = CustomerService()

    #ACT
    actual = customer_service.get_all_customers()

    # ASSERT
    assert actual == [
        {
            "id": 1,
            "customername": "Ruth Perez",
            "first_name": "Ruth",
            "last_name": "Perez",
            "birth_date": '1999-09-24',
            "customer_phone": '000-000-0004',
            "customer_city": 'Azusa',
            "username": 'ruthann777',
            "active": True
        }
    ]