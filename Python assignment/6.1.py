def evenno():
    for i in range(10):
        yield i * 2  # Yield even numbers: 0, 2, 4, ..., 18

# Create the generator
even = evenno()

# Print the first 10 even numbers
for number in even:
    print(number)