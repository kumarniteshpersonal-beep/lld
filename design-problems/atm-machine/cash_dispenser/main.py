from cash_dispenser.notes_handler import Notes100Handler, Notes10Handler, Notes50Handler
from cash_dispenser.notes_handler import DenominationType
from threading import Lock

class CashDispenser:
    def __init__(self):
        notes100, notes50, notes10 = Notes100Handler(), Notes50Handler(), Notes10Handler()
        self.denomination_cnt_map = {
            DenominationType.Note100: notes100,
            DenominationType.Note50: notes50,
            DenominationType.Note10: notes10
        }
        self.handler = notes100
        # build chain to delegate responsibility
        notes100.set_next_handler(notes50)
        notes50.set_next_handler(notes10)

        # lock instance
        self._lock = Lock()
        
    def refill_cash(self,denomination_map):
        with self._lock:
            print("refilling the cash..")
            for key,val in denomination_map.items():
                print(f"{val} notes added for denominations {key.value}")
                self.denomination_cnt_map[key].add_notes(val)

    def dispense(self,amount):
        if amount <= 0:
            raise ValueError("amount should be bigger than zero")
        with self._lock:
            # we are checking again for more correctness so first acquire lock then check and act
            can_dispense = self.handler.can_dispense(amount=amount)
            if not can_dispense:
                raise RuntimeError("we can't dispense the amount from atm due to insufficient cash, reconciliation will be performed")
            notes_cnt = {}
            return self.handler.dispense(amount,notes_cnt)
    
    def can_dispense(self,amount) -> bool:
        # this is pre-check / fast correctness check to avoid lock acquisition if not required
        if amount <= 0:
            return False
        return self.handler.can_dispense(amount=amount)