from typing import List, Tuple, NamedTuple, Optional, Dict

# As a variable
# Tuple[bool, int] looks bas
# SpendResult = Tuple[bool, int]
# def spend(self, value: int) -> SpendResult:
#     if value <= 0:
#         return False, self.initial_balance
#     if self.initial_balance < value:
#         return False, self.initial_balance
#     self.initial_balance -= value
#     return True, self.initial_balance


# Nametuple
class SpendResult(NamedTuple):
    is_successful: bool
    balance: int


class Account(object):
    def __init__(self, name: str, initial_balance: int) -> None:
        self.name = name
        self.initial_balance = initial_balance
        reveal_type(self.initial_balance) # mypy parses reveal_type

    def credit(self, value: int) -> bool:
        if value <= 0:
            return False
        self.initial_balance += value
        return True

    def spend(self, value: int) -> SpendResult:
        if value <= 0:
            return SpendResult(False, self.initial_balance)
        if self.initial_balance < value:
            return SpendResult(False, self.initial_balance)
        self.initial_balance -= value
        return SpendResult(True, self.initial_balance)


class Customer(object):
    def __init__(self, name: str) -> None:
        self.name = name
        self.accounts: List[Account] = [] # of class types!
        self.primary_account_name: Optional[str] = None

    # Use quotes if class comes before account class
    def find_account_by_name(self, name: str) -> Optional['Account']:
        for account in self.accounts:
            # Refering to name attribute of account class
            if account.name == name:
                return account
        return None

    def add_account(self, account: Account) -> None:
        self.accounts.append(account)

    @property
    def primary_account(self) -> Optional[Account]:
        # Shows that Optional is Union[type, None]
        reveal_type(self.primary_account_name)
        if self.primary_account_name is None:
            return None
        return self.find_account_by_name(self.primary_account_name)


class Bank(object):
    def __init__(self) -> None:
        self.name_to_customer: Dict[str, Customer] = {}

    def add_customer(self, customers: List[Customer]) -> List[bool]:

        result = []
        for customer in customers:
            if customer.name in self.name_to_customer:
                result.append(False)
            else:
                self.name_to_customer[customer.name] = customer
                result.append(True)
        reveal_type(result)
        return result

    def transfer_funds(self, customer_name_from: str, customer_name_to: str, value: int) -> bool:
        if customer_name_from not in self.name_to_customer or customer_name_to not in self.name_to_customer:
            return False
        primary_account_from = self.name_to_customer[customer_name_from].primary_account
        primary_account_to = self.name_to_customer[customer_name_to].primary_account

        if primary_account_from is None or primary_account_to is None:
            return False

        if primary_account_from.spend(value).is_successful:
            primary_account_to.credit(value)
            return True
        return False


