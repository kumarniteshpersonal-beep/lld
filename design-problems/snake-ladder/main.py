from game import GameBuilder
from game_pieces import Player, Dice
from board import Board
from board_entity import Snake, Ladder
from game_manager import GameManager


class GameService:
    @staticmethod
    def create_game(player_names):
        game_builder = GameBuilder()

        dice = Dice(1, 6)

        players = [Player(name) for name in player_names]

        board = Board(100)

        entity_list = [
            Snake(17, 7),
            Snake(25, 6),
            Snake(34, 4),
            Snake(44, 8),
            Snake(55, 9),
            Snake(99, 3),

            Ladder(3, 37),
            Ladder(5, 18),
            Ladder(19, 84),
            Ladder(49, 80),
            Ladder(55, 90),
            Ladder(64, 98)
        ]

        return (
            game_builder
            .set_dice(dice)
            .set_players(players)
            .set_board(entity_list, board)
            .build()
        )

    @staticmethod
    def main():
        game_manager = GameManager() # create a gamemanager
        
        game1 = GameService.create_game(
            ["Nitesh", "Anmol", "Ritu"]
        )
        game2 = GameService.create_game(
            ["Alice", "Bob"]
        )

        game_manager.add_game(game1)
        game_manager.add_game(game2)

        game_manager.start_all_games() # run all games concurrently


if __name__ == "__main__":
    GameService.main()