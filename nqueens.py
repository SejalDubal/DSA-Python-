def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper-left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the upper-right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row, n):
    # If all queens are placed, return True
    if row == n:
        return True

    for col in range(n):
        # If placing queen at (row, col) is safe
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place the queen

            # Recur to place the next queen
            if solve_n_queens(board, row + 1, n):
                return True

            # Backtrack: remove the queen
            board[row][col] = 0

    return False

def print_board(board):
    for row in board:
        print(" ".join(["Q" if x == 1 else "." for x in row]))

def n_queens(n):
    board = [[0] * n for _ in range(n)]  # Initialize the board with 0 (no queens)
    
    if not solve_n_queens(board, 0, n):
        print("Solution does not exist.")
        return False
    
    print("Solution found:")
    print_board(board)
    return True

# User input for number of queens
n = int(input("Enter the number of queens: "))
n_queens(n)
