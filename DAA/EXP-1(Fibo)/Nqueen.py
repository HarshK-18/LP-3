def is_safe(board, row, col):
    # Check the left side of the column
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower-left diagonal
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens(board, col + 1):
                return True
            board[i][col] = 0

    return False

def print_board(board):
    for row in board:
        print(' '.join(['Q' if cell == 1 else '.' for cell in row]))

# Create an 8x8 chessboard
n = 8
chessboard = [[0] * n for _ in range(n)]

# Place the first queen in the first column
chessboard[0][0] = 1

# Call the solver function to place the remaining queens
if solve_n_queens(chessboard, 1):
    print("Solution found:")
    print_board(chessboard)
else:
    print("No solution found.")



# The `zip` function is used in the code to iterate over two sequences 
# in parallel. In the context of the 8-Queens problem, it's used to check 
# the diagonals for conflicts with existing queens on the chessboard.

#  Let me explain how it works:

# 1. Upper-Left Diagonal Check:
#    - To check the upper-left diagonal for a given position `(row, col)`,
#     we want to examine the cells in the diagonal that extends from the 
#     current cell towards the upper-left direction.
#    - We can achieve this by iterating over rows from `row` down to `0`
#     and columns from `col` down to `0` simultaneously.
#    - `zip(range(row, -1, -1), range(col, -1, -1))` combines these two
#     ranges into pairs of coordinates that represent the cells in the upper-left diagonal.

# 2. Lower-Left Diagonal Check:
#    - Similarly, to check the lower-left diagonal, we iterate over rows from `row`
#     up to the board size and columns from `col` down to `0`.
#    - Again, `zip(range(row, len(board), 1), range(col, -1, -1))` is used to create
#     pairs of coordinates for the cells in the lower-left diagonal.

# By using `zip`, we can easily generate pairs of coordinates to examine the cells 
# along the diagonals and check for conflicts with already placed queens. 
# It simplifies the code and makes it more readable by avoiding nested loops 
# and explicitly handling the coordinates.


# Explanation of the Code:

# 1. `is_safe` function:
#    - This function checks whether it's safe to place a queen on a specific cell `(row, col)` of the chessboard.
#    - It checks three conditions:
#      - The left side of the column to ensure no queens are already placed in the same column.
#      - The upper-left diagonal to ensure no queens are attacking from that direction.
#      - The lower-left diagonal to ensure no queens are attacking from that direction.
#    - If any of these conditions are violated, the function returns `False`, indicating 
#      that placing a queen at that location is not safe. Otherwise, it returns `True`.

# 2. `solve_n_queens` function:
#    - This function is a recursive backtracking algorithm for solving the N-Queens problem.
#    - It takes the `board` (chessboard) and the current `col` (column) as input.
#    - If `col` is equal to or greater than the size of the board, it means all queens have 
#      been successfully placed, and the function returns `True`.
#    - It tries to place a queen in each row of the current column by calling `is_safe` to 
#      check if the placement is safe.
#    - If a safe placement is found, the function marks the cell with a queen (1), recursively 
#      calls itself for the next column, and returns `True` if the subsequent placements are successful.
#    - If no safe placement is found, the function backtracks, sets the cell back to empty (0), 
#      and continues searching for a safe placement.

# 3. `print_board` function:
#    - This function is used to print the chessboard, representing queens as 'Q' and empty cells as '.'.

# 4. Main part of the code:
#    - It creates an 8x8 chessboard and places the first queen in the top-left cell.
#    - It then calls the `solve_n_queens` function to solve the N-Queens problem for the remaining 
#      queens (columns).
#    - If a solution is found, it prints the chessboard configuration with queens placed. 
#      If no solution is found, it indicates that no valid placement is possible.

# N-Queens Problem:

# The N-Queens problem is a classic combinatorial problem. Given an N×N chessboard, the 
# goal is to place N queens on the board in such a way that no two queens threaten each 
# other. In other words, no two queens can share the same row, column, or diagonal. Solving 
# the N-Queens problem requires finding all distinct configurations of queens on the board 
# that satisfy these constraints.

# Time and Space Complexity:

# - Time Complexity: The time complexity of the code depends on the efficiency of the 
# backtracking algorithm. In the worst case, it explores all possible configurations of 
# queens on the board. Therefore, the time complexity is exponential, O(N!), where 'N' 
# is the size of the chessboard.

# - Space Complexity: The space complexity is determined by the space used for the 
# `chessboard`. It's O(N^2) because the board is an N×N matrix. Additionally, the 
# recursive call stack may consume space, but it is bounded by the depth of recursion,
#  which is at most 'N'. So, the overall space complexity is O(N^2).

# In summary, the code efficiently solves the N-Queens problem using a 
# backtracking algorithm. However, the time complexity grows rapidly with 
# the size of the chessboard, making it impractical for very large board sizes.