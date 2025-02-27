from functools import reduce

# Define a list of numbers
num = [1, 2, 3, 4, 5]

# Use reduce() to find the product of the numbers
product = reduce(lambda x, y: x * y, num)

# Print the product
print("Product of the numbers:", product)