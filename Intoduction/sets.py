# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements
my_set.add(6)

# Removing elements
my_set.remove(6)  # Raises a KeyError if the element is not found

# Set operations
another_set = {4, 5, 6, 7}
union_set = my_set.union(another_set)  # Union of my_set and another_set

# Iterating over a set
for element in my_set:
    print(element)
