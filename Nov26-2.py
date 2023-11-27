#Write a function to calculate the factorial of a given number.

#Sol1
import math
print(math.factorial(5))

#Sol2
arr = []
a = 5
for index in range(0,a):
    arr.append(a-index)
finalvalue = 1
for index in range(0,len(arr)):
    finalvalue = finalvalue * arr[index]
print(finalvalue)

#Sol3 using functions
def factorials(n):
    if n == 0:
        return 1
    else:
        return n * factorials(n-1) 
print(factorials(5))