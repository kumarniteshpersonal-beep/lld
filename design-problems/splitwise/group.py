from user import User

class Group:
    def __init__(self, group_id: str ,participants: list[User]):
        self.participants = participants
        self.group_id = group_id
    
    def get_participants(self):
        return self.participants
    
    def __hash__(self):
        return self.group_id