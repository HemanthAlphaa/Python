#   Write a function that checks if a given string is a palindrome.
#sol1
sol1 = 'radar' #input("Word: ")
reversed_sol1 = sol1[::-1]
if sol1 == reversed_sol1:
    print("Palindrome")
else:
    print("Not a Palindrome")

#sol2
arr=['string','ini','level','radar']
arr2 = []
for index in range(0,len(arr)):
    if arr[index] == arr[index][::-1]:
        arr2.append('Palindrome')
    else:
        arr2.append("Not a Palindrome")
print(arr2)

#sol3
arr = [121, 'string', 'ini', 'level', 'radar', 5678]
arr2 = []
for elements in arr:
    if isinstance(elements, str) and elements == elements[::-1]:
        arr2.append('Palindrome')
    else:
        arr2.append("Not a Palindrome")
print(arr2)