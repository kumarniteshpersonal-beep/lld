from user import User
from group import Group
from expense import Expense
from balance_sheet import BalanceSheet
from collections import defaultdict
from transaction import Transaction
from heapq import heapify, heappush, heappop
from threading import Lock

class SplitWiseService:
    _lock = Lock()
    
    def __init__(self):
        self.user = {} # id: User
        self.group = {} # id: Group
    
    def add_user(self, user: User):
        self.user[user.user_id] = user

    def add_group(self, group: Group):
        self.group[group.group_id] = group
    
    def create_expense(self, expense: Expense):
        with self._lock:
            splits = expense.calculate_splits()
            paid_by = expense.paid_by

            for split in splits:
                participant, share = split.participant, split.share
                participant.balance_sheet.update_balance(paid_by, share) # participant -> paid_by
                paid_by.balance_sheet.update_balance(participant, -share) # paid_by -> participant
            
            print(f"Expense '{expense.description}' of amount {expense.amount} created.")
    
    def get_simplified_transactions(self, group_id: str) -> list[Transaction]:
        all_participants = self.group[group_id].get_participants()
        net_balance_map = defaultdict(float)

        # calculating net money everyone needs to take or get
        for participant in all_participants:
            balance_sheet: BalanceSheet = participant.balance_sheet
            for other_user, amount in balance_sheet.balance.items():
                if other_user in all_participants:
                    if amount > 0:
                        net_balance_map[participant]-=amount
                    else:
                        net_balance_map[participant]+=abs(amount)
        
        # identifying creditors and debtors
        creditors = []
        debtors = []

        for _user, _amount in net_balance_map.items():
            if _amount > 0:
                creditors.append((-1*_amount, _user))
            else:
                debtors.append((_amount, _user))
        
        print("creditors:", creditors)
        print("debtors:", debtors)

        # calculate min transactions
        transactions = []
        heapify(creditors)
        heapify(debtors)
        
        while creditors and debtors:
            creditor_amount, creditor = heappop(creditors)
            debtor_amount, debtor = heappop(debtors)
            creditor_amount, debtor_amount = -1*creditor_amount, -1*debtor_amount

            settle_amount = min(creditor_amount, debtor_amount)
            transactions.append(Transaction(debtor, creditor, settle_amount))

            if settle_amount==creditor_amount:
                remaining_amount = debtor_amount-settle_amount
                if remaining_amount > 0:
                    heappush(debtors, (-remaining_amount, debtor))
            else:
                remaining_amount = creditor_amount-settle_amount
                if remaining_amount > 0:
                    heappush(creditors, (-remaining_amount, creditor))

        return transactions
    
    def settle(self, transaction):
        with self._lock:
            from_user, to_user, amount = transaction.from_user, transaction.to_user, transaction.amount
            try:
                transaction.settle_transaction()
                # now just reversing to nullify that balance
                from_user.balance_sheet.update_balance(to_user, -amount)
                to_user.balance_sheet.update_balance(from_user, amount)
            except Exception as e:
                print(f"error while money transfer due to e: {e}")
    
    def show_balance_sheet(self, user: User):
        user.balance_sheet.show_balance_sheet()