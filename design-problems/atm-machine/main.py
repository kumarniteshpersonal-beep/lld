from cash_dispenser.notes_handler import DenominationType
from operation import WithDrawOperation, DepositOperation, FetchStatementOperation
from atm import ATM

# client code

def main():
    try:
        atm = ATM() # creating ATM obj
        atm.refill_cash({DenominationType.Note100: 2000, DenominationType.Note50: 4000, DenominationType.Note10: 50000}) # cash refilling by bank

        atm.insert_card(card_number="atmcard234") # insert the card and card state stored at atm machine
        atm.authenticate(pin="pin123") # perform auth using pin based auth

        atm.set_operation(operation=DepositOperation(atm)) # set operation to deposit
        atm.perform_operation(amount=280)
        atm.perform_operation(amount=130)

        atm.set_operation(operation=FetchStatementOperation(atm)) # set operation to fetch mini statement
        atm.perform_operation()

        atm.set_operation(operation=WithDrawOperation(atm)) # set operation to deposit
        atm.perform_operation(amount=290)

        atm.eject_card()
    except Exception as e:
        print(f"fail to complete the atm operations due to err: {e}")

# running main function
main()