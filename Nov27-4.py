#Write a program that prints the numbers from 1 to 100. But for multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz." For numbers that are multiples of both three and five, print "FizzBuzz."

#MySol
#arr = [index for index in range(1,101)]
arr = []
for index in range(0,101):
    if index%3 == 0 and index%5 == 0:
        arr.append('FizzBuzz')
    elif index%5 == 0:
        arr.append('Buzz')
    elif index%3 == 0:
        arr.append('Fizz')
    else:
        arr.append(index)
print(arr)

#GPTSol
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
