import random
import string


def passwordgen():
    choose = input("Wanna strong password? (If yes enter Y) :")
    mypw = []
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "?"]
    if choose == "Y":
        for i in range(2):
            mypw.append(str(random.randint(1, 9)))
            mypw.append(random.choice(string.ascii_uppercase))
            mypw.append(random.choice(string.ascii_lowercase))
            mypw.append(random.choice(symbols))
        print("Your password: " + "".join(mypw))
        mypw = str(mypw)
        return mypw
    else:
        easy = []
        choose_easy = ["Kutya1234!", "Cica4321!", "Jelszo123!", "Alma2222!"]
        easy.append(random.choice(choose_easy))
        print("Your password: " + easy[0])
        easy = str(easy)

    return easy


def main():
    passwordgen()

    return


if __name__ == '__main__':
   main()
