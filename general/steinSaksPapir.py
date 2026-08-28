import random

choices = ["stein", "saks", "papir"]

win = 0
loose = 0


while loose < 3 and win < 3:
    choice = str(input("Velg hånd: "))
    computer = random.randint(0, 2)

    try:
        choice = choices.index(choice)
        print("Motstander valgte ", choices[computer])

        if choice == ((computer + 1)%3):
            loose += 1
            print("Du tapte runden\n")

        elif choice == ((computer - 1)%3):
            win += 1
            print("Du vant runden\n")

        else:
            print("Uavgjort\n")

    except KeyError:
        print("Ugyldig input!")


if win > loose:
    print("Du vant spillet!")

else:
    print("Du tapte spillet")