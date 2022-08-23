from flask import Blueprint, request

from model.account import Account
from exception.invalid_parameter import InvalidParameterError
from exception.balance_error import InvalidBalanceError
from exception.invalid_account_type import InvalidAccountTypeError
from exception.invalid_parameter import InvalidParameterError
from service.account_service import AccountService

ac = Blueprint('account_controller', __name__)

account_service = AccountService()

@ac.route('/accounts')
def get_accounts():
    return {
        "accounts": account_service.get_accounts()
    }