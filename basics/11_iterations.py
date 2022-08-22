# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-08-22 23:29:21
#  * @modify date 2022-08-22 23:29:21
#  * @desc [description]
#  */
# Actual code starts below this line
# -----------------------------------------------------------



# Iterators are used to either repeat a block of code or to iterate over a sequence of values.
# 
# In Python , we have following iterators:
# 1. While loop
# 2. For loop


# # ------------- Examples -----------------
# The below example is a very simple example, but it is a good example for understanding the looping mechanism.

# Example 1:
message = "Hello"
repeat = 10

# Initialize the counter
i = 0
# While loop
while i < repeat:
    print(message)
    # Increment the counter
    i = i + 1 
    # i = i + 1 is the same as i += 1


# Example 2:
# The same example as above, but with a for loop.

# For loop : for <variable> in <sequence>:
# For loop : Auto-incrementing counter
# range(<start>, <end>, <step>) : Returns a sequence of numbers, starting from <start> and ending before <end> (exclusive) with step <step>.

for i in range(0, repeat):
    print(message)
    
    
# ---------------In Class - Exercise -----------------
# Find the sum of all natural numbers from 1 to n.
# Description: 
# 1. n = 0 then sum = 0
# 2. n = 1 then sum = 1
# 3. n = 10 then sum = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55





# ----------------------------------------------------    

    
# ---------------In Class - Exercise -----------------
# Find the power of a number without using the ** operator or the math module.
# Description: 
# 1. 2 raised to the power of 3 is equal to 2 * 2 * 2 = 8
# 2. 3 raised to the power of 2 is equal to 3 * 3 = 9




# ----------------------------------------------------
    

# ---------------In Class - Excercise-----------------
# How to print a basic multiplication table ?
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# ...
# 5 x 10 = 50

# Write your code below




# --------------------------------------------------



# Example 3: Nested iterations

# While loop inside a while loop
i = 0
while i < 2:
    print("Inside the outer loop")
    j = 0
    while j < 2:
        print("Inside the inner loop")
        j += 1
    i += 1


# Nesting of for loops
for i in range(0, 2):
    print("Inside the outer loop")
    for j in range(0, 2):
        print("Inside the inner loop")
        
# Note : You can nest as many levels as you want.
# Note : You can combine while and for loops, no restrictions.
 
    

    