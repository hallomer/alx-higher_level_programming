#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    """
    Check if there is a queen in the same column.
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    """
    Check if there is a queen in the upper-left diagonal.
    """
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    """
    Check if there is a queen in the upper-right diagonal.
    """
    i = row
    j = col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens_util(board, row, N):
    if row == N:
        """
        Solution found, print the board.
        """
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
    else:
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                solve_nqueens_util(board, row + 1, N)
                board[row][col] = 0


def solve_nqueens(N):
    """
    Check if N is a positive integer.
    """
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    """
    Check if N is at least 4.
    """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens_util(board, 0, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
