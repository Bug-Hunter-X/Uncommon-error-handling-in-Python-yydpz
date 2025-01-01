def function_with_uncommon_error(x):
    try:
        result = 10 / x
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        if isinstance(x, str):
            return "String input not allowed"
        else:
            return "Unknown error"

print(function_with_uncommon_error(0)) # Output: Division by zero
print(function_with_uncommon_error(2)) # Output: 5.0
print(function_with_uncommon_error('a')) # Output: String input not allowed
print(function_with_uncommon_error([1,2])) # Output: Unknown error