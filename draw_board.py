# Draw a game board
#

import sys

# Constants

max_size = 30
grid_size = 3
blank = ' '
horizontal = '-'
vertical = '|'

# Helper to print a row

def print_row(board, grid, first_char, second_char):
    print(first_char, end = '')
    for _ in range(board):
        for _ in range(grid):
            print(second_char, end = '')
        print(first_char, end = '')
    print()

def main():

# Get the board size

    while True:
        entry = input(f"Enter the board size up to {max_size} ('q' to quit): ")
        if entry[0].casefold() == 'q':
            sys.exit()
        try:
            board_size = int(entry)
            if board_size < 1 or board_size > 30:
                raise ValueError
            break
        except ValueError:
            print("That is not a valid board size. Try again...")

# Print the game board

    print_row(board_size, grid_size, blank, horizontal)
    for _ in range(board_size):
        print_row(board_size, grid_size, vertical, blank)
        print_row(board_size, grid_size, blank, horizontal)        
    
if __name__ == "__main__":
    main()
