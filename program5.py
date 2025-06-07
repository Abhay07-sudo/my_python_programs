my_list = [10, 20, 30]
print("Original list:", my_list)

my_list[1] = 99
print("Modified list:", my_list)

my_tuple = (10, 20, 30)
print("\nOriginal tuple:", my_tuple)

try:
    my_tuple[1] = 99
except TypeError as e:
    print("Error when trying to modify tuple:", e)
