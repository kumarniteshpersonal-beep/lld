from abc import abstractmethod, ABC
from expense import Expense
from user import User

class Split(ABC):
    def __init__(self, participant: User, share: float):
        self.participant = participant
        self.share = share

class SplitStrategy(ABC):
    @abstractmethod
    def calculate_splits(self, expense: Expense) -> list[Split]:
        pass

class EqualSplitStrategy(SplitStrategy):
    def calculate_splits(self, expense: Expense) -> list[Split]:
        amount = expense.amount
        other_participants = expense.additional_details.get("other_participants", [])
        share_for_each_participants = amount / (len(other_participants) + 1)

        splits = []

        for participant in other_participants:
            splits.append(Split(participant, share_for_each_participants))
            
        return splits

class ExactSplitStrategy(SplitStrategy):
    def calculate_splits(self, expense: Expense) -> list[Split]:
        other_participants = expense.additional_details.get("other_participants", [])
        other_participants_share = expense.additional_details.get("other_participants_share", [])

        if len(other_participants)!=len(other_participants_share):
            raise ValueError("other_participants lenght should be equals to other_participants_share")

        splits = []

        for idx in range(len(other_participants)):
            participant = other_participants[idx]
            share = other_participants_share[idx]
            splits.append(Split(participant, share))
                
        return splits