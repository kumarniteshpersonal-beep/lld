from splitwise_service import SplitWiseService
from user import User
from group import Group
from split import EqualSplitStrategy, ExactSplitStrategy
from expense import ExpenseBuilder

class SplitWiseApplication:
    @staticmethod
    def main():
        svc = SplitWiseService()

        # add some users
        nitesh, anmol, ritu, ashu = User("nitesh", "Nitesh"), User("anmol", "Anmol"), User("ritu", "Ritu"), User("ashu", "Ashu")
        svc.add_user(nitesh)
        svc.add_user(anmol)
        svc.add_user(ritu)
        svc.add_user(ashu)

        # create a group
        group = Group("hyderabad trip", [nitesh, anmol, ritu, ashu])
        svc.add_group(group)

        # create an expense
        svc.create_expense(
            ExpenseBuilder()
            .set_description("dinner")
            .set_amount(412.0)
            .set_paid_by(nitesh)
            .set_split_strategy(EqualSplitStrategy())
            .set_additional_details({"other_participants": [anmol, ritu, ashu]})
            .build()
        )
        svc.show_balance_sheet(nitesh)

        # create another expense
        svc.create_expense(
            ExpenseBuilder()
            .set_description("lunch")
            .set_amount(805.0)
            .set_paid_by(ashu)
            .set_split_strategy(ExactSplitStrategy())
            .set_additional_details({"other_participants": [anmol, ritu, nitesh], "other_participants_share": [230.0, 100.0, 305.0]})
            .build()
        )
        svc.show_balance_sheet(nitesh)

        # simplified transactions for a hyderabad trip
        transactions = svc.get_simplified_transactions("hyderabad trip")
        print("simplified transactions ->")
        print(transactions)

if __name__=="__main__":
    SplitWiseApplication.main()