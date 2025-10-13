def fat_burning_heart_rate(age):
    """Calculates the fat-burning heart rate."""
    return 0.7 * (220 - age)

def get_age():
    """Gets the user's age and validates it. Age must be between 18 and 75"""
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError("Invalid age.")
    return age

if __name__ == "__main__":
    try:
        # Get the user's age
        age = get_age()
        
        # Calculate the fat-burning heart rate
        heart_rate = fat_burning_heart_rate(age)
        
        # Output the result
        print(f"Fat burning heart rate for a {age} year-old: {heart_rate:.1f} bpm")
    except ValueError as e:
        # Handle invalid age and print the error message
        print(e)
        print("Could not calculate heart rate info.")
