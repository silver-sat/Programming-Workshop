#
# Test the check winner function

from check_winner import check_winner

game_board =        [[1, 2, 0],
                     [2, 1, 0],
                     [2, 1, 1]]
check_winner(game_board)

winner_is_2 =       [[2, 2, 0],
                     [2, 1, 0],
                     [2, 1, 1]]
check_winner(winner_is_2)

winner_is_1 =       [[1, 2, 0],
                     [2, 1, 0],
                     [2, 1, 1]]
check_winner(winner_is_1)

winner_is_also_1 =  [[0, 1, 0],
                     [2, 1, 0],
                     [2, 1, 1]]
check_winner(winner_is_also_1)

no_winner =         [[1, 2, 0],
                     [2, 1, 0],
                     [2, 1, 2]]
check_winner(no_winner)

also_no_winner =    [[1, 2, 0],
                     [2, 1, 0],
                     [2, 1, 0]]
check_winner(also_no_winner)
