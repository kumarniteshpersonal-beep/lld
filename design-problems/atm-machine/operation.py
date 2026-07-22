from enum import Enum
from abc import ABC,abstractmethod
from bank.account import Account

class OperationType(Enum):
    WITHDRAW = 1
    FETCH_STATEMENT = 2
    DEPOSIT = 3

class Operation(ABC):
    def __init__(self, _atm):
        self.atm = _atm

    def get_current_account(self) -> Account:
        current_card = self.atm.get_current_card()
        account: Account = self.atm.bank_svc.get_account_by_card(current_card)
        return account

    @abstractmethod
    def perform(self):
        pass

class WithDrawOperation(Operation):
    def perform(self, **kwargs):
        amount = kwargs["amount"]
        # did atm has the required cash ?
        if not self.atm.dispenser.can_dispense(amount):
            raise RuntimeError("atm does't have the required cash quantity")

        print("atm has desired amount of notes!")
        account: Account = self.get_current_account()
        is_debited = self.atm.bank_svc.debit(account,amount)
        if not is_debited:
            raise RuntimeError("insufficient balance")
        
        # dispense the case
        try:
            print("dispensing the notes..")
            notes_cnt = self.atm.dispenser.dispense(amount)
            for key,val in notes_cnt.items():
                print(f"dispensing {val} notes for denomination: {key.value}")
        except Exception as e:
            print(f"error occurs while withdraw operation due to: {e}")
            self.atm.bank_svc.deposit(account,amount) # else deposit amount bank to account
            raise e

class FetchStatementOperation(Operation):
    def perform(self):
        account: Account = self.get_current_account()
        print(f"current balance for account_number: {account.get_account_number()} is {account.get_balance()}")

class DepositOperation(Operation):
    def perform(self, **kwargs):
        amount = kwargs["amount"]
        account: Account = self.get_current_account()
        self.atm.bank_svc.deposit(account,amount)