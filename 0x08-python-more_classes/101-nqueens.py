#!/usr/bin/python3

import sys

"""Initialize an NxN chessboard with empty spaces"""
def init_board(n):
    board = []
    """Create an NxN chessboard"""
    for i in range(n):
        board.append([' ' for i in range(n)])
    return board

"""Create a deep copy of the board"""
def board_deepcopy(board):
    return [row[:] for row in board]

"""Get the solution representation of the solved chessboard"""
def get_solution(board):
    solution = []
    """Identify the positions of the queens"""
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
    return solution

"""Check if placing a queen at board[row][col] is safe"""
def is_safe(board, row, col):
    """Check the row on the left side"""
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    """Check upper diagonal on the left side"""
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    """Check lower diagonal on the left side"""
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    """If safe, return True"""
    return True

"""Recursive function to solve the N-Queens problem"""
def solve_queens(board, col):
    """If all queens are placed then print the solution"""
    if col == len(board):
        solution = get_solution(board)
        print(solution)
        return

    """Try placing the queens in all rows one by one"""
    for i in range(len(board)):
        if is_safe(board, i, col):
            """Place the queen if it's safe"""
            board[i][col] = 'Q'
            """Recur to place the rest of the queens"""
            solve_queens(board, col + 1)
            """If placing a queen doesn't lead to a solution, backtrack"""
            board[i][col] = ' '

"""Main function to handle command-line arguments and start the solving process"""
def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    """Initialize the board"""
    board = init_board(n)
    """Start solving the N-Queens problem"""
    solve_queens(board, 0)

"""Execute the main function"""
if __name__ == "__main__":
    main()
