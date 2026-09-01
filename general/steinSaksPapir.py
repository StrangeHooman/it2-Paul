import random
import time

choices = ["stein", "saks", "papir", "øgle", "spock", "kaktus", "bønne"]

win = 0
loose = 0

scoreLim = 3


while loose < scoreLim and win < scoreLim:
    choice = str(input(f"---------------------\nVelg en hånd: \nMulige valg {choices}\n\nDitt valg: "))

    time.sleep(0.5)

    # availableChoices = [].append(choices[(choice - 1) % 3])

    choice.index(choice)

    computer = random.randint(0, len(choices)-1)

    try:
        choice = choices.index(choice)
        print("Motstander valgte: ", choices[computer])

        if choice == computer:
            print("Uavgjort\n")
            time.sleep(1.5)

        elif abs(choice - computer) % 2 == 0:
            loose += 1
            print("Du tapte runden\n")
            time.sleep(1.5)

        elif abs(choice - computer) % 2 != 0:
            win += 1
            print("Du vant runden\n")
            time.sleep(1.5)

        else:
            print("Wut da hell?")

    except ValueError:
        if choice == "pistol":
            win += 1
            print("Light 'em up\n")
            time.sleep(1.5)

        else:
            print("Ugyldig input!\n")
            time.sleep(1.5)


if win > loose:
    print("Du vant spillet!")

else:
    print("Du tapte spillet")