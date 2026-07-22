from enum import Enum
from abc import ABC,abstractmethod

class DenominationType(Enum):
    Note100 = 100
    Note50 = 50
    Note10 = 10

class BaseNotesHandler(ABC):
    def __init__(self):
        self.num_notes = 0
        self.next_handler = None
    
    def add_notes(self,num):
        self.num_notes+=num
    
    def set_next_handler(self,next_handler):
        self.next_handler = next_handler
        return self

    def can_dispense(self,amount) -> bool:
        if amount==0:
            return True
        notes_needed = amount//self.note.value
        if notes_needed==0:
            # delegate to lower denomination with same amount val
            return self.next_handler.can_dispense(amount) if self.next_handler else amount==0
        if self.num_notes >= notes_needed:
            # we have good quantity of notes with current denomination
            remaining_amount = amount - notes_needed*self.note.value
            return self.next_handler.can_dispense(remaining_amount) if self.next_handler else remaining_amount==0
        else:
            # we will consume all available notes of this denomination
            remaining_amount = amount - self.num_notes*self.note.value
            return self.next_handler.can_dispense(remaining_amount) if self.next_handler else remaining_amount==0
    
    def dispense(self,amount, notes_cnt) -> dict:
        if amount==0:
            return notes_cnt
        notes_needed = amount//self.note.value
        notes_cnt[self.note] = notes_needed
        if notes_needed==0:
            # delegate to lower denomination with same amount val
            return self.next_handler.dispense(amount,notes_cnt) if self.next_handler else notes_cnt
        else:
            # use available number of nodes
            remaining_amount = amount - min(notes_needed,self.num_notes)*self.note.value
            return self.next_handler.dispense(remaining_amount,notes_cnt) if self.next_handler else notes_cnt

class Notes100Handler(BaseNotesHandler):
    def __init__(self):
        super().__init__()
        self.note = DenominationType.Note100

class Notes50Handler(BaseNotesHandler):
    def __init__(self):
        super().__init__()
        self.note = DenominationType.Note50

class Notes10Handler(BaseNotesHandler):
    def __init__(self):
        super().__init__()
        self.note = DenominationType.Note10