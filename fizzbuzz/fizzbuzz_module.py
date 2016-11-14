def fizzbuzz(number):

    if number % 5 == 0 and number % 3 == 0:
        return "FizzBuzz"

    elif number % 3 == 0:
        return "Fizz"

    elif number % 5 == 0:
        return "Buzz"

    else:
        return number    
    
def main():
    for i in range(1, 101):
        print(fizzbuzz(i))
        fizzbuzz(i)
    return

if __name__ == '__main__':
    main()
