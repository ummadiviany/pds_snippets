# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-08-16 01:31:23
#  * @modify date 2022-08-16 01:31:23
#  * @desc [description]
#  */
# Actual code starts below this line
# -----------------------------------------------------------


# How to convert data types?

# 1. String to integer/float/ and vice versa

int_number = 10
float_number = 10.5

sep_str = "-"*50

# Converting int/float to string
print(f"\n-------------------Converting ints/floats to strings-------------------\n")

print(f"Integer number is {int_number} with type {type(int_number)}")
print(sep_str)

print(f"String of integer number is {str(int_number)} with type {type(str(int_number))}")
print(sep_str)

print(f"Float number is {float_number} with type {type(float_number)}")
print(sep_str)

print(f"String of float number is {str(float_number)} with type {type(str(float_number))}")
print(sep_str)


# Converting string to int/float

str_int = "10"
str_float = "10.5"

print(f"\n-------------------Converting strings to ints/floats-------------------\n")

print(f"String of integer number is {str_int} with type {type(str_int)}")
print(sep_str)

print(f"Integer of string is {int(str_int)} with type {type(int(str_int))}")
print(sep_str)

print(f"String of float number is {str_float} with type {type(str_float)}")
print(sep_str)

print(f"Float of string is {float(str_float)} with type {type(float(str_float))}")
print(sep_str)