# Define the custom exception class
class StudentInfoError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

# Function to find ID based on student's name
def find_ID(student_name, student_dict):
    if student_name in student_dict:
        return student_dict[student_name]
    else:
        raise StudentInfoError(f"Student ID not found for {student_name}")

# Function to find name based on student's ID
def find_name(student_id, student_dict):
    for name, id in student_dict.items():
        if id == student_id:
            return name
    else:
        raise StudentInfoError(f"Student name not found for {student_id}")

# Main program
if __name__ == "__main__":
    # Sample dictionary
    student_dict = {
        'Reagan': 'rebradshaw835',
        'Ryley': 'rbarber894',
        'Peyton': 'pstott885',
        'Tyrese': 'tmayo945',
        'Caius': 'ccharlton329'
    }
    
    # User input
    user_choice = int(input())  # 0 for finding ID, 1 for finding name
    search_value = input()      # Name or ID to search for

    try:
        if user_choice == 0:  # Find ID by name
            result = find_ID(search_value, student_dict)
        elif user_choice == 1:  # Find name by ID
            result = find_name(search_value, student_dict)
        else:
            raise ValueError("Invalid choice. Enter 0 to find ID or 1 to find name.")
        
        # Output result
        print(result)

    except (StudentInfoError, ValueError) as e:
        # Output exception message
        print(e)
