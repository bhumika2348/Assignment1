str = "  Hello, World!  "

# Using string methods
length = len(str)                # Get the length of the string
stripped_string = str.strip()    # Remove leading spaces
upper_string = str.upper()        # Convert to uppercase
lower_string = str.lower()        # Convert to lowercase
replaced_string = str.replace("World", "Python")  # Replace a substring
split_string = str.split(", ")    # Split the string into a list

# Print the results
print("Original string:", str)
print("Length of the string:", length)
print("Stripped string:", stripped_string)
print("Uppercase string:", upper_string)
print("Lowercase string:", lower_string)
print("Replaced string:", replaced_string)
print("Split string:", split_string)