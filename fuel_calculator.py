def calculate_trip_cost(mileage: float, one_way_distance: float, fuel_rate: float) -> tuple[float, float, float]:
    """
    Calculates the total distance, fuel required, and total cost for a round trip.
    """
    # Multiply by 2 for the round trip (going and coming back)
    total_distance = one_way_distance * 2
    
    # Calculate fuel needed
    fuel_needed = total_distance / mileage
    
    # Calculate total cost
    total_cost = fuel_needed * fuel_rate
    
    return total_distance, fuel_needed, total_cost

def main() -> None:
    # ANSI color codes
    RED = "\033[91m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RESET = "\033[0m"  # Resets the color back to normal

    print("========================================")
    print("      Trip Fuel Cost Calculator")
    print("========================================\n")
    
    try:
        # Taking inputs from the user
        mileage = float(input("Enter your vehicle's mileage (km per litre): "))
        
        if mileage <= 0:
            print("Error: Mileage must be greater than zero.")
            return

        distance = float(input("Enter the one-way distance to your destination (in km): "))
        fuel_rate = float(input("Enter the current Petrol/Diesel rate (per litre): "))

        # Performing the calculations
        total_distance, fuel_needed, total_cost = calculate_trip_cost(mileage, distance, fuel_rate)

        # Displaying the results with colors and 2 decimal places
        print("\n========================================")
        print("             Trip Summary")
        print("========================================")
        # Applying colors specifically to the result values
        print(f"Total Round-Trip Distance : {RED}{total_distance:.2f} km{RESET}")
        print(f"Total Fuel Required       : {YELLOW}{fuel_needed:.2f} litres{RESET}")
        print(f"Total Estimated Cost      : {GREEN}₹{total_cost:.2f}{RESET}")
        print("========================================\n")

    except ValueError:
        print("\nError: Invalid input. Please enter numbers only (e.g., 10 or 95.50).")

if __name__ == "__main__":
    main()
