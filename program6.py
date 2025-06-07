def modify_arguments(num, my_list):
    print("\nInside function before changes:")
    print("num =", num)
    print("my_list =", my_list)
    
    num += 10           # Will NOT change original num
    my_list.append(100) # Will change original list
    
    print("Inside function after changes:")
    print("num =", num)
    print("my_list =", my_list)

# Immutable argument
x = 5

# Mutable argument
lst = [1, 2, 3]

print("Before function call:")
print("x =", x)
print("lst =", lst)

# Call the function
modify_arguments(x, lst)

print("\nAfter function call:")
print("x =", x)        # Still 5 (unchanged)
print("lst =", lst)    # Changed, now includes 100
