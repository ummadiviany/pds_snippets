# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-08-16 01:31:23
#  * @modify date 2022-08-16 01:31:23
#  * @desc [description]
#  */
# Actual code starts below this line
# -----------------------------------------------------------


# How to input data from user?

sep_str = "-"*50


print(f"\n-------------------Input from user-------------------\n")
# 1. String input
name = input("Enter you name: ")

# Check if the input is a string
print(f"The type of entered value is {type(name)}")

# Print the input
print(f"Your name is {name}")
print(sep_str)

# 2. Integer input
number = int(input("Enter a number: "))

# Check if the input is an integer
print(f"The type of entered value is {type(number)}")

print(f"The number is {number}")