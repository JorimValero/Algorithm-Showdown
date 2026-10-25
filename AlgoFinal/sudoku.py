import json
import time

# Load the sample data
with open("sample_data.json", "r") as file:
    data = json.load(file)

sudoku_data = data["problem6_sudoku"]

puzzle_4x4 = sudoku_data["puzzle_4x4"]
puzzle_9x9 = sudoku_data["puzzle_9x9"]


def is_valid(grid, row, col, number, box_size):
    # Check the row
    if number in grid[row]:
        return False

    # Check the column
    for r in range(len(grid)):
        if grid[r][col] == number:
            return False

    # Find the top-left corner of the box
    box_row = (row // box_size) * box_size
    box_col = (col // box_size) * box_size

    # Check the box
    for r in range(box_row, box_row + box_size):
        for c in range(box_col, box_col + box_size):
            if grid[r][c] == number:
                return False

    return True
def brute_force_sudoku(original_grid):
    import itertools

    grid = [row[:] for row in original_grid]
    empty_cells = []

    # Find all empty cells
    for r in range(4):
        for c in range(4):
            if grid[r][c] == 0:
                empty_cells.append((r, c))

    attempts = 0

    # Generate every possible assignment for the empty cells
    for numbers in itertools.product(range(1, 5), repeat=len(empty_cells)):
        attempts += 1

        # Fill the empty cells
        for index, (r, c) in enumerate(empty_cells):
            grid[r][c] = numbers[index]

        # Check whether the completed grid is valid
        valid = True

        for r in range(4):
            for c in range(4):
                number = grid[r][c]

                if (
                    grid[r].count(number) != 1
                    or [grid[i][c] for i in range(4)].count(number) != 1
                ):
                    valid = False
                    break

            if not valid:
                break

        # Check the 2x2 boxes
        if valid:
            for box_row in range(0, 4, 2):
                for box_col in range(0, 4, 2):
                    box_numbers = [
                        grid[r][c]
                        for r in range(box_row, box_row + 2)
                        for c in range(box_col, box_col + 2)
                    ]

                    if len(set(box_numbers)) != 4:
                        valid = False
                        break

                if not valid:
                    break

        if valid:
            return grid, attempts

    return None, attempts

def backtracking_sudoku(original_grid, box_size):
    grid = [row[:] for row in original_grid]
    attempts = 0

    def solve():
        nonlocal attempts

        # Find the next empty cell
        for r in range(len(grid)):
            for c in range(len(grid)):
                if grid[r][c] == 0:

                    # Try each possible number
                    for number in range(1, len(grid) + 1):
                        attempts += 1

                        if is_valid(grid, r, c, number, box_size):
                            grid[r][c] = number

                            if solve():
                                return True

                            # Undo the choice and try another number
                            grid[r][c] = 0

                    return False

        # No empty cells remain
        return True

    if solve():
        return grid, attempts

    return None, attempts


def display_grid(grid):
    if grid is None:
        print("No solution found.")
        return

    for row in grid:
        print(" ".join(str(number) for number in row))


def run_sudoku():
    print()
    print("PROBLEM 6: SUDOKU SOLVER")
    print()

    # Display the original puzzles
    print("\n4x4 Sudoku Puzzle:")
    display_grid(puzzle_4x4)

    print("\n9x9 Sudoku Puzzle:")
    display_grid(puzzle_9x9)

    # 4x4 Brute Force
    print()
    print("4x4 SUDOKU - BRUTE FORCE")
    print()

    start_time = time.perf_counter()
    brute_solution, brute_attempts = brute_force_sudoku(puzzle_4x4)
    brute_time = time.perf_counter() - start_time

    display_grid(brute_solution)
    print(f"Attempts: {brute_attempts}")
    print(f"Execution Time: {brute_time:.6f} seconds")

    # 4x4 Backtracking
    print()
    print("4x4 SUDOKU - BACKTRACKING")
    print()

    start_time = time.perf_counter()
    backtrack_4x4, attempts_4x4 = backtracking_sudoku(puzzle_4x4, 2)
    backtrack_4x4_time = time.perf_counter() - start_time

    display_grid(backtrack_4x4)
    print(f"Attempts: {attempts_4x4}")
    print(f"Execution Time: {backtrack_4x4_time:.6f} seconds")

    # 9x9 Backtracking
    print()
    print("9x9 SUDOKU - BACKTRACKING")
    print()
    
    start_time = time.perf_counter()
    backtrack_9x9, attempts_9x9 = backtracking_sudoku(puzzle_9x9, 3)
    backtrack_9x9_time = time.perf_counter() - start_time

    display_grid(backtrack_9x9)
    print(f"Attempts: {attempts_9x9}")
    print(f"Execution Time: {backtrack_9x9_time:.6f} seconds")


# Allow this file to run independently
if __name__ == "__main__":
    run_sudoku()