from threading import Thread

class GameManager:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def start_all_games(self):
        threads = []

        for game in self.games:
            thread = Thread(target=game.play)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()