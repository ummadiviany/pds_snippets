# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-08-23 01:46:31
#  * @modify date 2022-08-23 01:46:31
#  * @desc [description]
#  */
# Actual code starts below this line
# -----------------------------------------------------------


# Continue and Break Statements

# Break Statement : Break statement is used to break out of the loop.

# Example 1:

find_number = 10
for i in range(1, 101):
    if i == find_number:
        print(f"{i} is found, breaking out of the loop")
        break



# Continue statement : Continue the loop and start the next iteration.
skip_multiple = 5
for i in range(1, 20):
    if i % skip_multiple == 0:
        print(f"Skipping {i}")
        continue
        # Any code after continue statement will not be executed and the next iteration will be started. 
    print(i)



# ------------------In Class Exercise-----------------
# Write a piece of code that finds out whether a number is a prime number or not.
# Prime numbers are numbers that have exactly two factors : 1 and itself.

# Steps:
# 1. Check if the number is less than or equal to 1. If it is, then it is not a prime number.
# 2. Iterate from 2 to the number itself.
#   3. If the number is divisible by any number between 2 and itself, then it is not a prime number.





# ---------------------------------------------------

# Additional exercise: Write a piece of code that prints the prime numbers between 1 and 100.