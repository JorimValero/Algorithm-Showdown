import json
import math
import itertools
import time

# Load the sample data
with open("sample_data.json", "r") as file:
    data = json.load(file)

route_data = data["problem2_delivery_route"]
stops = route_data["stops"]

# School is the starting and ending point
school = stops[0]
destinations = stops[1:]

def calculate_distance(point_a, point_b):
    x_difference = point_a["x"] - point_b["x"]
    y_difference = point_a["y"] - point_b["y"]

    return math.sqrt(
        x_difference ** 2 + y_difference ** 2
    )


def calculate_route_distance(route):
    total_distance = 0

    # Begin at School
    current_location = school

    # Visit every destination in the given order
    for stop in route:
        total_distance += calculate_distance(
            current_location, stop
        )
        current_location = stop

    # Return to School
    total_distance += calculate_distance(
        current_location, school
    )

    return total_distance

def brute_force_route():
    shortest_route = None
    shortest_distance = float("inf")

    # Try every possible order of destinations
    for route in itertools.permutations(destinations):
        distance = calculate_route_distance(route)

        if distance < shortest_distance:
            shortest_distance = distance
            shortest_route = route

    return shortest_route, shortest_distance

def nearest_neighbor_route():
    unvisited = destinations.copy()
    route = []
    current_location = school

    while unvisited:
        # Find the closest unvisited destination
        nearest_stop = min(
            unvisited,
            key=lambda stop: calculate_distance(
                current_location, stop
            )
        )

        route.append(nearest_stop)
        unvisited.remove(nearest_stop)
        current_location = nearest_stop

    return route, calculate_route_distance(route)

def run_delivery_route():
    print()
    print("PROBLEM 2: DELIVERY ROUTE")
    print()
    print("\nDelivery Locations:")
    for stop in stops:
        print(f"{stop['name']}: ({stop['x']}, {stop['y']})")

    # Run the brute force algorithm
    start_time = time.perf_counter()
    brute_route, brute_distance = brute_force_route()
    brute_time = time.perf_counter() - start_time

    # Run the nearest neighbor algorithm
    start_time = time.perf_counter()
    greedy_route, greedy_distance = nearest_neighbor_route()
    greedy_time = time.perf_counter() - start_time

    # Display brute force results
    print()
    print("BRUTE FORCE RESULTS")
    print()

    brute_route_names = (
        [school["name"]]
        + [stop["name"] for stop in brute_route]
        + [school["name"]]
    )

    print("Route:", " -> ".join(brute_route_names))
    print(f"Total Distance: {brute_distance:.2f}")
    print(f"Execution Time: {brute_time:.6f} seconds")

    # Display nearest neighbor results
    print()
    print("NEAREST NEIGHBOR RESULTS")
    print()

    greedy_route_names = (
        [school["name"]]
        + [stop["name"] for stop in greedy_route]
        + [school["name"]]
    )

    print("Route:", " -> ".join(greedy_route_names))
    print(f"Total Distance: {greedy_distance:.2f}")
    print(f"Execution Time: {greedy_time:.6f} seconds")

    # Compare the results
    print()
    print("COMPARISON")
    print()

    print(f"Brute Force Distance: {brute_distance:.2f}")
    print(f"Nearest Neighbor Distance: {greedy_distance:.2f}")

    if brute_distance < greedy_distance:
        print("Brute Force found the shorter route.")
    elif greedy_distance < brute_distance:
        print("Nearest Neighbor found the shorter route.")
    else:
        print("Both algorithms found routes of equal distance.")

    if brute_time < greedy_time:
        print("Brute Force ran faster on this test.")
    elif greedy_time < brute_time:
        print("Nearest Neighbor ran faster on this test.")
    else:
        print("Both algorithms took approximately the same time.")


# Allow this file to run independently
if __name__ == "__main__":
    run_delivery_route()