def int_to_reverse_binary(integer_value):
    """
    Converts an integer to a string representing its binary form in reverse order.
    
    :param integer_value: The integer to convert (int)
    :return: A string of 1's and 0's in reverse order (str)
    """
    binary_reverse = ""
    while integer_value > 0:
        binary_reverse += str(integer_value % 2)
        integer_value //= 2
    return binary_reverse


def string_reverse(input_string):
    """
    Reverses the input string.
    
    :param input_string: The string to reverse (str)
    :return: The reversed string (str)
    """
    return input_string[::-1]


# Main program
if __name__ == "__main__":
    # Get input from user
    user_input = int(input())
    
    # Convert integer to reverse binary
    reverse_binary = int_to_reverse_binary(user_input)
    
    # Reverse the binary string to get the correct binary representation
    binary_representation = string_reverse(reverse_binary)
    
    # Output the result
    print(binary_representation)
