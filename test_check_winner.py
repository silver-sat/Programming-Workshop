#
# Test the check winner function

from check_winner import check_winner
import unittest

class TestStringMethods(unittest.TestCase):

    def test_row(self):
        winner_is_1 =       [[2, 2, 0],
                            [2, 1, 0],
                            [1, 1, 1]]
        assert check_winner(winner_is_1) == 1

    def test_diagonal(self):
        game_board =        [[1, 2, 0],
                            [2, 1, 0],
                            [2, 1, 1]]
        assert check_winner(game_board) == 1

    def test_column(self):
        winner_is_2 =       [[2, 2, 0],
                            [2, 1, 0],
                            [2, 1, 1]]
        assert check_winner(winner_is_2) == 2

    def test_another_column(self):
        winner_is_also_1 =  [[0, 1, 0],
                            [2, 1, 0],
                            [2, 1, 1]]
        assert check_winner(winner_is_also_1) == 1

    def test_no_winner(self):
        no_winner =         [[1, 2, 0],
                            [2, 1, 0],
                            [2, 1, 2]]
        assert check_winner(no_winner) == 0

    def test_another_no_winner(self):
        also_no_winner =    [[1, 2, 0],
                            [2, 1, 0],
                            [2, 1, 0]]
        assert check_winner(also_no_winner) == 0

if __name__ == '__main__':
    unittest.main()
