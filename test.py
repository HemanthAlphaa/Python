n = int(input('Enter the number: '))
arr = [index for index in range(1,n+1)]
n = int(input('Enter the number of multiples: '))
arr2 = [index for index in range(1,n+1)]
for index in range(len(arr)):
    for index2 in range(len(arr2)):
        print(f'{arr[index]} * {arr2[index2]} = {arr[index]*arr2[index2]}')
    print('*************')
