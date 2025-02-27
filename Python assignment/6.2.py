class Integer:
    def __init__(self, integer_list):
        self.integer_list = integer_list  # Store the list of integers
        self.index = 0  # Initialize the index to 0

    def __iter__(self):
        return self  # The iterator object itself is returned

    def __next__(self):
        if self.index < len(self.integer_list):
            result = self.integer_list[self.index]  
            self.index += 1  # Move to the next index
            return result  # Return the current integer
        else:
            raise StopIteration  # Raise StopIteration when done

integers = [1, 2, 3, 4, 5]  # List of integers
iterator = Integer(integers)  # Create an instance of the custom iterator

for number in iterator:
    print(number)