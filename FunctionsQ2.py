#Write a function called `calculate_factorial` that takes a number as a parameter and returns its factorial. The factorial of a number is the product of all positive integers up to that number.
def calculate_factorial(para1):
    if para1 == 0:
        return 1
    else:
        return para1 * calculate_factorial(para1 - 1)
print(calculate_factorial(10))