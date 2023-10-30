#!/usr/bin/python3
# 101-nqueens.py
"""Trying to Solves the N-queens puzzle."""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    return [[' ' for i in range(n)] for j in range(n)]


def is_safe(board, row, col, n):
    """Check if the current position is safe to place a queen."""
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_nqueens(board, col, n, solutions):
    """Solve the N-queens puzzle using backtracking."""
    if col == n:
        solutions.append(get_solution(board))
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 'Q'
            solve_nqueens(board, col + 1, n, solutions)
            board[i][col] = ' '

def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for row in board:
        for i, val in enumerate(row):
            if val == 'Q':
                solution.append([board.index(row), i])
    return solution


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    n = int(sys.argv[1])
    board = init_board(n)
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    
    for sol in solutions:
        print(sol)

