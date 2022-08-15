# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-08-16 00:30:02
#  * @modify date 2022-08-16 00:30:02
#  * @desc [description]
#  */
# Actual code starts below this line
# -----------------------------------------------------------

# There are there ways of printing in Python:

name = "Vinay"
course = "CS60013 : Programming and Data Structures"
semester = "Autumn"
year = 2022

# Expeceted output:
# Vinay is a student of CS60013 : Programming and Data Structures in Autumn of 2022

sep_str = "-"*50
print(sep_str)

# 1. The basic method
print(name + " is a student of " + course + " in " + semester + " of " + str(year))
print(sep_str)

# 2. Format method
print("{} is a student of {} in {} of {}".format(name, course, semester, year))
print(sep_str)

# 3. F-String method
print(f"{name} is a student of {course} in {semester} of {year}")
print(sep_str)

# 4. Modulus method
print("%s is a student of %s in %s of %d" % (name, course, semester, year))
print(sep_str)