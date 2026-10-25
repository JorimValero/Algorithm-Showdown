import json
import itertools
import time

# Load the sample data
with open("sample_data.json", "r") as file:
    data = json.load(file)

budget_data = data["problem4_budget_allocation"]

budget = budget_data["budget"]
items = budget_data["items"]

def brute_force_allocation(items, budget):
    best_items = []
    best_score = 0
    best_cost = 0

    # Try every possible combination of equipment
    for count in range(len(items) + 1):
        for combination in itertools.combinations(items, count):

            total_cost = sum(item["cost"] for item in combination)
            total_score = sum(item["score"] for item in combination)

            # Check whether the combination fits the budget
            if total_cost <= budget and total_score > best_score:
                best_items = list(combination)
                best_score = total_score
                best_cost = total_cost

    return best_items, best_score, best_cost

def greedy_allocation(items, budget):
    # Sort items by score-to-cost ratio, highest first
    sorted_items = sorted(
        items,
        key=lambda item: item["score"] / item["cost"],
        reverse=True
    )

    selected_items = []
    total_cost = 0
    total_score = 0

    for item in sorted_items:

        # Select the item if it fits within the remaining budget
        if total_cost + item["cost"] <= budget:
            selected_items.append(item)
            total_cost += item["cost"]
            total_score += item["score"]

    return selected_items, total_score, total_cost

def run_budget_allocation():
    print()
    print("PROBLEM 4: BUDGET ALLOCATION")
    print()
    print(f"\nAvailable Budget: {budget}")

    print("\nEquipment Requests:")

    for item in items:
        print(
            f"{item['name']:<15} "
            f"Cost: {item['cost']:<3} "
            f"Score: {item['score']}"
        )

    # Run brute force
    start_time = time.perf_counter()

    brute_items, brute_score, brute_cost = brute_force_allocation(
        items, budget
    )

    brute_time = time.perf_counter() - start_time

    # Run greedy
    start_time = time.perf_counter()

    greedy_items, greedy_score, greedy_cost = greedy_allocation(
        items, budget
    )

    greedy_time = time.perf_counter() - start_time

    # Display brute-force results
    print()
    print("BRUTE FORCE RESULTS")
    print()
    for item in brute_items:
        print(
            f"{item['name']} - Cost: {item['cost']}, "
            f"Score: {item['score']}"
        )

    print(f"Total Cost: {brute_cost}")
    print(f"Total Score: {brute_score}")
    print(f"Execution Time: {brute_time:.6f} seconds")

    # Display greedy results
    print()
    print("GREEDY RESULTS")
    print()

    for item in greedy_items:
        print(
            f"{item['name']} - Cost: {item['cost']}, "
            f"Score: {item['score']}"
        )

    print(f"Total Cost: {greedy_cost}")
    print(f"Total Score: {greedy_score}")
    print(f"Execution Time: {greedy_time:.6f} seconds")

    # Compare the results
    print()
    print("COMPARISON")
    print()

    print(f"Brute Force: Score {brute_score}, Cost {brute_cost}")
    print(f"Greedy: Score {greedy_score}, Cost {greedy_cost}")

    if brute_score > greedy_score:
        print("Brute Force found the higher total score.")
    elif greedy_score > brute_score:
        print("Greedy found the higher total score.")
    else:
        print("Both algorithms found the same total score.")

    if brute_time < greedy_time:
        print("Brute Force ran faster on this test.")
    elif greedy_time < brute_time:
        print("Greedy ran faster on this test.")
    else:
        print("Both algorithms took approximately the same time.")


# Allow this file to run independently
if __name__ == "__main__":
    run_budget_allocation()