#
# practicepython.org Exercise 26: check winner

winner = 0 # caution! global variable

# Return number of the winner or 0 if no winner
    
def test_line(line):
    if all([item == 1 for item in line]):
        return 1
    if all([item == 2 for item in line]):
        return 2
    return 0

# Track whether there is a winner

def track_status(test_result):
    global winner
    if test_result != 0:
        winner = test_result

# Check each possible winning line on the board

def check_winner(board):
    
    global winner
    winner = 0
    
    # check rows
    for row in board:
        track_status(test_line(row))
            
    # check columns
    transpose = list(zip(*board))
    for row in transpose:
        track_status(test_line(row))
            
    # check diagonals
    track_status(test_line([board[0][0], board[1][1], board[2][2]]))
    track_status(test_line([board[0][2], board[1][1], board[2][0]]))
    
    # print result
    if winner:
        print(f"The winner is: {winner}")
    else:
        print("There is no winner")
    
if __name__ == "__main__":
    game_board = [[1, 2, 0],
              [2, 1, 0],
              [2, 1, 1]]
    check_winner(game_board)