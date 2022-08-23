import dao.account_dao
import dao.customer_dao
from exception.customer_not_found import CustomerNotFoundError
from exception.customer_exists import CustomerAlreadyExistsError
from exception.invalid_parameter import InvalidParameterError
from exception.account_not_found import AccountNotFoundError
from exception.invalid_account_type import InvalidAccountTypeError
from exception.balance_error import InvalidBalanceError
from model.customer import Customer
from model.account import Account
from service.customer_service import CustomerService
from service.account_service import AccountService
import pytest


def test_get_accounts(mocker):
    def mock_get_accounts(self):
        return [Account(1, 1000, 8, "savings"), Account(2, 2000, 9, "checking"),
                Account(3, 1500, 10, "savings")]

    mocker.patch('dao.account_dao.AccountDao.get_accounts', mock_get_accounts)

    account_service = AccountService()

    actual = account_service.get_accounts()

    assert actual == [
        {
            "a_id": 1,
            "balance": 1000,
            "customer_id": 8,
            "type": "savings"
        },
        {
            "a_id": 2,
            "balance": 2000,
            "customer_id": 9,
            "type": "checking"
        },
        {
            "a_id": 3,
            "balance": 1500,
            "customer_id": 10,
            "type": "savings"
        }
    ]