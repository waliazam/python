# Creating a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Accessing items
print(my_dict["name"])  # Output: John

# Adding or updating items
my_dict["email"] = "john@example.com"  # Adds a new key-value pair
my_dict["name"] = "Jane"  # Updates the value associated with key "name"

# Removing items
del my_dict["city"]  # Removes the item with key "city"
my_dict.pop("age")  # Removes the item with key "age"

# Iterating over a dictionary
for key, value in my_dict.items():
    print(key, value)
