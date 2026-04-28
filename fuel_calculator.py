def calculate_trip_cost(mileage: float, one_way_distance: float, fuel_rate: float) -> tuple[float, float, float]:
    """
    Calculates the total distance, fuel required, and total cost for a round trip.
    
    Args:
        mileage: The vehicle's mileage (km per litre).
        one_way_distance: The distance to the destination (km).
        fuel_rate: The cost of fuel per litre.
        
    Returns:
        A tuple containing (total_distance, fuel_needed, total_cost).
    """
    # Multiply by 2 for the round trip (going and coming back)
    total_distance = one_way_distance * 2
    
    # Calculate fuel needed
    fuel_needed = total_distance / mileage
    
    # Calculate total cost
    total_cost = fuel_needed * fuel_rate
    
    return total_distance, fuel_needed, total_cost

def main() -> None:
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

        # Displaying the results with 2 decimal places for neatness
        print("\n========================================")
        print("             Trip Summary")
        print("========================================")
        print(f"Total Round-Trip Distance : {total_distance:.2f} km")
        print(f"Total Fuel Required       : {fuel_needed:.2f} litres")
        print(f"Total Estimated Cost      : ₹{total_cost:.2f}")
        print("========================================\n")

    except ValueError:
        print("\nError: Invalid input. Please enter numbers only (e.g., 10 or 95.50).")

if __name__ == "__main__":
    main()
