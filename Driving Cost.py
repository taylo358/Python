def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    """
    Calculate the cost of driving based on fuel efficiency, fuel cost, and distance.

    :param miles_per_gallon: Fuel efficiency in miles per gallon (float)
    :param dollars_per_gallon: Cost of gas per gallon (float)
    :param miles_driven: Distance driven in miles (float)
    :return: Cost of driving the given distance (float)
    """
    return (miles_driven / miles_per_gallon) * dollars_per_gallon


# Main program
if __name__ == "__main__":
    # Get user inputs for miles per gallon and dollars per gallon
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())

    # Calculate and output the results for 10 miles, 50 miles, and 400 miles
    cost_10_miles = driving_cost(miles_per_gallon, dollars_per_gallon, 10.0)
    cost_50_miles = driving_cost(miles_per_gallon, dollars_per_gallon, 50.0)
    cost_400_miles = driving_cost(miles_per_gallon, dollars_per_gallon, 400.0)

    # Print the costs with two decimal places
    print(f'{cost_10_miles:.2f}')
    print(f'{cost_50_miles:.2f}')
    print(f'{cost_400_miles:.2f}')
