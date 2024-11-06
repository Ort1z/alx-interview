#!/usr/bin/python3

import sys


def is_safe(board, row, col):
    """
    Checks if placing a queen at (row, col) is safe (no attacks).

    Args:
        board: List representing the chessboard with queen positions.
        row: Integer representing the row index.
        col: Integer representing the column index.

    Returns:
        True if the placement is safe, False otherwise.
    """

    # Check for queens in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check for queens in diagonals
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(board, col):
    """
    Solves the N-Queens problem using backtracking.

    Args:
        board: List representing the chessboard (initially empty).
        col: Integer representing the current column (starts with 0).

    Returns:
        None if no solution exists, otherwise prints all solutions.
    """

    # Base case: All queens are placed
    if col == len(board):
        print_solution(board)
        return

    # Try placing a queen in all safe positions in the current row
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_n_queens(board, col + 1)
            # Backtrack: remove queen from current position
            board[i][col] = 0


def print_solution(board):
    """
    Prints the chessboard representation of a solution.

    Args:
        board: List representing the chessboard with queen positions.
    """

    for row in board:
        print("[", end="")
        for col in row:
            print(col, end=", ")
        print("]")  # Remove the last comma and space


def main():
    """
    Main function that validates arguments and calls the solver.
    """

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty chessboard
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_n_queens(board, 0)


if __name__ == "__main__":
    main()