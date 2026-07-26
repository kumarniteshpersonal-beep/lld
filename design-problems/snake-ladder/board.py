from board_entity import BoardEntity

class Board:
    def __init__(self, cell_cnt: int):
        self.entities: dict = {}
        self.cell_cnt = cell_cnt
    
    def register_entity(self, entity: BoardEntity):
        self.entities[entity.start] = entity.end

    def get_next_position(self, pos: int):
        if pos in self.entities:
            new_pos = self.entities[pos]
            if (new_pos - pos) > 0:
                print(f"climbing the ladder 🪜 and moving from pos: {pos} -> {new_pos}")
            else:
                print(f"snake 🐍 bites hence  moving from pos: {pos} -> {new_pos}")
            return new_pos
        return pos