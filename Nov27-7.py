#Write a function that takes a string as input and counts the number of vowels in it.
vowels = ['a','e','i','o','u']
count = 0
str_val = input('Enter the string: ')
str_val_arr = [elements for elements in str_val]
for i in range(len(vowels)):
    for j in range(0,len(str_val_arr)):
        if vowels[i] == str_val_arr[j]:
            count += 1

print(count)