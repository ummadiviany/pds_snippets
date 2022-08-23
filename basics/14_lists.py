# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-08-23 08:37:33
#  * @modify date 2022-08-23 08:37:33
#  * @desc [description]
#  */
# Actual code starts below this line
# -----------------------------------------------------------
# -----------------------------------------------------------

# Python Lists 
    # Lists are common sequence data types in Python.
    # Lists are a data structure that can hold multiple values.


# Properties of Lists
    # Can hold any type of data.
    # Lists are mutable. (meaning they can be changed)
    # Follows the order of insertion. (meaning supports indexing)


# -----------------------------------------------------------------------------------
# Creating a List 

# Creating a list using [] - square brackets
l = [1, 2, 3, 4, 5] # This is a list of integers.
print(f"List l: {l}")


# Creating a list using list() method
l = list((1, 2.0, "Hello", True)) # This is a list of mixed data types.
print(f"List l: {l}")

# -----------------------------------------------------------------------------------
# Accessing elements of a list

    # Accessing elements of a list using indexing
    # All Python sequences are zero-based indexed.
    # All Python sequences which support indexing can be indexed using forwards and backwards indexing. 

# This is forward indexing
print(f"l[0]: {l[0]}") # Accessing the first element of the list.

# This is backward indexing
print(f"l[-1]: {l[-1]}") # Accessing the last element of the list.


# -----------------------------------------------------------------------------------
# Changing elements of a list

print(f"Before changing l[0]: {l}") # Before changing the first element of the list.

l[0] = "Changed" # Changing the first element of the list.

print(f"After changing l[0]: {l}") # After changing the first element of the list.


# -----------------------------------------------------------------------------------
# Adding elements to a list

print(f"Before adding to l: {l}") # Before adding to the list.

l.append("Added") # Adding to the list.

print(f"After adding to l: {l}") # After adding to the list.


# -----------------------------------------------------------------------------------
# Deleting elements from a list

# Deleting elements from a list using del keyword
# Also called as index based deletion.

l.append("Deleted this item") # Adding to the list.

print(f"Before deleting from l: {l}") # Before deleting from the list.

del l[-1] # Deleting last element from the list.

print(f"After deleting from l: {l}") # After deleting from the list.


# Deleting elements from a list using remove() method
# Also called as value based deletion.

print(f"Before deleting from l: {l}") # Before deleting from the list.

l.remove(True) # Deletes the first instance of the specified value from the list.

print(f"After deleting from l: {l}") # After deleting from the list.

# -----------------------------------------------------------------------------------
# Slicing a list
# Slice a list using [start:end:step]
l = list(range(1, 11)) # This is a list of integers from 1 to 10.
print(f"List l: {l}")

# Slicing first 3 elements of the list.
print(f"Slicing first 3 elements of the list: {l[:3]}") 

# Slice last 3 elements of the list.
print(f"Slicing last 3 elements of the list: {l[-3:]}") 

# Slicing elements from 2nd to 5th element of the list.
print(f"Slicing elements from 2nd to 5th element of the list: {l[1:5]}") 

# Slicing elements at even index of the list.
print(f"Slicing elements at even index of the list: {l[::2]}")

# Slice elements at odd index of the list.
print(f"Slicing elements at odd index of the list: {l[1::2]}")

# Reverse the list.
print(f"Reverse the list: {l[::-1]}")

# -----------------------------------------------------------------------------------
# Extending a list








# -----------------------------------------------------------------------------------
