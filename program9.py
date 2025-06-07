# Take input from user (string by default)
user_input = input("Enter something: ")

# Convert to integer
try:
    int_value = int(user_input)
    print("Integer value:", int_value)
except ValueError:
    print("Cannot convert to integer.")

# Convert to float
try:
    float_value = float(user_input)
    print("Float value:", float_value)
except ValueError:
    print("Cannot convert to float.")

# Convert to boolean
# Rule: non-empty strings are True, empty string is False
bool_value = bool(user_input)
print("Boolean value:", bool_value)
