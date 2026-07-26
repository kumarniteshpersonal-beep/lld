from collections import deque
from game_pieces import Player, Dice
from board_entity import BoardEntity
from board import Board
import time

class Game:
    def __init__(self):
        self.dice: Dice = None
        self.players = deque()
        self.board: Board = None
        self.rankers: list[Player] = deque()
        turn: Player = None

    def play(self):
        # check for atleast 2 players
        if len(self.players) < 2:
            raise ValueError("At least 2 players should participate in the game")
        
        print("game started...")
        
        while len(self.players) > 1:
            print("running next turn...")
            time.sleep(2)

            self.turn = self.players.popleft() # set current player
            print(f"current player: {self.turn.name} is rolling the dice and is at position: {self.turn.pos}")
            jump = self.dice.roll()
            next_position = self.turn.pos + jump

            # check the case where next position exceded the max cell
            if next_position > self.board.cell_cnt:
                print(f"we can't move anywhere as next position is bigger than {self.board.cell_cnt}")
                final_position = self.turn.pos
            else:
                # get the final position after snake or ladder effect
                final_position = self.board.get_next_position(next_position)
                self.turn.pos = final_position

            # post process the pos
            if final_position==self.board.cell_cnt:
                print(f"hurray player: {self.turn.name} won! and got position: {len(self.rankers) + 1}")
                self.rankers.append(self.turn)
            elif jump==self.dice.max_num:
                # dice got max num hence we will again got one more chance
                print(f"player: {self.turn.name} got {jump} hence will again got the chance to roll the dice 😎")
                self.players.appendleft(self.turn)
            else:
                print(f"player: {self.turn.name} is now at position: {self.turn.pos}")
                self.players.append(self.turn) # append the player back to the queue
        
        # declare rankings
        print("game completed and rankings are as follows: ")
        for rank, player in enumerate(self.rankers, start=1):
            print(f"{rank}. {player.name}")

class GameBuilder:
    def __init__(self):
        self.game = Game()
    
    def set_dice(self, dice: Dice):
        self.game.dice = dice
        return self

    def set_players(self,players: list[Player]):
        self.game.players.extend(players)
        return self

    def set_board(self,entities: list[BoardEntity], board: Board):
        # register all entities like snake and ladder on board
        for entity in entities:
            board.register_entity(entity)

        self.game.board = board
        return self

    def build(self):
        return self.game