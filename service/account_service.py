from dao.customer_dao import CustomerDao
from dao.account_dao import AccountDao
from exception.account_not_found import AccountNotFoundError
from exception.customer_not_found import CustomerNotFoundError
from exception.balance_error import InvalidBalanceError
from exception.invalid_account_type import InvalidAccountTypeError
from exception.invalid_parameter import InvalidParameterError
from utility.contains_letter import containsLetter
from utility.contains_num import containsNumber
from utility.contains_space import containsSpace
from utility.contains_spec_char import containsSpecChar

class AccountService:

    def __init__(self):
        self.account_dao = AccountDao()
        self.customer_dao = CustomerDao()

    def get_accounts(self):
        list_of_accounts = self.account_dao.get_accounts()
        return list(map(lambda a: a.to_dict(), list_of_accounts))
