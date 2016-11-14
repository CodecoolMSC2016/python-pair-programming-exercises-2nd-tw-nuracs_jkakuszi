import datetime


def years(age):
    diff = 100-age
    current = datetime.date.today()
    return int(current.year) + diff
    return


def main():
    user = input("Give your name: ")
    age = int(input("Give your age: "))
    print("Welcome " + user)
    years(age)
    print(user + ", you will turn 100 in " + str(years(age)))
    return


if __name__ == '__main__':
    main()
