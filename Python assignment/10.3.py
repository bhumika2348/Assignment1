num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter() to get only odd numbers
odd_num = list(filter(lambda x: x % 2 != 0, num))

# Print the odd numbers
print("Odd numbers:", odd_num)