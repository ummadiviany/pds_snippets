# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-08-30 09:39:37
#  * @modify date 2022-08-30 09:39:37
#  * @desc [description]
#  */
# # Actual code starts below this line
# # -----------------------------------------------------------

# Example 1 : Recursion example cumilative sum of numbers from 1 to n
def sum_numbers(n):
    if n == 1:
        return 1
    return n + sum_numbers(n - 1)
    
# 1 + 2 + 3 = 6
print(f"Sum_numbers(3) = {sum_numbers(3)}")


# Example 2 : Recursion example factorial of a number
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
# 1 * 2 * 3 * 4 * 5 = 120
print(f"Factorial(5) = {factorial(5)}")


# Example 3 : Recursion example fibonacci series
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
# 1, 1, 2, 3
print(f"Fibonacci(4) = {fibonacci(4)}")


# ---------------------In Class Exercise-----------------
# Try to write a recrsive function that returns True if given string is palindrome or False if it is not.

def is_palindrome(my_str):
    
    if len(my_str) <= 1:
        return True
    else:
        if my_str[0] == my_str[-1]:
            return is_palindrome(my_str[1:-1])
        else:
            return False
    
print(f"is_palindrome('malayalam') = {is_palindrome('malayalam')}")