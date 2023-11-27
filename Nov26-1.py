#Write a Python program to find the sum of all multiples of 3 or 5 below 1000.
arr=[]
for index in range(0,1000):
    if index%3 == 0 or index%5 == 0:
        arr.append(index)
print(sum(arr))