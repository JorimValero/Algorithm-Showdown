from delivery_route import run_delivery_route
from budget_allocation import run_budget_allocation
from sudoku import run_sudoku


def main():
    print()
    print("ALGORITHM ANALYSIS FINAL PROJECT")
    print()

    run_delivery_route()

    input("\nPress Enter to continue to Problem 4...")

    run_budget_allocation()

    input("\nPress Enter to continue to Problem 6...")

    run_sudoku()
    print()
    print("       ALL PROBLEMS COMPLETED!")


if __name__ == "__main__":
    main()