# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-08-22 23:29:21
#  * @modify date 2022-08-22 23:29:21
#  * @desc [description]
#  */
# Actual code starts below this line
# -----------------------------------------------------------

# In Python , we have the following control statements:
# 1. if
# 2. if else
# 3. if elif else

# Note : Control statements find their best use when combined with Iterators and flowing information.

# ------------- if -----------------
print(f"\n-------------------if-------------------\n")

# Example 1:

number = 10
if number == 10:
    print(f"{number} is equal to 10")

# Instead of using the == operator, we can use any of the comparison operators (>, <, >=, <=, !=) and 
# combine them with the logical operators (and, or, not).

# Working with logical operators:
# and - Returns True if both the operands are True.
# or - Returns True if either of the operands is True.
# not - Flips the True/False value of the operand.



# Example 2:

another_number = 20
if number > 5 and another_number > 10:
    print(f"{number} is greater than 5 and {another_number} is also greater than 10")    


# Example 3:

# The above example can be written as:
# This is called as nested if statement.
if number > 5:
    if another_number > 10:
        print(f"{number} is greater than 5 and {another_number} is also greater than 10")
        
        
# ----------------------- if else -----------------
# If-else statement is used to execute a block of code if a condition is True and another block of code if the condition is False.

print(f"\n-------------------if else-------------------\n")
        
# Example 4:

name = "Vinay" # Type of name is string
exam_type = "mid-term"
passed = None # Type of passed is None
score = 80 # Type of score is integer

# Check the score and print the message accordingly.
# If the score is greater than or equal to 50, then print "Passed" otherwise print "Failed".

if score >= 50:
    passed = True
else:
    passed = False
    
if passed:
    print(f"{name} has passed the {exam_type} exam with score {score}.")
else:
    print(f"{name} was unable to clear the {exam_type}")
    
    
# ------------------------In Class - Exercise------------------------------
# The above example can be cut down to single if-else statement.
# Try to do it yourself.





# -------------------------------------------------------------------------




# ------------------------If elif else------------------------------
# Why do we need if-elif-else statements when we can use if-else statements?
# Answer: When we want to explicitly check for specific conditions and make sure that only one of the conditions is True.

# In the below example, I want check the given city and only print message accordingly.
# Only one of the conditions is True.

# Example 5:

city = 'Hyderabad'

if city == 'Bangalore':
    print("Bangalore is the silicon valley of India")
elif city == 'Mumbai':
    print("Mumbai is the financial capital of India")
elif city == 'Hyderabad':
    print("Hyderabad is the biryani capital of India")
else:
    print("No city found")


# Example 6: Positive-Negative-Zero
# Task to check if the given number is positive, negative or zero.

number = -10
if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")
    
    

# --------------In Class - Exercise------------------------------
# Write a piece of that to find the largest of three numbers.
num1 = 5
num2 = 10
num3 = 15




# Hint: Use nested conditional statements.
# ---------------------------------------------------------------