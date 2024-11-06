#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col].
    We check the column, and the two diagonals.
    """
    # Check column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, N, solutions):
    """
    Using backtracking to find all solutions.
    """
    # If we've placed queens in all rows, it's a valid solution
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return

    # Try placing the queen in all columns in the current row
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col  # Place queen
            solve_nqueens(board, row + 1, N, solutions)  # Recur to next row
            board[row] = -1  # Backtrack

def main():
    # Check command line arguments
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

    # Initialize the board as a list of N elements (-1 means no queen placed)
    board = [-1] * N
    solutions = []
    
    # Solve the problem using backtracking
    solve_nqueens(board, 0, N, solutions)
    
    # Print all solutions
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
