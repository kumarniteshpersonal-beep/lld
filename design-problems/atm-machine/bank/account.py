from threading import Lock

class Account:
    def __init__(self, account_number):
        self.__balance = 0
        self.__account_number = account_number
        self._lock = Lock()
    
    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        with self._lock:
            return self.__account_number
    
    def credit(self, amount):
        # acquire lock around atomic operation because they can cause race condition - correctness pattern
        with self._lock:
            self.__balance+=amount

    def debit(self, amount):
        # acquire lock around atomic operation because they can cause race condition - correctness pattern
        with self._lock:
            if self.__balance>=amount:
                self.__balance-=amount
                return True
            return False