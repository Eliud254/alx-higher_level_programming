#!/usr/bin/python3

import sys

def is_safe(board, row, col):
    # Check for queens attacking horizontally or diagonally
    for i in range(col):
        if board[i] == row or board[i] - i == row - col or board[i] + i == row + col:
            return False
    return True

def solve_nqueens(n, board, col):
    if col == n:
        print([[i, board[i]] for i in range(n)])
        return

    for i in range(n):
        if is_safe(board, i, col):
            board[col] = i
            solve_nqueens(n, board, col + 1)
            board[col] = -1

def nqueens(n):
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(n, board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
