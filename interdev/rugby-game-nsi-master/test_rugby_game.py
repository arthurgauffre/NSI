from unittest import TestCase

from rugby_game import RugbyGame


class RugbyGameTest(TestCase):
    def test_init_game(self):
        game = RugbyGame("UBB", "Toulouse")

        assert game.score() == "0-0"
    
    def test_drop_game(self):
        game = RugbyGame("Bordeaux", "Marseille")
        game.drop("Bordeaux")
        
        assert game.score() == "3-0"
