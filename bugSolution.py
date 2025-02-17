def function_with_uncommon_error(x, y):
    try:
        if not isinstance(x,(int,float)) or not isinstance(y,(int,float)):
            raise TypeError("Invalid input types. Both inputs must be numbers.")
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = x / y
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage demonstrating potential errors
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Error: Cannot divide by zero. None
print(function_with_uncommon_error(10, "a"))  # Output: Error: Invalid input types. Both inputs must be numbers. None
print(function_with_uncommon_error(10, [1,2])) # Output: Error: Invalid input types. Both inputs must be numbers. None