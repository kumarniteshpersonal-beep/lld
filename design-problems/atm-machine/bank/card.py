class Card:
    def __init__(self, card_number, pin):
        self.__card_number = card_number
        self.__pin = pin
        self.account = None
    
    def get_card_number(self):
        return self.__card_number

    def is_pin_valid(self,pin) -> bool:
        return pin==self.__pin

    def set_account(self,account):
        self.account = account