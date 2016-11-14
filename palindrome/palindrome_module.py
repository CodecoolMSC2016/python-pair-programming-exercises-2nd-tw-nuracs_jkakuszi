def palindrome(str):
    str_without = str.replace(" ","").lower()
    revstr =  str_without[::-1]
    if revstr == str_without :
        return True
    else:
        return False



def main():
    print(palindrome(str))


if __name__ == '__main__':
    main()
