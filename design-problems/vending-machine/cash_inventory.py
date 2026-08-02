from enum import Enum
from exception import InsufficientFundsException

class CashInventory:
    def __init__(self):
        cash10, cash5, cash2, cash1 = Cash10(), Cash5(), Cash2(), Cash1()
        self.cash_cnt = {
            DenominationType.ONE: cash1,
            DenominationType.TWO: cash2,
            DenominationType.FIVE: cash5,
            DenominationType.TEN: cash10
        }
        # build dispense handler
        cash10.set_next_handler(cash5)
        cash5.set_next_handler(cash2)
        cash2.set_next_handler(cash1)
        self.handler = cash10

    def add_money(self,cash_cnt: dict):
        for cash, cnt in cash_cnt.items():
            self.cash_cnt[cash].count += cnt
    
    def can_dispense(self,change: int):
        return self.handler.can_dispense(change)

    def dispense(self,change: int):
        if not self.can_dispense(change):
            raise InsufficientFundsException("we can't dispense the change due to insufficient cash, reconciliation will be performed")
        coin_freq = self.handler.dispense(change,{})
        for key,val in coin_freq.items():
            if val > 0:
                print(f"dispensing {val} coins of denomination {key.name}..")

class Cash:
    def __init__(self):
        self.count = 0
        self.next_handler = None
    
    def set_next_handler(self, next_handler):
        self.next_handler = next_handler

    def can_dispense(self, change: int):
        if change < self.denomination.value:
            return self.next_handler.can_dispense(change) if self.next_handler else change == 0
        coins_needed = min(change//self.denomination.value, self.count)
        return self.next_handler.can_dispense(change - coins_needed*self.denomination.value) if self.next_handler else (change - coins_needed*self.denomination.value == 0)
    
    def dispense(self,change: int, change_cnt: dict):
        if change < self.denomination.value:
            change_cnt[self.denomination] = 0
            return self.next_handler.dispense(change,change_cnt) if self.next_handler else change_cnt
        coins_needed = min(change//self.denomination.value, self.count)
        change_cnt[self.denomination] = coins_needed
        self.count -= coins_needed
        return self.next_handler.dispense(change-coins_needed*self.denomination.value,change_cnt)
    
    def __repr__(self):
        return f"{self.count} coins of denomination {self.denomination.value}"

class Cash1(Cash):
    def __init__(self):
        super().__init__()
        self.denomination = DenominationType.ONE

class Cash2(Cash):
    def __init__(self):
        super().__init__()
        self.denomination = DenominationType.TWO

class Cash5(Cash):
    def __init__(self):
        super().__init__()
        self.denomination = DenominationType.FIVE

class Cash10(Cash):
    def __init__(self):
        super().__init__()
        self.denomination = DenominationType.TEN

class DenominationType(Enum):
    ONE = 1
    TWO = 2
    FIVE = 5
    TEN = 10