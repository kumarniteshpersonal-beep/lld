from bank.account import Account
from bank.card import Card

class BankSVC:
    def __init__(self):
        # in main systems this should be drive via api or db but here I am managing the map
        self.accounts = {}
        self.atm_cards = {}
        self.atm_card_to_account_map = {}

    def create_account(self, account_id):
        account = Account(account_id)
        self.accounts[account_id] = account
        return account

    def create_atm_card(self, card_number, pin):
        card = Card(card_number, pin)
        self.atm_cards[card_number] = card
        return card

    def link_account_and_atm_card(self, card, account):
        self.atm_card_to_account_map[card.get_card_number()] = account
        card.set_account(account)
    
    def authenticate(self, pin, card):
        pin_valid = card.is_pin_valid(pin)
        if not pin_valid:
            raise Exception("invalid pin")
    
    def get_account_by_card(self,card: Card):
        return self.atm_card_to_account_map[card.get_card_number()]

    def deposit(self,account: Account, amount: int):
        account.credit(amount=amount)
    
    def debit(self,account: Account, amount: int) -> bool:
        return account.debit(amount=amount)