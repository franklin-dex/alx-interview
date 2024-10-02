#!/usr/bin/python3
"""
Solves the N Queens puzzle using backtracking.
"""


import sys

def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col].
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(N):
    """
    Solve the N Queens problem and print all solutions.
    """
    def backtrack(board, row):
        if row == N:
            solution = [[i, board[i].index(1)] for i in range(N)]
            print(solution)
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                backtrack(board, row + 1)
                board[row][col] = 0

    board = [[0] * N for _ in range(N)]
    backtrack(board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
