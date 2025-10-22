# Program: Taxi Fare Calculator

BASE_FARE = 50
RATE_PER_KM = 10

def fare_for_trip(distance):
    """Computes fare for one trip."""
    return BASE_FARE + (RATE_PER_KM * distance)

def show_total(trip_list):
    """Displays fare for each trip and total fare."""
    total_sum = 0
    for idx, dist in enumerate(trip_list, start=1):
        trip_cost = fare_for_trip(dist)
        print(f"Trip {idx}: ₹{trip_cost}")
        total_sum += trip_cost
    print(f"Grand Total: ₹{total_sum}")

# Example run
trip_distances = [5, 10, 3]
show_total(trip_distances)
