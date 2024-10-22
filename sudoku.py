# Sudoku Solver using Backtracking

# Function to check if the current number is valid in the given position
def is_valid(board, row, col, num):
    # Check if the number exists in the row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check if the number exists in the column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check if the number exists in the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

# Function to solve the Sudoku puzzle
def solve_sudoku(board):
    # Find the next empty cell
    empty = find_empty_location(board)
    if not empty:
        return True  # Puzzle solved
    row, col = empty

    # Try placing numbers 1 to 9 in the current cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num  # Assign number

            # Recursively solve the rest of the board
            if solve_sudoku(board):
                return True

            # Backtrack if the solution is not possible
            board[row][col] = 0

    return False

# Helper function to find an empty location on the board
def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

# Function to print the Sudoku board
GREEN = '\033[92m'
RESET = '\033[0m'

def print_board(board):
    # Top outer border with green color
    print(GREEN + "+-------+-------+-------+" + RESET)

    for i in range(9):
        if i % 3 == 0 and i != 0:
            # Green horizontal separator between 3x3 subgrids
            print(GREEN + "+-------+-------+-------+" + RESET)
        
        for j in range(9):
            if j % 3 == 0:
                # Green vertical separator between 3x3 subgrids
                print(GREEN + "| " + RESET, end="")
            
            # Print each number in the row
            if board[i][j] == 0:
                print("_ ", end="")  # Use '.' to represent empty cells for better visibility
            else:
                print(f"{board[i][j]} ", end="")

        # End of the row, close with green vertical border
        print(GREEN + "|" + RESET)

    # Bottom outer border with green color
    print(GREEN + "+-------+-------+-------+" + RESET)


# # Initialize the board (9x9)
# board = [[0 for _ in range(9)] for _ in range(9)]

# # Get user input for the Sudoku puzzle
# print("Enter Sudoku values (row by row). Enter '0' where the cell is empty.")
# for i in range(9):
#     row_input = input(f"Enter 9 numbers for row {i+1} (separated by spaces): ").split()
#     for j in range(9):
#         board[i][j] = int(row_input[j])


board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print_board(board)

# Solve the Sudoku puzzle
if solve_sudoku(board):
    print("\nSudoku solved successfully!")
    print_board(board)
else:
    print("No solution exists.")
