from iebank_api.models import Account
import pytest

def test_create_account():
    """
    GIVEN an Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status, country, and created_at fields are defined correctly
    """
    account = Account('John Doe', '€', 'Spain')
    assert account.name == 'John Doe'
    assert account.currency == '€'
    assert account.account_number != None
    assert account.balance == 0.0
    assert account.status == 'Active'
    assert account.country == 'Spain'


def test_default_status():
    """
    GIVEN an Account model
    WHEN a new Account is created
    THEN check the status is defaulted to 'Active'
    """
    account = Account('Jane Doe', '€', 'Germany')
    assert account.status == 'Active'