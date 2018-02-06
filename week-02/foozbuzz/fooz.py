def fob(limit):
    for num in range(1, int(limit + 1)):
        if num % 15 is 0:
            print(str(num) + ' FizzBuzz')
        elif num % 3 is 0:
            print(str(num) + ' Fizz')
        elif num % 5 is 0:
            print(str(num) + ' Buzz')
        else:
            print(num)

