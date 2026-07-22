from cash_dispenser import CashDispenser
from bank import BankSVC
from bank.card import Card
from operation import Operation

class ATM:
    def __init__(self):
        self.dispenser: CashDispenser = CashDispenser()
        self.bank_svc: BankSVC = BankSVC()
        self.current_card: Card = None
        self.current_operation: Operation = None

        # dummy to pupulate some data in bank
        account = self.bank_svc.create_account("account123") # create an account
        card = self.bank_svc.create_atm_card("atmcard234","pin123") # create atm card with pin
        self.bank_svc.link_account_and_atm_card(card,account) # link card to account number

    def refill_cash(self,denomination_cnt_map):
        self.dispenser.refill_cash(denomination_cnt_map)
    
    def insert_card(self, card_number):
        self.current_card = self.bank_svc.atm_cards[card_number]
    
    def get_current_card(self):
        return self.current_card
    
    def authenticate(self, pin):
        self.bank_svc.authenticate(pin,self.current_card)
    
    def set_operation(self,operation):
        self.current_operation = operation

    def perform_operation(self,**kwargs):
        self.current_operation.perform(**kwargs)

    def eject_card(self):
        self.current_card = None