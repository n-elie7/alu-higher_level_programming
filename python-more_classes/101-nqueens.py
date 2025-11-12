#!/usr/bin/python3
"""N Queens puzzle solver"""
import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check diagonal (upper left)
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve_nqueens(n, row, board, solutions):
    """Recursively solve N queens using backtracking"""
    if row == n:
        # Found a solution - convert to required format
        solution = [[i, board[i]] for i in range(n)]
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)
            board[row] = -1  # Backtrack


def main():
    """Main function to handle input and solve N queens"""
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

    # Initialize board and solutions list
    board = [-1] * n
    solutions = []

    # Solve the puzzle
    solve_nqueens(n, 0, board, solutions)

    # Print all solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
