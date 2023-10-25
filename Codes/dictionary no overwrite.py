# Initialize an empty dictionary
my_dict = {}

# Key prefix for new keys
key_prefix = 'key'

# Initialize a counter for keys
counter = 1

# Collect three key-value pairs
for _ in range(3):
    new_key = f'{key_prefix}{counter}'
    new_value = input(f"Enter a value for {new_key}: ")

    my_dict[new_key] = new_value
    counter += 1

# Printing the final dictionary
print("Final Dictionary:", my_dict)

#This will already be able to create a dictionary to save new information data gave by the user

#If you want to use the same code but without the user input 

# Initialize an empty dictionary
my_dict = {}

# Key prefix for new keys
key_prefix = 'key'

# Initialize a counter for keys
counter = 1

# Collect three key-value pairs
for _ in range(3):
    new_key = f'{key_prefix}{counter}'
    new_value = #Your variable that comes from another part

    my_dict[new_key] = new_value
    counter += 1

# Printing the final dictionary
print("Final Dictionary:", my_dict)

#If you want to use the same code but without the For loop

# This tree if you are using inside a loop you need to move outside of the loop, otherwise gonna be erasing and creating a overwrite problem
my_dict = {}
key_prefix = 'key'
counter = 1

# Collect three key-value pairs
new_key = f'{key_prefix}{counter}'
new_value = #Your variable that comes from another part

my_dict[new_key] = new_value
counter += 1

# Printing the final dictionary
print("Final Dictionary:", my_dict)