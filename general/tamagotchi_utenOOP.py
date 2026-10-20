alle_dyr = [{"navn": "Dimbus", "sult" : 5, "energi" : 5, "glede" : 5}, {"navn": "Pusur", "sult" : 5, "energi" : 5, "glede" : 5}]

def clamp(num: int, min, max):
    if num < min:
        num = min

    elif num > max:
        num = max

    return num

def mate(dyr: dict):
    dyr["sult"] -=3
    dyr["glede"] += 1

def leke(dyr: dict):
    if energi > 2:
        dyr["glede"] += 3
        dyr["energi"] -= 2
        dyr["sult"] += 1

def sove(dyr: dict):
    dyr["energi"] += 4
    dyr["sult"] += 1

def adopter(dyr: dict):
    global alle_dyr    
    navn = input("Velg navn på det nye dyret: ")

    alle_dyr.append({"navn": navn, "sult" : 5, "energi" : 5, "glede" : 5})

    print(f"Gratulerer med dit nye dyr {navn}")

def status(dyr: dict):
    print(f"""
{dyr["navn"]}:
Sult: {dyr["sult"]}, Energi: {dyr["energi"]}, Glede: {dyr["glede"]}

""")

def tid():
    global alle_dyr

    for dyr in alle_dyr:
        dyr["sult"] += 1
        dyr["glede"] -= 1


def main():
    global sult, energi, glede

    while True:
        print("\n\n")

        for dyr in alle_dyr:
            dyr["sult"] = clamp(dyr["sult"], 0, 10)
            dyr["energi"] = clamp(dyr["energi"], 0, 10)
            dyr["glede"] = clamp(dyr["glede"], 0, 10)

            if dyr["sult"] > 7:
                print(f"{dyr["navn"]} er sulten.")

            if dyr["energi"] < 3:
                print(f"{dyr["navn"]} er sliten.")

            if dyr["glede"] < 3:
                print(f"{dyr["navn"]} er ulykkelig.")

            status(dyr)
        
        action = input(f"""
1: Mate, 2: Leke, 3: Sove, 4: Adopter, 0: Avsultt
Velg: """)

        action_reference = None

        if action == "1":
            action_reference = mate
        
        elif action == "2":
            action_reference = leke

        elif action == "3":
            action_reference = sove

        elif action == "4":
            adopter()

        elif action == "0":
            break

        else:
            print(f"Ugyldig kommando ({action}). Du må skrive et tall")

        if action_reference != None:
            print(f"Dyr du eier:")

            dyrenavn = []
            
            for dyr in alle_dyr:
                print(dyr["navn"])
                dyrenavn.append(dyr["navn"])

            dyr = input("Hvilket dyr vil du gjenomføre handlingen på? ")

            if dyr in dyrenavn:
                action_reference(alle_dyr[dyrenavn.index(dyr)])

        tid()
main()