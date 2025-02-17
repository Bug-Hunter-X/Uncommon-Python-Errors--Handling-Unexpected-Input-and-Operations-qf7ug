def function_with_uncommon_error(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Invalid input types.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage demonstrating potential errors
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Error: Cannot divide by zero. None
print(function_with_uncommon_error(10, "a"))  # Output: Error: Invalid input types. None
print(function_with_uncommon_error(10, [1,2])) # Output: An unexpected error occurred: unsupported operand type(s) for /: 'int' and 'list' None