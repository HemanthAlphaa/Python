#Given a list containing n distinct numbers taken from the range 0 to n, find the one that is missing from the list.


n = int(input('Range: '))
arr1 = [index for index in range(n+1)]
print(arr1)
arr1.remove(n-5)
if len(arr1) != n:
    for index in range(len(arr1)):
        if arr1[index] != index:
            print(f'{index} - in missing in the list')